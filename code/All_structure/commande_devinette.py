import discord
from All_structure.dico import Dico
class Arbre_Binaire:
    def __init__(self) -> None:
        self.data = None
        self.pere   : Arbre_Binaire = None
        self.Gauche : Arbre_Binaire = None
        self.Droite : Arbre_Binaire = None
    
    def add_data(self, data):
        self.data = data
    
    def add_Gauche(self):
        self.Gauche = Arbre_Binaire()
        self.Gauche.pere = self

    def add_Droite(self):
        self.Droite = Arbre_Binaire()
        self.Droite.pere = self

    def Go_Gauche(self):
        return self.Gauche
    
    def Go_Droite(self):
        return self.Droite
    
    def Go_back(self):
        return self.pere

    def Create_and_go_Droit(self, data):
        self.add_Droite()
        res = self.Go_Droite()
        res.add_data(data)
        return res

    def Create_and_go_Gauche(self, data):
        self.add_Gauche()
        res = self.Go_Gauche()
        res.add_data(data)
        return res
    
    def get_data(self): return self.data

tete = Arbre_Binaire()

tete.add_data("Est-ce un objet ?")
tete_gauche = tete.Create_and_go_Gauche("Est-ce un animal ?")  # Ajoute une question en cas où la réponse précédente est négative
tete.Create_and_go_Droit("Tu penses à un objet mais je ne sais pas lequel.")  # Ajoute une question en cas où la réponse précédente est positive

tete_gauche.Create_and_go_Gauche("C'est végétal : un arbre, une plante ou un champignon.")
tete_gd = tete_gauche.Create_and_go_Droit("Tu penses à un humain ?")

tete_gd.Create_and_go_Gauche("Tu penses à un animal, mais je ne sais pas lequel. Je ne connais pas tous les animaux et leurs caractéristiques.")
tete_gd.Create_and_go_Droit("Tu penses à un humain, connu ou inconnu, voire même fictif. Mais je ne connais pas beaucoup de personnes, héhéhé.")

# print(tete.data)

# rep = input("Reponse : oui ou non ")

# if (rep == "oui"):
#     print(tete.Go_Droite().get_data())
# if (rep == "non"):
#     print(tete.Go_Gauche().get_data())

class Partie_en_cour:
    def __init__(self, last_message : discord.Message, user: discord.User, index : Arbre_Binaire) -> None:
        self.last_message : discord.Message = last_message
        self.user : discord.User = user
        self.index : Arbre_Binaire = index
    

    def get_last_message(self): return self.last_message
    def get_user(self): return self.user
    def get_index(self): return self.index

    def say_no(self):
        self.index = self.index.Go_Gauche()
        return self.index.get_data()

    def say_yes(self):
        self.index = self.index.Go_Droite()
        return self.index.get_data()
    
    def end(self):
        return (self.index.Droite == None and self.index.Gauche == None)
    
    def new_message(self, message : discord.Message):
        self.last_message = message
    
    def back(self):
        if (self.index.pere == None): return False
        self.index = self.index.Go_back()
        return True

class Commande_devinette:
    def __init__(self):
        """
        Arbre binaire du jeux
        """
        self.message_user_index = Dico()
        self.tete = tete

    def get_info(self, user: discord.User):
        partie = self.message_user_index.get(user)
        if (partie == None):
            return None
        return partie[1]

    async def back(self, m : discord.Message, author : discord.User):
        partie : Partie_en_cour= self.get_info(user=author)
        if partie == None:
            await m.channel.send("tu n'as pas de partie en cour "+author.mention)
            return
        if (not partie.back()):
            await m.channel.send("Tu ne peux pas retourner en arriere.")
            return
        await m.channel.send("retour en arriere")
        n_m = await m.channel.send(partie.index.get_data())
        await n_m.add_reaction("✅")
        await n_m.add_reaction("❌")
        partie.new_message(n_m)

    async def reaction(self, reaction : discord.reaction.Reaction, user :discord.User):
        """
        dans l'evenemeent reaction
        """
        partie : Partie_en_cour = self.get_info(user)
        if (partie == None): return None
        if (partie.last_message != reaction.message):
            await reaction.message.channel.send("Euh si tu shouaite retournée en arriere il faus faire la commande \n\"!back\".")
            return
        else:
            await reaction.message.channel.send("Bien Alors :thinking:??")
        if (reaction.emoji == "❌"):
            newl_message = await reaction.message.channel.send(partie.say_no())
        elif (reaction.emoji == "✅"):
            newl_message = await reaction.message.channel.send(partie.say_yes())
        if (partie.end()):
            await self.fin_commande(partie)
        else:
            await newl_message.add_reaction("✅")
            await newl_message.add_reaction("❌")
            partie.new_message(newl_message)


    async def fin_commande(self, partie : Partie_en_cour):
        await partie.last_message.channel.send("Fin de partie.")
        self.message_user_index.del_key(partie.user)

    async def start_commande(self, message: discord.Message, user: discord.User):
        """
        ajoute l'user dans la liste user game on verifie qu'il n'est pas deja présente
        """

        dernier_message = await message.channel.send(self.tete.get_data())
        await dernier_message.add_reaction("✅")
        await dernier_message.add_reaction("❌")
        self.message_user_index.append(user, Partie_en_cour(dernier_message, user, self.tete))
        pass
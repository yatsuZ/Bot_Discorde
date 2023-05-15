from ast import List
import discord

class Arbre_Binaire:
    def __init__(self) -> None:
        self.data = None
        self.Gauche : Arbre_Binaire = None
        self.Droite : Arbre_Binaire = None
    
    def add_data(self, data):
        self.data = data
    
    def add_Gauche(self):
        self.Gauche = Arbre_Binaire()

    def add_Droite(self):
        self.Droite = Arbre_Binaire()

    def Go_Gauche(self):
        return self.Gauche
    
    def Go_Droite(self):
        return self.Droite
    
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

print(tete.data)

rep = input("Reponse : oui ou non ")

if (rep == "oui"):
    print(tete.Go_Droite().get_data())
if (rep == "non"):
    print(tete.Go_Gauche().get_data())

class Partie_en_cour:
    def __init__(self, last_message : discord.Message, user: discord.User, index : Arbre_Binaire) -> None:
        self.last_message : discord.Message = last_message
        self.user : discord.User = user
        self.index : Arbre_Binaire = index
    

    def get_last_message(self): return self.last_message
    def get_user(self): return self.user
    def get_index(self): return self.index

class Commande_devinette:
    def __init__(self):
        """
        Arbre binaire du jeux
        """
        self.message_user_index: List[Partie_en_cour] = []
        self.tete = tete

    def en_cour_dutilisation(self, user: discord.User) -> bool:
        pass

    def start_commande(self, message: discord.Message, user: discord.User):
        """
        ajoute l'user dans la liste user game on verifie qu'il n'est pas deja présente
        """
        pass
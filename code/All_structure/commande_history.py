from All_structure.Node_historique import PileH, NodeH

import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

emojie_History = ["➡️", "⬅️", "🗑️", "🏁"]

# def get_hisotiry_commande_data(message : discord.Message) -> str :

#     message = get_hisotiry_commande_data(dernier_message)
#     if (dernier_message == None):
#         await ctx.send(message)
#         return
#     else :
#         ajout_emojie : discord.Message = await ctx.send(message)
#         for emojie in emojie_History:
#             await ajout_emojie.add_reaction(emojie)

class Commande_History:
    def __init__(self):
        """
        Historique du commande serveur
        List de tout les utilisateur qui attende de pouvoir utilise la commande.
        BOOL qui dis si quelqun utilise la la commande actuellement
        la personne qui utilise la commande actuellement
        Liste de user
        Liste de channelle
        Liste de role
        Le dernier message que l'objet a envoyer pour le surpimer ou faire des interaction"""
        self.Historie_serveur : PileH =  None
        self.List_dattente : PileH = PileH()
        self.Index_message : NodeH = None
        self.Actif : bool = False
        self.Celui_qui_utilise_la_commande : discord.User = None
        self.Activer_dans_le_chanelle : discord.TextChannel = None
        self.Param_U = None
        self.Param_C = None
        self.Param_R = None
        self.Dernier_message_envoyer : discord.Message = None
    
    def affichage_data(self, message : discord.Message) -> str :
        if (message == None):
            return ("")
        serveur = message.guild
        channel = message.channel
        author = message.author
        anne = message.created_at.strftime("%Y")
        mois = message.created_at.strftime("%m")
        jour = message.created_at.strftime("%d")
        heur = message.created_at.strftime("%H")
        minute = message.created_at.strftime("%M")
        contenu = message.content
        message = "```ansi\n"+\
            "\n\t[0;37m Par                         : [0;35m" + str(author)+\
            "\n\t[0;37m Contenu                     : [0;33m" + contenu +\
            "\n\t[0;37m Dans le channelle           : \"[0;32m" + str(channel) +"[0;37m\""\
            "\n\t[0;37m Dans le serveur             : \"[0;31m" + str(serveur) +"[0;37m\""\
            "\n\t[0;37m Envoyer le [0;36m" + jour + "/"+ mois + "/" + anne + " à "+heur+"H"+minute+\
            "```"
        return message

    def get_node_message(self) -> NodeH:
        """
        Fonction qui recupere la Node message ayant le message le plus recent avec les parrametre valide.
        """
        return self.Historie_serveur.get_message(self.Param_U, self.Param_C, self.Param_R)
    
    async def Fin_de_commande(self):
        """
        Fin de commande remet tout a leur valeur initial
        et mentione tout ce qui son dans la liste d'attente que le user a fini.
        """
        self.Historie_serveur=  None
        message_de_fin = self.Celui_qui_utilise_la_commande.mention + " a fini d'utilise la commande historie.\n"
        while self.List_dattente.size:
            message_de_fin = message_de_fin + self.List_dattente.pop().mention + " "
        message_de_fin = message_de_fin + "\nVous pouvez executer la commande !history, premier arriver premier servie ."
        self.Index_message : NodeH = None
        self.Actif : bool = False
        self.Celui_qui_utilise_la_commande : discord.User = None
        await self.Activer_dans_le_chanelle.send(message_de_fin)
        await self.Activer_dans_le_chanelle.send("https://tenor.com/view/who-will-be-the-first-king-dice-the-cuphead-show-whos-up-first-whos-wants-to-start-gif-22556332")
        self.Activer_dans_le_chanelle : discord.TextChannel = None
        self.Param_U = None
        self.Param_C = None
        self.Param_R = None
        self.Dernier_message_envoyer : discord.Message = None
    
    async def add_emojie(self):
        """
        J'ajoute des emojie au dernier message envoyer en fonction de lindex
        """
        if self.Index_message.next != None:
            await self.Dernier_message_envoyer.add_reaction("⬅️")
        if self.Index_message.previous != None:
            await self.Dernier_message_envoyer.add_reaction("➡️")
        await self.Dernier_message_envoyer.add_reaction("🗑️")
        await self.Dernier_message_envoyer.add_reaction("🏁")


    async def Activation_de_la_commande(self, author: discord.User, channelle: discord.TextChannel, Historique_commande: PileH, Param_U, Param_C, Param_R):
        """
        C'est ça qui activera la classe. c ici que je dois metre un timer
        """
        if self.Actif:
            if not (self.List_dattente.push_No_double(author)):
                await channelle.send("Bon "+author.mention+" je tai deja dis dattendre vas harceler le mec qui utilise la commande c'est a dire "+ self.Celui_qui_utilise_la_commande.mention+" Pas moi donc arrete de marcerler >:(\nOu soi patient je sais pas attend t'es deja dans la liste dattente.")
                await channelle.send("https://tenor.com/view/stare-angry-mad-black-snake-moan-samuel-l-jackson-gif-17424729")
            else:
                await channelle.send("Salut " + author.mention + " Malheureusement la commande `history` est en cours d'utilisation par " + self.Celui_qui_utilise_la_commande.name + ".\nJe vais t'ajouter dans une liste d'attente, d'accord ? Quand il aura fini, je mentionnerai tout ceux qui sont sur la liste d'attente et ce sera le premier qui exécutera la commande qui pourra reprendre le relais.")
                print(author.name + " est ajouté dans la liste d'attente.")
            return
        self.Actif = True
        self.Activer_dans_le_chanelle = channelle
        self.Celui_qui_utilise_la_commande = author
        self.Param_U, self.Param_C, self.Param_R = Param_U, Param_C, Param_R
        self.Historie_serveur = Historique_commande
        self.Index_message = node_message = self.get_node_message()
        if (node_message == None):
            await channelle.send("Et Bien aucune commande fus trouver :smiling_face_with_tear:.")
            await self.Fin_de_commande()
            return
        self.Dernier_message_envoyer = await self.Activer_dans_le_chanelle.send(self.affichage_data(node_message.get_data()))
        await self.add_emojie()
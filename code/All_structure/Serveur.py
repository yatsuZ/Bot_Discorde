from All_structure.Node_historique import NodeH
from All_structure.Node_historique import PileH
from All_structure.commande_history import Commande_History
from All_structure.commande_aide import Commande_aide
from All_structure.commande_devinette import Commande_devinette
from All_structure.dico import Dico
import discord
import json

class Serveur_Discorde:
    def __init__(self, id_serveur):
        self.id_serveur = id_serveur
        self.list_id_chanelle = None
        self.list_id_user = None
        self.historique = PileH()
        self.Commande_Historique = Commande_History()
        self.Commande_aide = Commande_aide()
        self.Commande_devinette = Commande_devinette()
    
    def sauvegarde(self):
        dico = {
            "id_serveur" : self.id_serveur,
            "historique" : self.historique.sauvegarde()
        }
        return dico

    async def inactif_commande_historique(self):
        await self.Commande_Historique.inactif()

    async def commande_History_init(self, auhtor : discord.User, chanelle : discord.TextChannel, params):
        """
        Methode qui va activer l'objet commande_historique
        Et ne return rien la methode affiche tout seul dans le serveur
        """
        # print("activation de l'initialisation de commande historie.")
        await self.Commande_Historique.Activation_de_la_commande(auhtor, chanelle, self.get_historique(), params[0], params[1], params[2])
        
    def add_user(self, user_id):
        """
        ajoute un nouveaux id user
        """
        new_node = NodeH(user_id)
        if (self.list_id_user == None):
            self.list_id_user = new_node
            return
        self.list_id_user.previous = new_node
        new_node.next = self.list_id_user
        self.list_id_user = new_node

    def add_chanelle(self, channelle_id):
        """
        ajoute un nouveaux id channel
        """
        new_node = NodeH(channelle_id)
        if (self.list_id_chanelle == None):
            self.list_id_chanelle = new_node
            return
        self.list_id_chanelle.previous = new_node
        new_node.next = self.list_id_chanelle
        self.list_id_chanelle = new_node

    def check_if_user_exist(self, user_id):
        """
        Regarde si user_id est present dans list_id_user.
        return 0 si il y est present. 
        1 si user id est absent.
        """
        current = self.list_id_user
        while (current != None):
            if (current.get_data() == user_id): return 0
            current = current.next
        return (1)

    def check_if_channel_exist(self, channel_id):
        """
        Regarde si channel_id est present dans list_id_chanelle.
        return 0 si il y est present. 
        1 si user id est absent.
        """
        current = self.list_id_chanelle
        while (current != None):
            if (current.get_data() == channel_id): return 0
            current = current.next
        return (1)

    def get_all_user_id(self): return self.list_id_user
    def get_all_chanelle_id(self): return self.list_id_chanelle
    def get_historique(self): return self.historique

class List_Serveur:
    def __init__(self):
        self.list_serveur = Dico()
        self.size = 0
    
    def add_serveur(self, serveur_id):
        """
        ajoute un nouveaux id user
        """
        self.list_serveur.append(serveur_id, Serveur_Discorde(serveur_id))
    
    def serveur_existe(self, serveur_id):
        """
        verifie que se serveur id est deja ma liste.
        0 si l'id est trouver
        """
        return (self.list_serveur.get(serveur_id) == None)

    def get_serveur(self, serveur_id):
        """
        return l'objet serveur par raport a l'id.
        """
        if (self.serveur_existe(serveur_id)): return None
        res = self.list_serveur.get(serveur_id)
        return (res[1])

    def get_history_of_serv(self, serveur_id:int):
        """
        Return la pile historique du serveur
        """
        tmp = self.get_serveur(serveur_id)
        if (tmp == None):
            return None
        return tmp.get_historique()
    def get_last_data(self, serveur_id:int):
        """
        Return la derniere datacdu serveur
        """
        tmp = self.get_history_of_serv(serveur_id)
        if (tmp == None):
            return None
        return tmp.get_lastNode().get_data()
    def get_last_previous_data(self, serveur_id:int):
        """
        Return l'avant dernier message'
        """
        tmp = self.get_history_of_serv(serveur_id)
        if (tmp == None):
            return None
        tmp = tmp.get_lastNode().next
        if (tmp == None):
            return None
        return tmp.get_data()
    
    async def Commande_History_init(self, id_guild, author : discord.User, channelle : discord.TextChannel, List_user, List_channelle, List_role):
        """
        Retourne la dernier commande en fonction des parametre de plus l'objet serveur aura un attirbut objet commande historie qui aura un parama qui est 
        1. si il est initialise avec true false, si deja activé alors on ajoue le mec sur une liste dattente de la commande.
        """
        bon_serveur = self.get_serveur(id_guild)
        if (bon_serveur == None):
            return ("ERROR la guild id n'est pas dans ba bdd. ce ne devrais pas etre possible.")
        params = [List_user, List_channelle, List_role]
        await bon_serveur.commande_History_init(author, channelle, params)
    
    async def inactif_commande_historique(self, id_serv):
        await self.get_serveur(id_serv).inactif_commande_historique()
    
    def sauvegarde(self):
        """
        Sauvegarde tout en format json
        # Convertir les données en un format JSON
        # Renvoyer les données au format JSON
        """
        data = {
            "List_Serveur" : self.list_serveur.sauvegarde()
        }

        with open("yassbot.json", "w") as fichier:
            json.dump(data, fichier)


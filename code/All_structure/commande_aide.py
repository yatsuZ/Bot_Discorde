import discord
from discord.ext import commands

class Commande_aide:
    def __init__(self):
        """
        Dictionaire : message -> key, value -> user
        """
        self.List_message_User = []
    
    def add_message_user(self, message : discord.Message, user : discord.User):
        self.List_message_User.append([message, user])
    
    def find_by_message(self, message: discord.Message):
        """
        Chercher dans la liste des messages et renvoyer le tableau de 2 éléments correspondant au message
        """
        for entry in self.List_message_User:
            if entry[0] == message:
                return entry
        
        return None
    
    def del_message_user(self, message: discord.Message):
        """
        Supprime le message et son utilisateur de la liste des messages
        """
        for entry in self.List_message_User:
            if entry[0] == message:
                self.List_message_User.remove(entry)
                return
        
        return None

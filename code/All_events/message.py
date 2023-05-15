import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from All_structure import List_Serveur

###################################################################################### EVENT Message

def add_event_on_message(yassbot : commands.Bot, List_serveur : List_Serveur):
    """
    Le yassbot aura la l'event on_message
    """

    All_Serveurs = List_serveur

    @yassbot.event
    async def on_message(message):
        '''
        L'event activera la fonction a chaque fois qu'un utilisateur.
        Ecxepter Yassbot.
        '''
        if message.author == yassbot.user:
            return

        serveur = All_Serveurs.get_serveur(message.guild.id)
        if (serveur == None):
            All_Serveurs.add_serveur(message.guild.id)
            serveur = All_Serveurs.get_serveur(message.guild.id)
        message.content = message.content.lower()

        if message.content.startswith("hello"):
            await message.channel.send("Wesh ma guel.")
        if message.content == "ping":
            await message.channel.send("pong")
        if message.content == "quoicoubaka":
            await message.channel.send("https://media.tenor.com/GOYRQva4UeoAAAAd/anime-dance.gif")
        if (message.content == None or message.content == ""):
            return
        if message.content[0] == "!":
            command_name = message.content[1:].split()[0]
            command = yassbot.get_command(command_name)
            if command:
                serveur.historique.push(message)
                await yassbot.process_commands(message)
        All_Serveurs.sauvegarde()

    return Description

Description = (
    "\n> **on_message**:\n>\t- Quand quelqu'un envoie un message. ***L'ÉVÉNEMENT LE PLUS IMPORTANT.*** Cela permet de savoir si quelqu'un a envoyé une commande.\n>\tRéagit si quelqu'un envoie :\n"
    "\n```python\nQui commence par : \"hello ...\".\nExactement : \"ping\", \"quoicoubaka\"\n```"
)
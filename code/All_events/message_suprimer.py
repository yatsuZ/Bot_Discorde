import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

###################################################################################### Event Suppression de message

def add_event_message_suprimer(yassbot : commands.Bot):
    """
    Le yassbot aura la l'event on_message_delete
    """

    @yassbot.event
    async def on_message_delete(message):
        # pass
        print("Un message a été supprimé.")
        # print(f"Contenu du message : {message.content}")
    
    return Description

Description = (
    "\n> **on_message_delete**:\n>\t- Quand un message est supprimé. \"**Un message a été supprimé.**\" sera affiché dans le serveur de YassBot."
)
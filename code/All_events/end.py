import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

###################################################################################### Event quand le bot se deconnecte

def add_event_disconecte(yassbot : commands.Bot):
    """
    Le yassbot aura la l'event on_disconnect
    """

    @yassbot.event
    async def on_disconnect(message):
        # pass
        print("Bay Bay.")
        # print(f"Contenu du message : {message.content}")
    
    return Description

Description = (
    "\n> **on_disconnect**:\n>\t- Quand le bot se decconecte il effecture une sauvgarde de toute ces données."
)
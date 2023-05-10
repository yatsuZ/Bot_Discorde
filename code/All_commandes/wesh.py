import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

###################################################################################### Commande wsh

def add_commande_wesh(yassbot : commands.Bot, mon_id : int):
    """
    Le yassbot aura la commande wesh
    """
    @yassbot.command(name="wsh")
    @commands.guild_only()
    async def say_hello(ctx):
        '''
        Si un user envoie : "!wsh".
        alors le yassbot mementionera et l'auteur de celui qui a envoyer la commande.
        '''
        user = ctx.author
        yatsu = yassbot.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
        await ctx.send("Wsh "+user.mention+".\nJe suis un yassbot pas encore fini fait par "+ yatsu.mention +".")
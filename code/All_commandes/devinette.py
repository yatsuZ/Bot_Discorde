## Faire la commande devinette
## Commande deriver 
#- "restarte" : permettra de recommencer la discution
# - "speak about X" : permettra de savoir si un sujet est traité par le bot ou non (exemple : speak about python dira si oui ou non le bot parle de python)
# Fair qu'il prend un parametre resultat !devinette param si il y a param en tant que resultat return true
# Faire !add_devinette rajoute une question reponse
import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from All_structure import List_Serveur, Serveur_Discorde
###################################################################################### Commande wsh

def add_commande_devinette(yassbot : commands.Bot, Tout_les_serveurs : List_Serveur) -> str:
    """
    Le yassbot aura la commande devinette
    """

    All_serv = Tout_les_serveurs
    message_de_depart = "Salut tu comence le jeux de devinette\nX : Non\nV : OUI"

    @yassbot.command(name="devinette")
    @commands.guild_only()
    async def say_hello(ctx):
        '''
        initiliase le jeux de devinette
        '''
        await ctx.send(message_de_depart)
        await ctx.send("metre gif akinator")
        serveur : Serveur_Discorde = All_serv.get_serveur(ctx.guild.id)
    
    return Description

Description = "\n> **!devinette**:\n>\t- On commence un jeux de devinette seulement avec OUI ou NON .\n"
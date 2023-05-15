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
    message_de_depart = "Salut tu commence le jeux de devinette\n❌ : Non\n✅ : OUI"

    @yassbot.command(name="devinette")
    @commands.guild_only()
    async def devinette(ctx):
        '''
        initiliase le jeux de devinette
        '''
        serveur : Serveur_Discorde = All_serv.get_serveur(ctx.guild.id)
        if (serveur.Commande_devinette.message_user_index.get(ctx.author) != None):
            await ctx.send("Salut "+ctx.author.mention+". Tu es deja en train de jouer aux devinette termine ta partie.")
            return
        await ctx.send(message_de_depart)
        dernier_message = await ctx.send("https://tenor.com/view/aladdin-and-the-king-of-thieves-genie-raise-eyebrows-grin-smile-gif-15623514")
        await serveur.Commande_devinette.start_commande(message=dernier_message, user=ctx.author)
    
    return Description

Description = "\n> **!devinette**:\n>\t- On commence un jeux de devinette seulement avec OUI ou NON .\n"
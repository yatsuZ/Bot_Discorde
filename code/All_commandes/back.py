from discord.ext import commands
from All_structure import List_Serveur
from dotenv import load_dotenv

###################################################################################### Commande back

def add_commande_back(yassbot : commands.Bot, all_serv : List_Serveur) -> str:
    """
    Le yassbot aura la commande back
    """
    All_serveur = all_serv
    @yassbot.command(name="back")
    @commands.guild_only()
    async def devinette_back(ctx):
        user = ctx.author
        serv = All_serveur.get_serveur(ctx.guild.id)
        await serv.Commande_devinette.back(ctx.message, user)
    
    return Description

Description = "\n> **!back**:\n>\t- Si l'utilisateur joue aux devinette cela lui permetra de retoruner en arrier en cas de mauvais choix.\n"
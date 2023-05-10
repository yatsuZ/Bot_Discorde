import asyncio
import discord
from discord.ext import commands
from All_structure import List_Serveur

###################################################################################### Commande derniere _commande
def add_commande_derniere_commande(yassbot : commands.Bot, List_serveur : List_Serveur) -> str:
    """
    Le yassbot aura la commande derniere_commande
    """

    All_Serveurs = List_serveur

    @yassbot.command(name="derniere_commande")
    @commands.guild_only()
    async def derniere_commande(ctx):
        '''
        Affiche la dernière commande avec les informations.
        '''
        dernier_message = All_Serveurs.get_last_previous_data(ctx.guild.id)
        message = get_hisotiry_commande_data(dernier_message)
        if (dernier_message == None):
            await ctx.send(message)
            return
        await ctx.send("Voici les informations de l'avant dernière commande...\nVus que la derniere comande c'est celle que vous venez de rentrez ... enfin bref voila:"+message)

    return Description

def get_hisotiry_commande_data(message : discord.Message) -> str :
    if (message == None):
        return ("Aucune commande n'as encore etais envoyer.")
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

Description = "\n> **!derniere_commande**:\n>\t- Affiche les informations suivantes : l'auteur, le contenu et la date de la dernière commande envoyée dans le serveur, ainsi que le nom du canal.\n"
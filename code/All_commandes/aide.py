import asyncio
import discord
from discord.ext import commands
from All_structure import List_Serveur

###################################################################################### Texte + Comande Aide

message_aide = "**Yo Yasbot va t'aider !!**\n" + \
    "Salut, sur quoi as-tu besoin d'aide ? Sélectionne l'emoji correspondant.\n" + \
    "\n-\t ℹ️ : Je me présente :```Si tu te demandes qui est Yassbot ?```" + \
    "\n-\t 📄 : Je liste toutes mes commandes.```Si tu te demandes ce que je peux faire ?```" + \
    "\n-\t 🪄 : Je liste tous mes événements.```Si tu te demandes quelles interactions je peux avoir ?```" + \
    "\n-\t ⚒️ : Je liste ce que je pourrais faire.```Si tu te demandes ce qui est en construction ?```" + \
    "\n-\t ❌ : Si tu n'as plus besoin d'aide,```(Le message ne se supprimera pas).```" + \
    "\n-\t 🗑️ : Tu as fini de lire le message d'aide.```Si tu shouaite surpimer le message d'aide.```" + \
    "\n\n***Seul l'auteur de ce message peut choisir et interagir avec ce message***.\n"

emojie_aide = ["ℹ️", "📄", "🪄", "⚒️", "❌", "🗑️"]

def add_commande_aide(yassbot : commands.Bot, timer : int, List_serveur : List_Serveur) -> str:
    """
    Le yassbot aura la commande aide.
    return la description de la commande.
    """
    
    All_Serveurs = List_serveur

    @yassbot.command(name="aide")
    @commands.guild_only()
    async def aide(ctx):
        '''
        Affiche un message d'aide sur le serveur.
        '''
        messgae_auteur: discord.Message = All_Serveurs.get_last_data(ctx.guild.id)
        auteur_id = messgae_auteur.author.id
        message: discord.Message = await ctx.send(message_aide + "||Apres ***"+str(timer)+"*** secondes ce message se GOGOGADGET-autodétruira :detective:.\n"+"Toi actuellement :||\nhttps://thumbs.gfycat.com/TepidCloudyArmadillo-max-1mb.gif")
        All_Serveurs.get_serveur(ctx.guild.id).historique_reponse_BOT.push_No_double(message)
        for emojie in emojie_aide:
            await message.add_reaction(emojie)
        await asyncio.sleep(timer)
        try:
            msg = await ctx.channel.fetch_message(message.id)
        except discord.NotFound:
            return
        for reaction in msg.reactions:
            if reaction.emoji == "❌":
                async for user in reaction.users():
                    if user.id == auteur_id:
                        await ctx.send("Fin du compte à rebour. l'auteur est activer ❌ le message d'aide ne sera pas suprimer. Sauf si vous apuyer sur 🗑️.")
                        return
                break
        await message.delete()
        await reaction.message.channel.send("https://hellogiggles.com/wp-content/uploads/sites/7/2016/07/10/giphy31.gif")
    return Description

Description = "\n> **!aide**:\n>\t- Affiche le répertoire des commandes.\n"
import nest_asyncio
import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

from All_structure.Node_historique import NodeH, PileH
from All_structure.Serveur import List_Serveur, Serveur_Discorde

All_Serveurs = List_Serveur()

mon_id = 284082499649273856

nest_asyncio.apply()

intents = discord.Intents.all()

yassbot = commands.Bot(command_prefix="!", intents = intents)

Explication_commande = [
    "!aide:\n\t-Affiche le repertoire des commandes.",
    "!wsh :\n\t-Le bot vous salura en vous mentionant et mentionara son createur.\n",
    "!king_krimson:\n\t-les 10 derniers message serons suprimer + doit afficher un gif de king_krimson.\n\t(JOJO REF TU CONNAIS.)",
    "!ajout_serveur:\n\t-La premier commande a faire tant que cette comande n'est pas faite je n'interagirai pas avec ce serveur.\n\tC'est pour que vous ajouter \"manuellement\" ce serveur dans ma base de donnée."
                        ]

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

@yassbot.command(name="king_krimson")
async def delete(ctx):
    '''
    Si un user envoie : "!king_krimson".
    Alors le yassbot suprimera les 10 dernier message.
    et affiche un gif de king_krimson.
    '''
    async for message in ctx.channel.history(limit=10):
        await message.delete()

@yassbot.command(name="ajout_serveur")
@commands.guild_only()
async def ajout_serveur(ctx):
    '''
    Ajoue du serveur dans la liste de mon bot.
    '''
    user = ctx.author
    if (All_Serveurs.serveur_existe(ctx.guild.id)):
        await ctx.send(""+user.mention+" a ajouter le serveur "+ctx.guild.name+" dans les données de \""+yassbot.user.mention+"\".\nA present vous pouvez interagir avec moi dans ce serveur.")
        All_Serveurs.add_serveur(ctx.guild.id)
        return
    else:
        await ctx.send("J'ai deja ajouter le serveur : \""+ctx.guild.name+"\". Dans mes donnée à présent tu peut utilise mes commande fais\n!help si tu veux voir ce que je peux faire.")



message_aide = "Salut sur quoi a tu besoin d'aide ? Appuye sur quoi a besoin tu d'aide \n\t-📄 : Je liste toute mes commande.\n\t-ℹ️: Je me presente\n\t-❌: Si tu n'as plus besoin d'aide.\n\nSeul l'auteur de ce message peux choisir. Si l'auteur du message ne choisi rien apres plus de 20 seconde\nou apres avoir choisi ce message s'auto detruira"

@yassbot.event
async def on_reaction_add(reaction, user):
    historique = All_Serveurs.get_serveur(user.guild.id).historique
    auteur_id: discord.message.Message = historique.get_lastNode().get_data()
    print(auteur_id.author.name)
    if user.id == auteur_id.author.id and reaction.message.content == message_aide:
        if reaction.emoji == "📄" or reaction.emoji == "ℹ️" or reaction.emoji == "❌":
            await reaction.message.delete()

@yassbot.command(name="aide")
@commands.guild_only()
async def aide(ctx):
    '''
    Affiche un message d'aide sur le serveur.
    '''
    message = await ctx.send(message_aide)
    await message.add_reaction("📄")
    await message.add_reaction("ℹ️")
    await message.add_reaction("❌")


@yassbot.command(name="derniere_commande")
@commands.guild_only()
async def derniere_commande(ctx):
    '''
    Affiche la derniere commande avec les information.
    '''
    historique_du_serveur = All_Serveurs.get_serveur(ctx.guild.id).historique
    dernier_message = historique_du_serveur.get_lastNode().get_data()
    await ctx.send("message = "+ dernier_message.content)


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
    # if (message.content == "!ajout_serveur"):
    #     await yassbot.process_commands(message)
    #     All_Serveurs.get_serveur(message.guild.id).historique.push(message)
    #     return
    # elif (message.content[0] == "!" and serveur == None):
    #         await message.channel.send("Aie je ne connais pas encore ce serveur :(.\nFait la commande !ajout_serveur.\nSi tu veux que je puisse ajouter le serveur : \""+message.guild.name+"\" dans mon repertoire et que tu puisse m'utiliser.")
    #         return

    message.content = message.content.lower()

    if message.content.startswith("hello"):
        await message.channel.send("Wesh ma guel.")
    if message.content == "ping":
        await message.channel.send("pong")
    

    if message.content[0] == "!":
        command_name = message.content[1:].split()[0]
        command = yassbot.get_command(command_name)
        if command:
            serveur.historique.push(message)
            await yassbot.process_commands(message)# Executera la commande du message.

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    yassbot.run(TOKENBOT)
else:
    print("Absence de clés.")

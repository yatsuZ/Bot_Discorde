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

Makrdown = (
    "Voici un message de démonstration avec différentes utilisations de Markdown :"
    "\n\n**Texte en gras**"
    "\n*Texte en italique*"
    "\n***Texte en gras et italique***"
    "\n\n# Titre de niveau 1"
    "\n## Titre de niveau 2"
    "\n### Titre de niveau 3"
    "\n\n- Liste à puces item 1"
    "\n- Liste à puces item 2"
    "\n\n1. Liste numérotée item 1"
    "\n2. Liste numérotée item 2"
    "\n\n> Citation de texte"
    "\n\n`Code en ligne`"
    "\n\n```\nBloc de code\n```"
    "\n\n[Texte avec un lien](https://www.example.com)"
    "\n\n![Image avec une légende](https://www.example.com/image.jpg 'Légende de l\'image')"
    "\n\n||Texte Cachée||"
    "\n\n~~Texte Barée~~"
)

@yassbot.command(name="markdown")
@commands.guild_only()
async def show_all_markdown_discorde(ctx):
    '''
    Afficher out les effet de texte possible markdown sous discorde
    '''
    print("Il doit se passer quelque chose")
    await ctx.send("test")
    await ctx.send(Makrdown)


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

@yassbot.event
async def on_message_delete(message):
    print("Un message a été supprimé.")
    # print(f"Contenu du message : {message.content}")


Explication_commande = [
    "!aide:\n\t-Affiche le repertoire des commandes.\n",
    "!wsh :\n\t-Le bot vous salura en vous mentionant et mentionara son createur.\n",
    "!king_krimson:\n\t-les 10 derniers message serons suprimer + doit afficher un gif de king_krimson.\n\t(JOJO REF TU CONNAIS.)\n",
                        ]

@yassbot.event
async def on_reaction_add(reaction:discord.reaction.Reaction, user:discord.member.Member):
    if (user.id == yassbot.user.id):
        return
    if str(reaction.emoji) == "👍": 
        if user.id == reaction.message.author.id:
            await reaction.message.channel.send("L'utilisateur a réagi avec la réaction 👍. A son propre message trop con haha.")
    last_message = All_Serveurs.get_serveur(user.guild.id).historique.get_lastNode()
    if (last_message != None):
        auteur_id = last_message.get_data()
        if user.id == auteur_id.author.id and reaction.message.content == message_aide and reaction.message.author.id == yassbot.user.id:
            await affichage_aide(reaction, auteur_id.author.id, reaction.message)

async def affichage_aide(reaction:discord.reaction.Reaction, id_autheur, message:discord.message.Message):
    if reaction.emoji != "📄" and reaction.emoji != "ℹ️" or reaction.emoji == "❌":
        await reaction.message.channel.send("Je ne suprime rien.")
        return
    try:
        msg = await message.channel.fetch_message(message.id)
    except discord.NotFound:
        return
    supr = True
    for reac in reaction.message.reactions:
        if reac.emoji == "❌":
             async for user in reaction.users():
                 if user.id == id_autheur:
                     supr = False
                     break
    if (supr):
        await reaction.message.delete()
    if (reaction.emoji == "📄"):
        await reaction.message.channel.send("Voici toute les commande d'ont je dispose :\n\n")
        for text in Explication_commande:
            await reaction.message.channel.send(text)
    elif (reaction.emoji == "ℹ️"):
        Presentation_Yassbot: str = str("Salut Je suis " + str(yassbot.user.mention) + " crée pas Yassine / yatsu.\nJe suis crée à des fin pédagogique et jespere que yassine m'ameliora dans le futur et ne moubliera pas ;-;.\nSi tu shouaite voir l'avancement du projet ou des idée de chose que je peux faire je te conseil de jeter un coup d'oeil à sa ;) : https://github.com/yatsuZ/Bot_Discorde")
        await reaction.message.channel.send(Presentation_Yassbot)

message_aide = "## Yo Yasbot va t'aidé!!\nSalut sur quoi a tu besoin d'aide ? \`Selection l'emojie.\` \n-\t 📄 : Je liste toute mes commande.\n-\t ℹ️: Je me presente\n-\t ❌: Si tu n'as plus besoin d'aide, (Le message ne se surpimera pas).\n\nSeul l'auteur de ce message peux choisir. Si l'auteur du message ne choisi rien apres plus de 20 seconde\nou apres avoir choisi ce message s'auto detruira"

@yassbot.command(name="aide")
@commands.guild_only()
async def aide(ctx):
    '''
    Affiche un message d'aide sur le serveur.
    '''
    messgae_auteur: discord.Message = All_Serveurs.get_last_data(ctx.guild.id)
    auteur_id = messgae_auteur.author.id
    message: discord.Message = await ctx.send(message_aide)
    await message.add_reaction("📄")
    await message.add_reaction("ℹ️")
    await message.add_reaction("❌")
    await asyncio.sleep(3)
    try:
        msg = await ctx.channel.fetch_message(message.id)
    except discord.NotFound:
        return
    for reaction in msg.reactions:
        if reaction.emoji == "❌":
            async for user in reaction.users():
                if user.id == auteur_id:
                    print("STOP!!\n\n")
                    await ctx.send("La ❌ a etais selectioner donc pas de supression du message.")
                    return
            break
    await message.delete()

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
            await yassbot.process_commands(message)

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    yassbot.run(TOKENBOT)
else:
    print("Absence de clés.")

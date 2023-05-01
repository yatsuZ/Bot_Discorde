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

message_aide = "Salut sur quoi a tu besoin d'aide ? Appuye sur quoi a besoin tu d'aide \n\t-📄 : Je liste toute mes commande.\n\t-ℹ️: Je me presente\n\t-❌: Si tu n'as plus besoin d'aide.\n\nSeul l'auteur de ce message peux choisir. Si l'auteur du message ne choisi rien apres plus de 20 seconde\nou apres avoir choisi ce message s'auto detruira"

@yassbot.event
async def on_reaction_add(reaction, user):
    historique = All_Serveurs.get_serveur(user.guild.id).historique
    auteur_id: discord.message.Message = historique.get_lastNode().get_data()
    if user.id == auteur_id.author.id and reaction.message.content == message_aide:
        await affichage_aide(reaction, user)

async def affichage_aide(reaction:discord.reaction.Reaction, user:discord.member.Member):
    print("Je renctre dans la fonction")
    if reaction.emoji != "📄" and reaction.emoji != "ℹ️" and reaction.emoji != "❌":
        return
    print(type(reaction))
    print(type(user))
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

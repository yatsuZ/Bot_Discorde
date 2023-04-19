# Installer :
# pip install discord.py (pour utilise le bot discorde)
# pip install nest_asyncio (pour insyncronisé)
# pip install nest_asyncio (pour utilise import les fichier .env)
# documentation du bot discorde: https://discordpy.readthedocs.io/en/stable/

import nest_asyncio
import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

# Permet d'activer le mode asynchrone dans un environnement synchrone.
nest_asyncio.apply()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)
mon_id = 284082499649273856
mon_channel = 1067463854054965338

#######

@client.command(name="wsh")
@commands.guild_only()
async def say_hello(ctx):
    '''
    Si un user envoie : "!wsh".
    alors le bot mementionera et l'auteur de celui qui a envoyer la commande.
    '''
    user = ctx.author
    yatsu = client.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
    await ctx.send("Wsh "+user.mention+".\nJe suis un bot pas encore fini fait par "+ yatsu.mention +".")

@client.command(name="king_krimson")
async def delete(ctx):
    '''
    Si un user envoie : "!king_krimson".
    Alors le bot suprimera les 10 dernier message.
    '''
    async for message in ctx.channel.history(limit=10):
        await message.delete()


@client.event
async def on_ready():
    '''
    Des que le bot sera demarée affichera un message dans le serveur.
    et un autre dans l'un de mes serveurs discordes.
    '''
    print("Le bot est prêt !")
    yatsu = client.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
    channel = client.get_channel(mon_channel)
    await channel.send("Salut je suis Réveillé :) ."+yatsu.mention)

@client.event
async def on_typing(channel, user, when):
    '''
    Quand quelqun est en train decrire et mets plus de 10 seconde.
    Mentione le fais qu'il mets du temp.
    '''
    async for message in channel.history(limit=1): # Récupérer le dernier message du canal
        last_message = message
    await asyncio.sleep(10)
    async for message in channel.history(limit=1): # Récupérer le dernier message du canal
        if last_message == message: # Vérifier si l'auteur est l'utilisateur en question
            await channel.send("Oui " + user.name + " éclaire nous de ta sagesse.") 

@client.event
async def on_member_join(member):
    '''
    Quand quelqun est en train decrire
    le bot le mentione.
    '''
    general_channel = client.get_channel(mon_channel)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    message.content = message.content.lower()

    if message.content.startswith("hello"):
        await message.channel.send("Hello")

    if "cochon" in message.content:
        await message.channel.send("Frero ça va ?")

    if message.content == "azerty":
        await message.channel.send("qwerty")
    
    if message.content == "ping":
        await message.channel.send("pong")

    await client.process_commands(message)

#######

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    client.run(TOKENBOT)
else:
    print("Absence de clés.")

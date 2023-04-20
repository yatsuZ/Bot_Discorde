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

mon_id = 284082499649273856
mes_channel = [1067463854054965338 #underworld -> KK yassine
               , 417775845231427604#La teub -> Bureau pdg
               ]
# Permet d'activer le mode asynchrone dans un environnement synchrone.
nest_asyncio.apply()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents = intents)

## Comment faire pour que le bot puisse interagir avec plusieur serveur en meme temp?
#######

@bot.command(name="wsh")
@commands.guild_only()
async def say_hello(ctx):
    '''
    Si un user envoie : "!wsh".
    alors le bot mementionera et l'auteur de celui qui a envoyer la commande.
    '''
    user = ctx.author
    yatsu = bot.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
    await ctx.send("Wsh "+user.mention+".\nJe suis un bot pas encore fini fait par "+ yatsu.mention +".")

@bot.command(name="king_krimson")
async def delete(ctx):
    '''
    Si un user envoie : "!king_krimson".
    Alors le bot suprimera les 10 dernier message.
    '''
    async for message in ctx.channel.history(limit=10):
        await message.delete()


@bot.event
async def on_ready():
    '''
    Des que le bot sera demarée affichera un message dans le serveur.
    et un autre dans l'un de mes serveurs discordes.
    '''
    print("Le bot est prêt !")
    yatsu = bot.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
    for id_channel in mes_channel:
        channel = bot.get_channel(id_channel)
        await channel.send("Salut je suis Réveillé :) ."+yatsu.mention+
                           "\nJe suis en deploiment yassine essaie de faire des testes sur moi.")

@bot.event
async def on_typing(channel, user, when):
    '''
    Quand quelqun est en train decrire et mets plus de 10 seconde.
    Mentione le fais qu'il mets du temp.
    '''
    async for message in channel.history(limit=1): # Récupérer le dernier message du canal
        last_message = message
    await asyncio.sleep(10) # attend 10 seconde
    async for message in channel.history(limit=1): # Récupérer le dernier message du canal
        if last_message == message: # Vérifier si l'auteur est l'utilisateur en question
            await channel.send("Oui " + user.name + " éclaire nous de ta sagesse.") 

@bot.event
async def on_member_join(member):
    '''
    Quand quelqun est en train decrire
    le bot le mentione.
    '''
    for id_channel in mes_channel:
        channel = bot.get_channel(id_channel)
        await channel.send("Bienvenue sur le serveur ! "+ member.name)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
  
    message.content = message.content.lower()

    print(message.content[0])
    if message.content.startswith("hello"):
        await message.channel.send("Hello")
    if message.content == "ping":
        await message.channel.send("pong")
    if message.content[0] == "!":
        command_name = message.content[1:].split()[0]  # Extrait le nom de la commande à partir du message
        command = bot.get_command(command_name)
        if command:
            await message.channel.send(f"La commande '{command_name}' existe.")
        else:
            await message.channel.send(f"La commande '{command_name}' n'existe pas.")
    await bot.process_commands(message)



@bot.event
async def on_disconnect():
    print("Le bot s'est déconnecté du serveur Discord.")

#######

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    bot.run(TOKENBOT)
else:
    print("Absence de clés.")

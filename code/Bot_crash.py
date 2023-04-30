# Installer :
# pip install discord.py (pour utilise le yassbot discorde)
# pip install nest_asyncio (pour insyncronisé)
# pip install python-dotenv (pour utilise import les fichier .env)
# documentation du yassbot discorde: https://discordpy.readthedocs.io/en/stable/

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

# Permet d'activer le mode asynchrone dans un environnement synchrone.
nest_asyncio.apply()

## Recevoir tout les evenent possible.
intents = discord.Intents.all()

## Initialisation de mon yassbot
# Pour faire un commande il faudra metre un ! au depart
# et gere tout les events.
yassbot = commands.Bot(command_prefix="!", intents = intents)

#######

## Les commandes sont des message commancent par un prefix "!"(defini plus tot)
# Que les user pouront executer.
# qui executera une fonction.
#####
## Les Events sont des evenements -_- je ne peux pas mieux expliquer ahah et du coup
# dans mon code cela executera  

### Command :

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
    ## Faire un code qui affiche un gif de kingkrimson.


## EVENT :

# @yassbot.event
# async def on_ready():
#     '''
#     Des que le yassbot sera demarée affichera un message dans le serveur.
#     et un autre dans l'un de mes serveurs discordes.
#     '''
#     print("Le yassbot est prêt !")
#     yatsu = yassbot.get_user(mon_id) # Obtenir un objet utilisateur en utilisant son ID (c moi)
#     for id_channel in mes_channel:
#         channel = yassbot.get_channel(id_channel)
#         await channel.send("Salut je suis Réveillé :) ."+yatsu.mention+
#                            "\nJe suis en deploiment yassine essaie de faire des testes sur moi.")

# @yassbot.event
# async def on_typing(channel, user, when):
#     '''
#     Quand quelqun est en train decrire et mets plus de 10 seconde.
#     Mentione le fais qu'il mets du temp.
#     '''
#     async for message in channel.history(limit=1): # Récupérer le dernier message du canal
#         last_message = message
#     await asyncio.sleep(10) # attend 10 seconde
#     async for message in channel.history(limit=1): # Récupérer le dernier message du canal
#         if last_message == message: # Vérifier si l'auteur est l'utilisateur en question
#             await channel.send("Oui " + user.name + " éclaire nous de ta sagesse.") 

# @yassbot.event
# async def on_member_join(member):
#     '''
#     Quand quelqun est en train decrire
#     le yassbot le mentione.
#     '''
#     for id_channel in mes_channel:
#         channel = yassbot.get_channel(id_channel)
#         await channel.send("Bienvenue sur le serveur ! "+ member.name)

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

@yassbot.command(name="aide")
@commands.guild_only()
async def aide(ctx):
    '''
    Affiche un message d'aide sur le serveur.
    '''
    await ctx.send("Je dois afficher un message qui explique qui suis je comme bot. et mes commande mais vu que je ne suis pas fini bah jecris rien :).")



## L'event le plus important sa sera comme mon main
@yassbot.event
async def on_message(message):
    '''
    L'event activera la fonction a chaque fois qu'un utilisateur.
    Ecxepter Yassbot.
    '''
    if message.author == yassbot.user:
        return
    serveur = All_Serveurs.get_serveur(message.guild.id)
    if (message.content == "!ajout_serveur"):
        await yassbot.process_commands(message)
        All_Serveurs.get_serveur(message.guild.id).historique.push(message)
        return
    elif (message.content[0] == "!" and All_Serveurs.serveur_existe(message.guild.id)):
            await message.channel.send("Aie je ne connais pas encore ce serveur :(.\nFait la commande !ajout_serveur.\nSi tu veux que je puisse ajouter le serveur : \""+message.guild.name+"\" dans mon repertoire et que tu puisse m'utiliser.")
            return

    message.content = message.content.lower()

    if message.content.startswith("hello"):
        await message.channel.send("Wesh ma guel.")
    if message.content == "ping":
        await message.channel.send("pong")
    

    if message.content[0] == "!":
        command_name = message.content[1:].split()[0]
        command = yassbot.get_command(command_name)
        if command:
            # await message.channel.send(f"La commande '{command_name}' existe.")
            await yassbot.process_commands(message)# Executera la commande du message.
        # else:
        #     await message.channel.send(f"La commande '{command_name}' n'existe pas.") 


#######

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    yassbot.run(TOKENBOT)
else:
    print("Absence de clés.")

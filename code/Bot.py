# Installer :
# pip install discord.py (pour utilise le bot discorde)
# pip install nest_asyncio (pour insyncronisé)
# pip install python-dotenv (pour utilise import les fichier .env)
# documentation du bot discorde: https://discordpy.readthedocs.io/en/stable/

import nest_asyncio 
import discord 
import os
from discord.ext import commands
from dotenv import load_dotenv

# Permet d'activer le mode asynchrone dans un environnement synchrone.
nest_asyncio.apply()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)

#######

@client.command(name="Hello")
@commands.guild_only()
async def say_hello(ctx):
    user = ctx.author
    yatsu = client.get_user(284082499649273856) # Obtenir un objet utilisateur en utilisant son ID
    await ctx.send("Salut "+user.mention+". Je suis un bot pas encore fini fais par "+ yatsu.mention +".")


#######
load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    client.run(TOKENBOT)
else:
    print("Absence de clés.")
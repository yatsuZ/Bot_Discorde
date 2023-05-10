###################################################################################### Import
import os
import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

from All_structure.Node_historique import NodeH, PileH
from All_structure.Serveur import List_Serveur, Serveur_Discorde
import All_commandes
import All_events

###################################################################################### Initial var

All_Serveurs = List_Serveur()

mon_id = 284082499649273856

nest_asyncio.apply()

intents = discord.Intents.all()

yassbot = commands.Bot(command_prefix="!", intents = intents)

timer = 30

###################################################################################### Ajoue des events

All_events.add_all_events(yassbot, mon_id, All_Serveurs)

###################################################################################### Ajoue des commandes

All_commandes.add_all_commandes(yassbot, mon_id, timer, All_Serveurs)

###################################################################################### ACTVIER LE BOT

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    yassbot.run(TOKENBOT)
else:
    print("Absence de clés.")

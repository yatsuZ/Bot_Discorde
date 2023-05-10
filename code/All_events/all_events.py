import All_events
from discord.ext import commands
from All_structure import List_Serveur

def add_all_events(yassbot : commands.Bot, mon_id : int, All_serveurs : List_Serveur):
    """
    Fonction qui ajoute toutes les events
    """

    All_events.add_event_message_suprimer(yassbot)

    All_events.add_event_reaction(yassbot, All_serveurs)

    All_events.add_event_on_message(yassbot, All_serveurs)

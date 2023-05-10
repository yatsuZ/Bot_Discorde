import All_events
from discord.ext import commands
from All_structure import List_Serveur

def add_all_events(yassbot : commands.Bot, mon_id : int, All_serveurs : List_Serveur, description_commandes : str, description_events : str):
    """
    Fonction qui ajoute toutes les events
    """

    description_events = description_events + All_events.add_event_on_message(yassbot, All_serveurs)

    description_events = description_events + All_events.add_event_message_suprimer(yassbot)

    All_events.add_event_reaction(yassbot, All_serveurs, description_commandes, description_events)

import All_commandes
from discord.ext import commands
from All_structure import List_Serveur

def add_all_commandes(yassbot : commands.Bot, mon_id : int, timer : int, All_serveurs : List_Serveur):
    """
    Fonction qui ajoute toutes les commandes
    """

    description_commandes = ""

    description_commandes = description_commandes + All_commandes.add_commande_aide(yassbot, timer, All_serveurs)

    description_commandes = description_commandes + All_commandes.add_commande_wesh(yassbot, mon_id)

    description_commandes = description_commandes + All_commandes.add_commande_markdown(yassbot)

    description_commandes = description_commandes + All_commandes.add_commande_KING_KRIMSON(yassbot)

    description_commandes = description_commandes + All_commandes.add_commande_derniere_commande(yassbot, All_serveurs)

    description_commandes = description_commandes + All_commandes.add_commande_history(yassbot, All_serveurs)

    return description_commandes
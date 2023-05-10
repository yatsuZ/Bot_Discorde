import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from All_structure import List_Serveur

Explication_events = (
    "\n> **on_reaction_add**:\n>\t- Quand quelqu'un lâche une réaction.\n"
    "\n```ansi\n[0;37m1. Si vous faites \"👍\" à l'un de vos propres messages, je le mentionnerai avec sarcasme -_-."
    "\n2. Permet d'interagir avec la commande `!aide` et `!history`.\n```"
)

A_Faire = "```ansi\n" + \
    "- Créer une commande historique qui prendra des paramètres pour historique global ou personnel, et qui pourra aussi supprimer un message de l'historique. Faire en sorte qu'une seule personne à la fois puisse y avoir accès.\n" + \
    "----\n" + \
    "- Faire une conversation d'arbre binaire (pas trop compris, attends Abdel pour le faire).\n" + \
    "----\n" + \
    "- Essayer de créer un système de devinette comme Akinator. Créer un Akinator par serveur. Les utilisateurs pourront le personnaliser au fur et à mesure.\n" + \
    "----\n" + \
    "- Faire la gestion de l'historique de serveur de liste avec des hashtable pour que ce soit plus rapide.\n" + \
    "----\n" + \
    "- Tout sauvegarder en JSON pour que tout soit sauvegardé.\n" + \
    "----\n" + \
    "- Rajouter des trucs.\n" + \
    "----\n" + \
    "- Faire une variable ON/OFF pour chaque événement.\n" + \
    "----\n" + \
    "- Essayer de créer un jeu Loup-Garou, où le bot sera le MJ. Mon bot créera un canal textuel et vocal pour les classes morts et vivants, et il prendra les choix de chaque joueur pour créer la partie.\n" + \
    "----\n" + \
    "- Faire un event chip si 2 ou plusieur utilisateur ecrivve exeactement le meme message a la minute pres alors bot enverra un message et le premier qui ecrirea \"chip\" mutera l'autre pendant 5min ou plus ou si quelqun mention celui qui sera mute.\n" + \
    "```"

###################################################################################### Event Reaction

def add_event_reaction(yassbot : commands.Bot, List_serveur : List_Serveur, Description_commandes, Description_events):
    """
    Le yassbot aura la l'event on_reaction_add
    """

    All_Serveurs = List_serveur

    description_com = "```Voici toute les commande d'ont je dispose :```" + Description_commandes

    description_eve = "```Voici tous les ÉVÉNEMENTS qui sont actifs sur le bot :```" + Explication_events + Description_events

    @yassbot.event
    async def on_reaction_add(reaction:discord.reaction.Reaction, user:discord.member.Member):
        if (user.id == yassbot.user.id):
            return
        if str(reaction.emoji) == "👍": 
            if user.id == reaction.message.author.id:
                await reaction.message.channel.send("L'utilisateur a réagi avec la réaction 👍. A son propre message trop con haha.")
        last_message = All_Serveurs.get_serveur(serveur_id=user.guild.id).historique.get_lastNode()
        if (last_message != None):
            auteur_id = last_message.get_data()
            all_reponse_bot = All_Serveurs.get_serveur(user.guild.id).historique_reponse_BOT
            if user.id == auteur_id.author.id and not (all_reponse_bot.check_unique(reaction.message)) and reaction.message.author.id == yassbot.user.id:
                await affichage_aide(yassbot, reaction, user.id, reaction.message, description_com, description_eve)

async def affichage_aide(yassbot : commands.Bot, reaction:discord.reaction.Reaction, id_autheur, message:discord.message.Message, desc_commande : str, desc_events : str):
    if reaction.emoji == "❌":
        return
    try:
        msg = await message.channel.fetch_message(message.id)
    except discord.NotFound:
        return
    supr = True
    for reac in reaction.message.reactions:
        if reac.emoji == "❌":
             async for user in reac.users():
                 if user.id == id_autheur:
                     supr = False
                     break
    if (reaction.emoji == "📄"):
        await reaction.message.channel.send(desc_commande)
    elif (reaction.emoji == "ℹ️"):
        Presentation_Yassbot: str = "Salut, je suis " + str(yassbot.user.mention) + " créé par Yassine / yatsu.\nJe suis créé à des fins pédagogiques et j'espère que Yassine m'améliorera dans le futur et ne m'oubliera pas ;-;.\nSi tu souhaites voir l'avancement du projet ou des idées de choses que je peux faire, je te conseille de jeter un coup d'œil ici ;) : https://github.com/yatsuZ/Bot_Discorde"
        await reaction.message.channel.send(Presentation_Yassbot)
    elif reaction.emoji == "🪄":
        await reaction.message.channel.send(desc_events)
    elif reaction.emoji == "⚒️":
        await reaction.message.channel.send("Voici tout ce qu'il me reste à faire :\n\n" + A_Faire)
    elif reaction.emoji == "🗑️":
        if (supr == False):
            await reaction.message.channel.send("ECOUTE MOI BIEN FDP TU ME DEMANDE DE FAIRE 2 TRUC CONTRAIDCTOIRE TU VEUX JE TE GOUMME ???.\nOUUUU????\n||Je rigole biens sur desolée davoir etais vulgaire ou offensent c'est une vanne tkt <3.\nDécoche ❌ et 🗑️ puis coche 🗑️.||")
            await reaction.message.channel.send("https://media.giphy.com/media/2Yd8KeTXLDt8Yb8yg2/giphy.gif")
            return
        await reaction.message.delete()

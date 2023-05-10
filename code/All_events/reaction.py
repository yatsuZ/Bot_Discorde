import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from All_structure import List_Serveur

Explication_events = (
    "\n> **on_reaction_add**:\n>\t- Quand quelqu'un ajoute une réaction.\n"
    "\n```ansi\n1. Si vous faites \"👍\" à l'un de vos propres messages, je le mentionnerai avec sarcasme -_-."
    "\n2. Permet d'interagir avec les commandes `!aide` et `!historique`.\n```"
)

A_Faire = (
    "```ansi\n"
    "- Créer une commande historique qui prendra des paramètres pour l'historique global ou personnel, et qui pourra aussi supprimer un message de l'historique. Faire en sorte qu'une seule personne à la fois puisse y avoir accès.\n"
    "----\n"
    "- Faire une conversation d'arbre binaire (pas trop compris, attends Abdel pour le faire).\n"
    "----\n"
    "- Essayer de créer un système de devinette comme Akinator. Créer un Akinator par serveur. Les utilisateurs pourront le personnaliser au fur et à mesure.\n"
    "----\n"
    "- Faire la gestion de l'historique du serveur de liste avec des hashtable pour que ce soit plus rapide.\n"
    "----\n"
    "- Tout sauvegarder en JSON pour que tout soit sauvegardé.\n"
    "----\n"
    "- Rajouter des trucs.\n"
    "----\n"
    "- Faire une variable ON/OFF pour chaque événement.\n"
    "----\n"
    "- Essayer de créer un jeu Loup-Garou, où le bot sera le MJ. Mon bot créera un canal textuel et vocal pour les classes morts et vivants, et il prendra les choix de chaque joueur pour créer la partie.\n"
    "----\n"
    "- Faire un event chip si 2 ou plusieurs utilisateurs écrivent exactement le même message à la minute près, alors le bot enverra un message et le premier qui écrira \"chip\" mutera l'autre pendant 5 minutes ou plus, ou si quelqu'un mentionne celui qui sera muté.\n"
    "```"
)
###################################################################################### Event Reaction

def add_event_reaction(yassbot: commands.Bot, List_serveur: List_Serveur, Description_commandes, Description_events):
    """
    Le yassbot aura l'événement on_reaction_add
    """

    All_Serveurs = List_serveur

    description_com = "```Voici toutes les commandes dont je dispose :```" + Description_commandes

    description_eve = "```Voici tous les ÉVÉNEMENTS qui sont actifs sur le bot :```" + Explication_events + Description_events

    @yassbot.event
    async def on_reaction_add(reaction:discord.reaction.Reaction, user:discord.member.Member):
        if (user.id == yassbot.user.id):
            return
        if str(reaction.emoji) == "👍": 
            if user.id == reaction.message.author.id:
                await reaction.message.channel.send("L'utilisateur a réagi avec la réaction 👍 à son propre message. Quel idiot !")
        last_message = All_Serveurs.get_serveur(serveur_id=user.guild.id).historique.get_lastNode()
        if (last_message != None):
            auteur_id = last_message.get_data()
            all_reponse_bot = All_Serveurs.get_serveur(user.guild.id).historique_reponse_BOT
            if user.id == auteur_id.author.id and not (all_reponse_bot.check_unique(reaction.message)) and reaction.message.author.id == yassbot.user.id:
                await affichage_aide(yassbot, reaction, user.id, reaction.message, description_com, description_eve)
        # tOUTES LES INFO SONT DANS ALL_SERVEUR COMMANDE HISTORIE ;)

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
        Presentation_Yassbot_1 = f"""
```md
# Présentation du bot Yassbot
```
Salut, je suis {yassbot.user.mention}, créé par Yassine / yatsu. :wave:
De base, j'ai été conçu à des fins pédagogiques, MAIS à présent, pas que. J'espère que Yassine continuera à m'améliorer à l'avenir et ne m'oubliera pas ;-;.
En tout cas, il m'a créé avec passion. :sparkles::sparkles:
"""
        Presentation_Yassbot_2 = f"""
Et n'oublie pas, {yassbot.user.mention} est là pour te divertir avec des délires goofy, kawaii, drôles, geek, etc. XD. Mon but est de te divertir et si tu as des besoins spécifiques, n'hésite pas à contacter Yassine :)

Yassine doit sûrement être comme Yoshi, posé, en train d'explorer le monde en quête d'aventure et de méditer, OU NON, en train de charboner sur son PC, hahaha. Bref, voilà ! Chow ! N'hésite pas à refaire la commande `!aide` pour voir tout ce que je peux faire ou ce qui me reste à faire, etc.

Si tu souhaites suivre l'avancement du projet, proposer des idées pour m'améliorer ou obtenir des conseils, je te conseille de jeter un coup d'œil ici :wink: (c'est le repo GitHub du projet) :
https://github.com/yatsuZ/Bot_Discorde
"""

        await reaction.message.channel.send(Presentation_Yassbot_1)
        await reaction.message.channel.send("https://tenor.com/view/yoshi-alone-music-gif-13828164")
        await reaction.message.channel.send(Presentation_Yassbot_2)
        await reaction.message.channel.send("```Le temps que tu lises tout le message d'aide, il a déjà dû s'autodétruire. RUPTURE !!```")
    elif reaction.emoji == "🪄":
        await reaction.message.channel.send(desc_events)
    elif reaction.emoji == "⚒️":
        await reaction.message.channel.send("Voici tout ce qu'il me reste à faire :\n\n" + A_Faire)
    elif reaction.emoji == "🗑️":
        if (supr == False):
            await reaction.message.channel.send("ECOUTE-MOI BIEN FDP, TU ME DEMANDES DE FAIRE 2 TRUCS CONTRADICTOIRES ? TU VEUX QUE JE TE GOMME ???\nOUUUU ????\n||Je rigole bien sûr, désolé d'avoir été vulgaire ou offensant, c'est une vanne, tkt <3.||\nDécoche ❌ et 🗑️ puis coche 🗑️.")
            await reaction.message.channel.send("https://media.giphy.com/media/2Yd8KeTXLDt8Yb8yg2/giphy.gif")
            return
        await reaction.message.delete()

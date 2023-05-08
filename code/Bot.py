###################################################################################### Import
import nest_asyncio
import asyncio
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

from All_structure.Node_historique import NodeH, PileH
from All_structure.Serveur import List_Serveur, Serveur_Discorde

###################################################################################### Initial var

All_Serveurs = List_Serveur()

mon_id = 284082499649273856

nest_asyncio.apply()

intents = discord.Intents.all()

yassbot = commands.Bot(command_prefix="!", intents = intents)

###################################################################################### Texte + Comande Aide
Explication_commande = (
    "> **!aide**:\n>\t- Affiche le répertoire des commandes.\n\n"
    "> **!markdown**:\n>\t- Affiche tous les effets de texte qu'on peut faire sur Discord (liste non exhaustive).\n"
    "> **!wsh**:\n>\t- Le bot vous saluera en vous mentionnant et mentionnera son créateur.\n\n"
    "> **!king_krimson**:\n>\t- Les 10 derniers messages seront supprimés et il affichera un gif de King Crimson.\n>\t(JOJO REF TU CONNAIS.)\n\n"
    "> **!derniere_commande**:\n>\t- Affiche les informations suivantes : l'auteur, le contenu et la date de la dernière commande envoyée dans le serveur, ainsi que le nom du canal.\n\n"
    "> **!history** ***Param***:"
    "\n>\t- Cette commande permet de consulter l'historique des commandes précédentes et offre la possibilité de naviguer dans cet historique. Par exemple, vous pouvez voir l'avant-dernière commande ou la dernière commande. De plus, vous pouvez également supprimer une commande de l'historique. Si un utilisateur est inactif pendant 10 secondes ou s'il supprime une commande, la commande en cours sera terminée et un autre utilisateur pourra l'utiliser. La commande prend également un paramètre :"
    "\n``` -Si le paramètre est vide, l'historique général du serveur sera affiché."
    "\n- Si le paramètre est \"S\", \"Me\" ou \"moi\", l'historique de l'auteur (votre propre historique) sera affiché."
    "\n- Si le paramètre est une mention d'un membre du serveur, l'historique de cet utilisateur sera affiché."
    "\n- Si le paramètre est un canal du serveur, l'historique de ce canal sera affiché.```"
    "\n> `Notez que les paramètres peuvent être combinés. De plus, seul un utilisateur peut utiliser la commande à la fois, car l'utilisateur qui l'exécute a la possibilité de supprimer des commandes de l'historique. Si plusieurs utilisateurs souhaitent utiliser la commande simultanément, une liste d'attente sera mise en place, et chaque utilisateur sera mentionné lorsqu'il pourra utiliser la commande.`"
)

Explication_events = \
    "> **on_message**:\n>\t- Quand quelqu'un envoie un message. ***L'ÉVÉNEMENT LE PLUS IMPORTANT.*** Cela permet de savoir si quelqu'un a envoyé une commande.\n>\tRéagit si quelqu'un envoie :\n"+\
    "\n```python\nQui commence par : \"hello ...\".\nExactement : \"ping\", \"quoicoubaka\"\n```"+\
    "> **on_message_delete**:\n>\t- Quand un message est supprimé. \"**Un message a été supprimé.**\" sera affiché dans le serveur de YassBot.\n"+\
    "> **on_reaction_add**:\n>\t- Quand quelqu'un lâche une réaction.\n"+\
    "\n```ansi\n[0;37m1. Si vous faites \"👍\" à l'un de vos propres messages, je le mentionnerai avec sarcasme -_-.\n" +\
    "2. Permet d'interagir avec la commande `!aide`.\n```"

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
timer = 30

message_aide = "**Yo Yasbot va t'aider !!**\n" + \
    "Salut, sur quoi as-tu besoin d'aide ? Sélectionne l'emoji correspondant.\n" + \
    "\n-\t ℹ️ : Je me présente :```Si tu te demandes qui est Yassbot ?```" + \
    "\n-\t 📄 : Je liste toutes mes commandes.```Si tu te demandes ce que je peux faire ?```" + \
    "\n-\t 🪄 : Je liste tous mes événements.```Si tu te demandes quelles interactions je peux avoir ?```" + \
    "\n-\t ⚒️ : Je liste ce que je pourrais faire.```Si tu te demandes ce qui est en construction ?```" + \
    "\n-\t ❌ : Si tu n'as plus besoin d'aide,```(Le message ne se supprimera pas).```" + \
    "\n-\t 🗑️ : Tu as fini de lire le message d'aide.```Si tu shouaite surpimer le message d'aide.```" + \
    "\n\n***Seul l'auteur de ce message peut choisir et interagir avec ce message***.\n"+\
    "||Apres ***"+str(timer)+"*** secondes ce message se GOGOGADGET-autodétruira :detective:.\n"+\
    "Toi actuellement :||\nhttps://thumbs.gfycat.com/TepidCloudyArmadillo-max-1mb.gif"

emojie_aide = ["ℹ️", "📄", "🪄", "⚒️", "❌", "🗑️"]

emojie_History = ["➡️", "⬅️", "🗑️", "🏁"]

async def affichage_aide(reaction:discord.reaction.Reaction, id_autheur, message:discord.message.Message):
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
        await reaction.message.channel.send("Voici toute les commande d'ont je dispose :\n\n"+Explication_commande)
    elif (reaction.emoji == "ℹ️"):
        Presentation_Yassbot: str = "Salut, je suis " + str(yassbot.user.mention) + " créé par Yassine / yatsu.\nJe suis créé à des fins pédagogiques et j'espère que Yassine m'améliorera dans le futur et ne m'oubliera pas ;-;.\nSi tu souhaites voir l'avancement du projet ou des idées de choses que je peux faire, je te conseille de jeter un coup d'œil ici ;) : https://github.com/yatsuZ/Bot_Discorde"
        await reaction.message.channel.send(Presentation_Yassbot)
    elif reaction.emoji == "🪄":
        await reaction.message.channel.send("Voici tous les ÉVÉNEMENTS qui sont actifs sur le bot :\n\n" + "\n"+Explication_events)
    elif reaction.emoji == "⚒️":
        await reaction.message.channel.send("Voici tout ce qu'il me reste à faire :\n\n" + A_Faire)
    elif reaction.emoji == "🗑️":
        if (supr == False):
            await reaction.message.channel.send("ECOUTE MOI BIEN FDP TU ME DEMANDE DE FAIRE 2 TRUC CONTRAIDCTOIRE TU VEUX JE TE GOUMME ???.\nOUUUU????\n||Je rigole biens sur desolée davoir etais vulgaire ou offensent c'est une vanne tkt <3.\nDécoche ❌ et 🗑️ puis coche 🗑️.||")
            await reaction.message.channel.send("https://media.giphy.com/media/2Yd8KeTXLDt8Yb8yg2/giphy.gif")
            return
        await reaction.message.delete()


@yassbot.command(name="aide")
@commands.guild_only()
async def aide(ctx):
    '''
    Affiche un message d'aide sur le serveur.
    '''
    messgae_auteur: discord.Message = All_Serveurs.get_last_data(ctx.guild.id)
    auteur_id = messgae_auteur.author.id
    message: discord.Message = await ctx.send(message_aide)
    for emojie in emojie_aide:
        await message.add_reaction(emojie)
    await asyncio.sleep(timer)
    try:
        msg = await ctx.channel.fetch_message(message.id)
    except discord.NotFound:
        return
    for reaction in msg.reactions:
        if reaction.emoji == "❌":
            async for user in reaction.users():
                if user.id == auteur_id:
                    await ctx.send("Fin du compte à rebour. l'auteur est activer ❌ le message d'aide ne sera pas suprimer. Sauf si vous apuyer sur 🗑️.")
                    return
            break
    await message.delete()
    await reaction.message.channel.send("https://hellogiggles.com/wp-content/uploads/sites/7/2016/07/10/giphy31.gif")


###################################################################################### texte Markdown + Commande Markdown

Makrdown = (
    "Voici un message de démonstration avec différentes utilisations de Markdown :"
    "\n**Texte en gras**"
    "\n*Texte en italique*"
    "\n***Texte en gras et italique***"
    "\n```python\nTitre Python\n```"
    "\n```markdown\nTitre Markdown\n```"
    "\n```css\nTitre CSS\n```"
    "\n```fix\nTitre fix\n```"
    "\n```xl\nTitre XL\n```"
    "\n```text\nTitre Text\n```"
    "\n```\nBloc de code\n```"
    "\n- Liste à puces item 1"
    "\n- Liste à puces item 2"
    "\n1. Liste numérotée item 1"
    "\n2. Liste numérotée item 2"
    "\n> Citation de texte"
    "\n`Code en ligne`"
    "\n||Texte Cachée||"
    "\n~~Texte Barée~~"
    "\nLien : https://github.com/yatsuZ"
)

@yassbot.command(name="markdown")
@commands.guild_only()
async def show_all_markdown_discorde(ctx):
    '''
    Afficher out les effet de texte possible markdown sous discorde
    '''
    print("Il doit se passer quelque chose")
    await ctx.send("test")
    await ctx.send(Makrdown)

###################################################################################### Commande wsh

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

###################################################################################### Commande King Krimson

@yassbot.command(name="king_krimson")
async def delete(ctx):
    '''
    Si un user envoie : "!king_krimson".
    Alors le yassbot suprimera les 10 dernier message.
    et affiche un gif de king_krimson.
    '''
    async for message in ctx.channel.history(limit=10):
        await message.delete()
        await asyncio.sleep(0.5)
        
    if (bool(random.getrandbits(1))):
        gif_king_krimson = "https://media.tenor.com/lNzPjBeAeB8AAAAd/king-crimson-cartoon.gif"
    else:
        gif_king_krimson = "https://media.tenor.com/vUdvSJpdQq8AAAAd/king-crimson.gif"
    await ctx.send("`Lorsque le Stand arrête d'effacer le temps, les victimes ne se souviennent plus de ce qui s'est passé.`\n")
    await ctx.send(gif_king_krimson)

###################################################################################### Event Suppression de message

@yassbot.event
async def on_message_delete(message):
    pass
    # print("Un message a été supprimé.")
    # print(f"Contenu du message : {message.content}")

###################################################################################### Event Reaction

@yassbot.event
async def on_reaction_add(reaction:discord.reaction.Reaction, user:discord.member.Member):
    if (user.id == yassbot.user.id):
        return
    if str(reaction.emoji) == "👍": 
        if user.id == reaction.message.author.id:
            await reaction.message.channel.send("L'utilisateur a réagi avec la réaction 👍. A son propre message trop con haha.")
    last_message = All_Serveurs.get_serveur(user.guild.id).historique.get_lastNode()
    if (last_message != None):
        auteur_id = last_message.get_data()
        if user.id == auteur_id.author.id and reaction.message.content == message_aide and reaction.message.author.id == yassbot.user.id:
            await affichage_aide(reaction, user.id, reaction.message)

###################################################################################### Commande derniere _commande

def get_hisotiry_commande_data(message : discord.Message) -> str :
    if (message == None):
        return ("Aucune commande n'as encore etais envoyer.")
    serveur = message.guild
    channel = message.channel
    author = message.author
    anne = message.created_at.strftime("%Y")
    mois = message.created_at.strftime("%m")
    jour = message.created_at.strftime("%d")
    heur = message.created_at.strftime("%H")
    minute = message.created_at.strftime("%M")
    contenu = message.content
    message = "```ansi\n"+\
        "\n\t[0;37m Par                         : [0;35m" + str(author)+\
        "\n\t[0;37m Contenu                     : [0;33m" + contenu +\
        "\n\t[0;37m Dans le channelle           : \"[0;32m" + str(channel) +"[0;37m\""\
        "\n\t[0;37m Dans le serveur             : \"[0;31m" + str(serveur) +"[0;37m\""\
        "\n\t[0;37m Envoyer le [0;36m" + jour + "/"+ mois + "/" + anne + " à "+heur+"H"+minute+\
        "```"
    return message

@yassbot.command(name="derniere_commande")
@commands.guild_only()
async def derniere_commande(ctx):
    '''
    Affiche la dernière commande avec les informations.
    '''
    dernier_message = All_Serveurs.get_last_previous_data(ctx.guild.id)
    message = get_hisotiry_commande_data(dernier_message)
    if (dernier_message == None):
        await ctx.send(message)
        return
    await ctx.send("Voici les informations de l'avant dernière commande...\nVus que la derniere comande c'est celle que vous venez de rentrez ... enfin bref voila:"+message)

###################################################################################### COMMAND HISTORY

@yassbot.command(name="history")
@commands.guild_only()
async def History(ctx, *args):
    '''
        Fait la commande History
    '''
    List_role = []
    List_user = []
    List_channelle = []
    Argument_non_valide = ""
    await ctx.send("Legende navigation history```➡️ : Message précedent.\n⬅️ : Message suivant\n🗑️ : Suprimer cette commande de l'historiqque\n🏁: en avoir fini avec la commande```")
    if len(args) == 0:
        List_role = None
        List_user = None
        List_channelle = None
        print("Pas d'argument")
    else:
        for arg in args:
            if arg.startswith('<@&') and arg.endswith('>'):  # Vérifie si c'est une mention de rôle
                role_id = int(arg[3:-1])
                role : discord.role.Role = discord.utils.get(ctx.guild.roles, id=role_id)
                if role:
                    List_role.append(role)
            elif arg.startswith('<@') and arg.endswith('>'):  # Vérifie si c'est une mention utilisateur
                user_id = int(arg[2:-1])
                user : discord.user.User = discord.utils.get(ctx.guild.members, id=user_id)
                if user:
                    List_user.append(user)
            elif arg.startswith('<#') and arg.endswith('>'):  # Vérifie si c'est une mention de canal
                channel_id = int(arg[2:-1])
                channel : discord.channel.TextChannel = discord.utils.get(ctx.guild.channels, id=channel_id)
                if channel:
                    List_channelle.append(channel)
            else:
                if (Argument_non_valide == ""):
                    Argument_non_valide = arg
                else :
                    Argument_non_valide = Argument_non_valide + ", " + arg

        # Convertir les listes en chaînes de caractères
        if (len(List_role) == 0):
            List_role = None
            str_list_role = "Aucun role."
        else:
            str_list_role = ", ".join([str(role.name) for role in List_role])
        if (len(List_user) == 0):
            List_user = None
            str_list_user = "Tout les users"
        else :
            str_list_user = ", ".join([str(user.name) for user in List_user])
        if (len(List_channelle) == 0):
            List_channelle = None
            str_list_channel = "en absence de parametre sa sera sur le channelle present " + ctx.channel.name
        else:
            str_list_channel = ", ".join([str(channel.name) for channel in List_channelle])
        if (Argument_non_valide == ""):
            Argument_non_valide = "GG tu as mis 0 argument non valide."

        # Envoyer les listes converties en chaînes de caractères
        # await ctx.send("Voici les paramètres que tu as mis. `Tu auras l'historique des commande qui auront tout sa comme parametre` \nListe d'utilisateurs :\n\t" + str_list_user + "\nListe de rôles :\n\t" + str_list_role + "\nListe de canaux :\n\t" + str_list_channel + "\nMais frero sa c'est pas des arguments valide tu voulais faire quoi :\n\t" + Argument_non_valide)
    print(List_user == None, List_user, List_channelle, List_role)
    await All_Serveurs.Commande_History_init(ctx.guild.id, ctx.author, ctx.channel, List_user, List_channelle, List_role)## Fera tout seul l'affichage

###################################################################################### EVENT Message

@yassbot.event
async def on_message(message):
    '''
    L'event activera la fonction a chaque fois qu'un utilisateur.
    Ecxepter Yassbot.
    '''
    if message.author == yassbot.user:
        return

    serveur = All_Serveurs.get_serveur(message.guild.id)
    if (serveur == None):
        All_Serveurs.add_serveur(message.guild.id)
        serveur = All_Serveurs.get_serveur(message.guild.id)
    message.content = message.content.lower()

    if message.content.startswith("hello"):
        await message.channel.send("Wesh ma guel.")
    if message.content == "ping":
        await message.channel.send("pong")
    if message.content == "quoicoubaka":
        await message.channel.send("https://media.tenor.com/GOYRQva4UeoAAAAd/anime-dance.gif")
    if (message.content == None or message.content == ""):
        return
    if message.content[0] == "!":
        command_name = message.content[1:].split()[0]
        command = yassbot.get_command(command_name)
        if command:
            serveur.historique.push(message)
            await yassbot.process_commands(message)

###################################################################################### ACTVIER LE BOT

load_dotenv()
TOKENBOT = os.getenv('tokenBot')  # récupérer la valeur de votre token
if (TOKENBOT):
    yassbot.run(TOKENBOT)
else:
    print("Absence de clés.")

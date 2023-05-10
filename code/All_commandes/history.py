import nest_asyncio
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from All_structure import List_Serveur

###################################################################################### COMMAND HISTORY

def add_commande_history(yassbot : commands.Bot, List_serv : List_Serveur):
    """
    Le yassbot aura la commande history
    """

    All_Serveurs = List_serv

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
        await All_Serveurs.Commande_History_init(ctx.guild.id, ctx.author, ctx.channel, List_user, List_channelle, List_role)## Fera tout seul l'affichage

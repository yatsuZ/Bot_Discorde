from discord.ext import commands
from dotenv import load_dotenv

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
def add_commande_markdown(yassbot : commands.Bot) -> str:
    """
    Le yassbot aura la commande markdown.
    return la description de la commande
    """
    @yassbot.command(name="markdown")
    @commands.guild_only()
    async def show_all_markdown_discorde(ctx):
        '''
        Afficher out les effet de texte possible markdown sous discorde
        '''
        print("Il doit se passer quelque chose")
        await ctx.send("test")
        await ctx.send(Makrdown)
    return Desciption

Desciption = "\n> **!markdown**:\n>\t- Affiche tous les effets de texte qu'on peut faire sur Discord (liste non exhaustive).\n"
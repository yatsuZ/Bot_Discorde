import asyncio
import random
from discord.ext import commands

###################################################################################### Commande King Krimson

def add_commande_KING_KRIMSON(yassbot : commands.Bot):
    """
    Le yassbot aura la commande king_krimson
    """

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
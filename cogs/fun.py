from ast import alias
import nextcord
from nextcord.ext import commands
from nextcord import Color
import random
import aiohttp


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colors = {}
    @commands.command(aliases=['kostka'])
    async def dice(self, ctx, min:int=1, max:int=6):
        if not min > max:
            embed = nextcord.Embed(title='Dice', description = f'Dice says: {random.randint(min, max)}',color=Color.blurple())
            await ctx.reply(embed=embed)
        else:
            embed = nextcord.Embed(title='Dice', description = f'Dice says: {random.randint(max, min)}',color=Color.blurple())
            await ctx.reply(embed=embed)
    
    @commands.command(aliases=['powiedz', 'mów'])
    async def say(self, ctx, *, msg):
        command = ctx.message
        await command.delete()
        await ctx.send(msg)
    """
    @commands.command(aliases=['ciekawostka'])
    async def funfact(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.aakhilv.me/fun/facts') as r:
                resp = await r.json()
                embed = nextcord.Embed(title = 'Fun Fact!', description = resp[0], color=Color.blurple())
                await ctx.reply(embed=embed)
    @commands.command()
    async def wyr(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.aakhilv.me/fun/wyr') as r:
                resp = await r.json()
                embed = nextcord.Embed(title = 'What would you prefer?', description = resp[0], color=Color.blurple())
                await ctx.reply(embed=embed)
    @commands.command(aliases=['definicja'])
    async def term(self, ctx):
        async with aiohttp.ClientSession() as session:  
            async with session.get('https://api.aakhilv.me/bio/terms') as r:
                resp = await r.json()
                embed = nextcord.Embed(title = 'Term: ' + resp[0]['term'], description = resp[0]['definition'], color=Color.blurple())
                await ctx.reply(embed=embed)
    """


def setup(bot):
    bot.add_cog(Fun(bot))

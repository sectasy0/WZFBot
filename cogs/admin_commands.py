from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE
import nextcord
from nextcord.ext import commands
from nextcord import Color


class OwnerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user:nextcord.User, reason='No reason'):
        await ctx.guild.kick(user, reason=reason)
        embed = nextcord.Embed(title='Kicked!', description=f'User {user.name} has been kicked!', color=Color.blurple())
        await ctx.reply(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user:nextcord.User, reason='No reason'):
        await ctx.guild.ban(user, reason=reason)
        embed = nextcord.Embed(title='Banned!', description=f'User {user.name} has been banned!', color=Color.blurple())
        await ctx.reply(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def add_text_channel(self, ctx, name:str):
        await ctx.guild.create_text_channel(name)
        embed = nextcord.Embed(title=f'Text channel {name} added!', color=Color.blurple())
        await ctx.reply(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def add_voice_channel(self, ctx, name:str):
        await ctx.guild.create_voice_channel(name)
        embed = nextcord.Embed(title=f'Voice channel {name} added!', color=Color.blurple())
        await ctx.reply(embed=embed)
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pins(self, ctx, index='all'):
        if index == 'all':
            for pin in await ctx.channel.pins():
                await ctx.send('> '+pin.content + '\nSent by: ' + pin.author.name)
        else:
            _pin = await ctx.channel.pins()[int(index)]
            await ctx.send('> '+_pin.content + '\nSent by: ' + await _pin.author.name)
    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        embed = nextcord.Embed(title=f'Servers that im in:', color=Color.blurple())
        embed.set_footer(text=f'Total: {len(self.bot.guilds)}')
        for guild in self.bot.guilds:
            embed.add_field(name=f'{guild.name}', value=f'{guild.owner.name}', inline=False)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(OwnerCommands(bot))

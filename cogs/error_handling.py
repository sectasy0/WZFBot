import nextcord
from nextcord.ext import commands
from nextcord import Color


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        match type(error):
            case commands.CommandNotFound:
               await ctx.message.add_reaction('❌')
            case commands.MissingRequiredArgument:
                embed = nextcord.Embed(title='❌',description='Missing argument(s)', color=Color.red())
                await ctx.reply(embed=embed)
            case commands.MissingPermissions:
                embed = nextcord.Embed(title='❌',description='You don\'t have permission to do this!', color=Color.red())
                await ctx.reply(embed=embed)
            case commands.BadArgument:
                embed = nextcord.Embed(title='❌',description='Bad argument type!', color=Color.red())
                await ctx.reply(embed=embed)
            case commands.ExtensionNotLoaded:
                embed = nextcord.Embed(title='❌',description='Cog does not appear to be loaded!', color=Color.red())
                await ctx.reply(embed=embed)
            case commands.UserNotFound:
                embed = nextcord.Embed(title='❌',description='User wasn\'t found!', color=Color.red())
                await ctx.reply(embed=embed)
            case _:
                embed = nextcord.Embed(title='❌',description=f'**{type(error).__name__}** Error: {error}', color=Color.red())
                await ctx.reply(embed=embed)
                raise error
                

def setup(bot):
    bot.add_cog(ErrorHandler(bot))

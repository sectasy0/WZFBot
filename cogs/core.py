import nextcord
from nextcord.ext import commands
from nextcord import Color
import time


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pomoc', 'help'])
    async def _help(self, ctx):
        embed = nextcord.Embed(
            title='Help', description='Commands:', color=Color.blurple())
        embed.add_field(name='$help', value='Displays this message')
        embed.add_field(name='$dice (min) (max)', value='Just dice!')
        embed.add_field(name='$say *(phrase)', value='Says choosen phrase(s)')
        embed.add_field(name='COMMAND DELETED (api does not work) $funfact', value='Shows random funfact')
        embed.add_field(
            name='COMMAND DELETED (api does not work) $wyr', value='Shows random "would you rather" question')
        embed.add_field(name='COMMAND DELETED (api does not work) $term', value='Sends definition of random term')
        embed.add_field(name='$avatar [user]', value='Sends user avatar')
        embed.add_field(name='$user [user]', value='Sends info about user')
        embed.add_field(name='$term', value='Sends definition of random term')
        embed.add_field(name='$poll *(reactions separated by "," with no spaces)', value='Adds reactions to message')
        await ctx.author.send(embed=embed)
        info = nextcord.Embed(
            title='I just sent you help message to our DM\'s!', color=Color.blurple())
        await ctx.reply(embed=info)

    @commands.command()
    async def avatar(self, ctx, user: nextcord.User = None):
        if user == None:
            user = ctx.author
        embed = nextcord.Embed(color=Color.blurple())
        embed.set_image(url=user.avatar.url)
        await ctx.reply(embed=embed)

    @commands.command()
    async def user(self, ctx, user: nextcord.Member = None):
        if user == None:
            user = ctx.author
        embed = nextcord.Embed(title=f'User {user.name}', color=Color.blurple())\
            .add_field(name='Created:', value=f"<t:{int(time.mktime(user.created_at.timetuple()))}>")\
            .add_field(name='Joined:', value=f"<t:{int(time.mktime(user.joined_at.timetuple()))}>")
        await ctx.reply(embed=embed)

    @commands.command()
    async def poll(self, ctx, reactions):
        for reaction in reactions.split(','):
            await ctx.message.add_reaction(reaction)
def setup(bot):
    bot.add_cog(Core(bot))

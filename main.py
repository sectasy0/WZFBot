import nextcord
from nextcord.ext import commands
import os
import sys
intents = nextcord.Intents.all()


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_cogs()

    async def on_ready(self):
        print("Bot is now ready!")
        await self.change_presence(activity=nextcord.Streaming(name='$help', url='https://www.youtube.com/watch?v=xvFZjo5PgG0'))

    def load_cogs(self):
        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                self.load_extension(f'cogs.{file[:-3]}')


bot = Bot(command_prefix='$', case_insensitive=True, intents=intents, help_command=None)


@bot.command()
@commands.is_owner()
async def reload_cogs(ctx, cog: str = 'all'):
    if cog == 'all':
        for file in os.listdir('cogs'):
            if file.endswith('.py'):
                bot.unload_extension(f'cogs.{file[:-3]}')
                bot.load_extension(f'cogs.{file[:-3]}')
                await ctx.send(f'Cog **cogs.{file[:-3]}** reloaded!')
    else:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await ctx.send(f'Cog **{cog}** reloaded!')

bot.run(input("Enter Bot token: "))

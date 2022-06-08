import nextcord
from nextcord.ext import commands
import os
import sys

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix = '$', case_insensitive = True, intents = intents)
bot.remove_command('help')


for file in os.listdir('cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Streaming(name='$help', url='https://www.youtube.com/watch?v=xvFZjo5PgG0'))
@bot.command()
@commands.is_owner()
async def reload_cogs(ctx, cog:str='all'):
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

if len(sys.argv) < 2:
    print('Argument (token) missing.')
else:
    bot.run(sys.argv[1])

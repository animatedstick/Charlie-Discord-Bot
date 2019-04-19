import discord
import asyncio
from discord.ext import commands
from discord.utils import get
import os

bot = discord.Client()
bot_prefix= "c!"
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")


#startup_extensions = [
#   'cogs.info',
#    'cogs.mod'
#]


@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Users: {}".format(len(set(bot.get_all_members()))))
    await bot.change_presence(game=discord.Game(name="c!help | {} Users ".format(len(set(bot.get_all_members()))),type=3))



bot.run(os.getenv("BOT_TOKEN"))

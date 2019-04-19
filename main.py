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


@bot.event
async def on_message(message):
        if message.author.bot:
            return

        elif message.content.startswith("c!say"):
            if message.author.id == "429118689367949322":
                text = message.content[len('<tell'):].strip()
                if "efnejifn" in text:
                    return
                elif "discord." in text:
                    return
                elif "@here" in text:
                    return
                elif "@everyone" in text:
                    return
                else:
                    await bot.send_message(message.channel ,"{}".format(text))
                    await bot.delete_message(message)
            else:
                return



bot.run(os.getenv("BOT_TOKEN"))

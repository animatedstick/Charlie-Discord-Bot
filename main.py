import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import random
import time
import datetime
import io
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

        elif message.content.startswith ("<8ball"):
            await bot.send_message(message.channel, random.choice([":8ball: | **{},** It is Certain ".format(message.author.name),
                                                                  ":8ball: | **{},** It is Decidedly, So ?".format(message.author.name),
                                                                  ":8ball: | **{},** Without a doubt ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes, definitely  ".format(message.author.name),
                                                                  ":8ball: | **{},** You may rely on it ".format(message.author.name),
                                                                  ":8ball: | **{},** As I see it, yes  ".format(message.author.name),
                                                                  ":8ball: | **{},** Most likely  ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook Looks Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Yes Bro ".format(message.author.name),
                                                                  ":8ball: | **{},** Signs point to yes ".format(message.author.name),
                                                                  ":8ball: | **{},** Reply lazy try again ".format(message.author.name),
                                                                  ":8ball: | **{},** Ask again later ".format(message.author.name),
                                                                  ":8ball: | **{},** Better not tell you now ".format(message.author.name),
                                                                  ":8ball: | **{},** Cannot predict now ".format(message.author.name),
                                                                  ":8ball: | **{},** Concentrate and ask again ".format(message.author.name),
                                                                  ":8ball: | **{},** Don't count on it  ".format(message.author.name),
                                                                  ":8ball: | **{},** My reply is no ".format(message.author.name),
                                                                  ":8ball: | **{},** My sources say no ".format(message.author.name),
                                                                  ":8ball: | **{},** Outlook is Not So Good  ".format(message.author.name),
                                                                  ":8ball: | **{},** Very doubtful  ".format(message.author.name)]))

        elif message.content.startswith("t!say"):
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

import discord
from discord.ext import commands
import sys, traceback
import datetime
import time
import asyncio
import os 

bot = discord.Client()
prefix = 'c!' , 'C!' ,'charlie ','c' , '<@568492275504775178> ' 
bot = commands.Bot(command_prefix=prefix, description='A Discord Bot By the AnimatedStick#4797')
bot.remove_command("help")

minutes = 0
hour = 0
days = 0
use = 0


initial_extensions = ['cogs.mod',
                      'cogs.owner',
                      'cogs.fun',
                      'cogs.info',
                      'cogs.events',
                      'cogs.tanki',
                      'cogs.help',
                      'cogs.events']
                      

async def status_task():
    while True:
       await bot.change_presence(activity=discord.Game(name="c!help | {:,} Users ".format(len(set(bot.get_all_members()))), type=3))
       await asyncio.sleep(10)
       await bot.change_presence(activity=discord.Game(name="c!help | {:,} Servers".format(len(bot.guilds)), type=3))
       await asyncio.sleep(10)
       await bot.change_presence(activity=discord.Game(name="c!help | Join Our Discord!".format(len(set(bot.get_all_members())))))
       await asyncio.sleep(10)


@bot.event
async def on_command(command):
    global use
    use +=1

@bot.event
async def on_ready():
    print("Name: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Users: {}".format(len(set(bot.get_all_members()))))
    bot.loop.create_task(status_task())
    #await client.change_presence(status=discord.Status.idle, activity=game)
    #await bot.change_presence(activity=discord.Game(name="c!help | {} Users ".format(len(set(bot.get_all_members()))), type=1, url='https://www.twitch.tv/animatedstick'))

@bot.command()
async def bug(ctx,*,bug:str):
    if bug == None:
        await ctx.author.send('Please Mention the Bug `c!bug [bug]`')
    
    else:
       await ctx.message.delete()
       chan = bot.get_channel(572760775530119180)
       embed=discord.Embed()
       embed.add_field(name="Bug Report!!", value=f"**User :** {ctx.author}\n**Server :** {ctx.guild.name}\n**Bug :** {bug}", inline=True)
       embed.timestamp = datetime.datetime.utcnow()
       await chan.send(embed=embed)

@bot.command()
async def suggest(ctx,*,sug:str):
    if sug == None:
        await ctx.author.send('Please Mention a Suggestion `c!suggest [suggestion]`')
    
    else:
        await ctx.message.delete()
        chan = bot.get_channel(572761324359122951)
        embed=discord.Embed()
        embed.add_field(name="Suggestion!", value=f"**User :** {ctx.author}\n**Server :** {ctx.guild.name}\n**Suggestion :** {sug}", inline=True)
        embed.timestamp = datetime.datetime.utcnow()
        await chan.send(embed=embed)

@bot.command()
async def usages(ctx):
    embed=discord.Embed()
    embed.add_field(name="Usages :wrench:", value=f"**{use}** Commands Have Been Used After The Bot Restart!", inline=True)
    await ctx.send(embed=embed)
# verify 560383768372838400
 #loadiungh 568851263140265992 
@bot.command()
async def ping(ctx):
    loading = bot.get_emoji(568851263140265992)
    done = bot.get_emoji(560383768372838400)
    start = time.perf_counter()
    e = discord.Embed(title="Pinging!", description="Aquiring Response From the Servers! {}".format(loading))
    message = await ctx.send(embed=e)
    end = time.perf_counter()
    duration = (end - start) * 1000
    await asyncio.sleep(1)
    e = discord.Embed(title="Complete!", description='Pong! {:.2f}ms {}'.format(duration , done))
    await message.edit(embed=e)

@bot.command(pass_context=True)
async def uptime(ctx):
    embed=discord.Embed()
    embed.add_field(name="Uptime:", value="Been Online For **|** **{0}** Day(s) **{1}** Hour(s) and **{2}** Minute(s) !".format(days , hour , minutes), inline=True)
    await ctx.send(embed=embed)



@bot.event
async def on_command_error(ctx,error):
    try:
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            user = ctx.message.author
            embed=discord.Embed(title="Support Server Link", url="https://discord.gg/DyPu726", description="```\n{}\n```".format(error))
            embed.set_author(name="The Following Error Ocurred ", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="Charlie Discord Bot" ,icon_url=bot.user.avatar_url)
            await user.send(embed=embed)
            await user.send('Support Server Link: https://discord.gg/xutQNJB')
       
    except:
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            embed=discord.Embed(title="Support Server Link", url="https://discord.gg/DyPu726", description="```py{}```".format(error))
            embed.set_author(name="The Following Error Ocurred ", icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="Charlie Discord Bot" ,icon_url=bot.user.avatar_url)
            await ctx.send(embed=embed)
            await ctx.send('Support Server Link: https://discord.gg/xutQNJB')


async def charlie_uptime():
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    global days
    days = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if hour == 24:
            minutes = 0
            hour = 0
            days +=1
bot.loop.create_task(charlie_uptime())


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()




bot.run(os.getenv("BOT_TOKEN"), bot=True, reconnect=True)

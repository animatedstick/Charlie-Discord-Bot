import discord
from discord.ext import commands
import sys, traceback
import datetime
import time
import asyncio
import os

bot = discord.Client()
prefix = 'c!' , 'C!' ,'charlie ','c' , '<@568492275504775178> ' , 'C'
bot = commands.Bot(command_prefix=prefix, description='A Discord Bot By the AnimatedStick#4797')
bot.remove_command("help")


use = 0
start_time = datetime.datetime.now()


initial_extensions = ['cogs.mod',
                      'cogs.owner',
                      'cogs.fun',
                      'cogs.info',
                      'cogs.calc',
                      'cogs.tanki',
                      'cogs.help',
                      'cogs.fort']
                      

async def status_task():
    while True:
       await bot.change_presence(activity=discord.Game(name="c!help | {:,} Users ".format(len(set(bot.get_all_members()))), type=3))
       await asyncio.sleep(10)
       await bot.change_presence(activity=discord.Game(name="c!help | {:,} Servers".format(len(bot.guilds)), type=3))
       await asyncio.sleep(10)
       await bot.change_presence(activity=discord.Game(name="c!help | Join Our Discord!" ,type=3))
       await asyncio.sleep(10)

def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '**{0}** Days, **{1}** Hours, **{2}** Minute and **{3}** Second.'.format(days,hours,minutes,sec)
    elif minutes > 1 and sec == 1:
        return '**{0}** Days, **{1}** Hours, **{2}** Minutes and **{3}** Second.'.format(days,hours,minutes,sec)
    elif minutes == 1 and sec > 1:
        return '**{0}** Days, **{1}** Hours, **{2}** Minute and **{3}** Seconds.'.format(days,hours,minutes,sec)
    else:
        return '**{0}** Days, **{1}** Hours, **{2}** Minutes and **{3}** Seconds.'.format(days,hours,minutes,sec)

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
       chan = bot.get_channel(572760775530119180)
       embed=discord.Embed()
       embed.add_field(name="Bug Report!!", value=f"**User :** {ctx.author}\n**Server :** {ctx.guild.name}\n**Bug :** {bug}", inline=True)
       embed.set_thumbnail(url=str(ctx.author.avatar_url))
       embed.timestamp = datetime.datetime.utcnow()
       await chan.send(embed=embed)
       await ctx.message.delete()
       await ctx.send(f':tada: Your Bug Report Was Sucessfully Sent! , {ctx.author.mention}')

@bot.command()
async def suggestion(ctx,*,sug:str):
    if sug == None:
        await ctx.author.send('Please Mention a Suggestion `c!suggest [suggestion]`')
    
    else:
        chan = bot.get_channel(572761324359122951)
        embed=discord.Embed()
        embed.add_field(name="Suggestion!", value=f"**User :** {ctx.author}\n**Server :** {ctx.guild.name}\n**Suggestion :** {sug}", inline=True)
        embed.set_thumbnail(url=str(ctx.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await chan.send(embed=embed)
        await ctx.message.delete()
        await ctx.send(f':tada: Your Suggestion Was Sucessfully Sent! , {ctx.author.mention}')

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

@bot.command()
async def uptime(ctx):
    """Displays bot uptime."""
    global start_time
    embed=discord.Embed()
    embed.add_field(name="Uptime", value=timedelta_str(datetime.datetime.now() - start_time), inline=False)
    embed.set_thumbnail(url=str(bot.user.avatar_url))
    embed.timestamp = datetime.datetime.utcnow()
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

@bot.event
async def on_guild_join(guild):
    join = bot.get_channel(572773776039739452)
    embed=discord.Embed(title="New Server!!")
    embed.set_thumbnail(url=str(guild.icon_url))
    embed.add_field(name='Server Name', value=guild.name, inline=True)
    embed.add_field(name='Server ID', value=guild.id, inline=True)
    embed.add_field(name='Server Owner', value=guild.owner, inline=True)
    embed.add_field(name='Server Owner ID', value=guild.owner.id, inline=True)
    embed.add_field(name='Server Members', value=len(guild.members), inline=True)
    await join.send(embed=embed)

@bot.event
async def on_member_join(member):
    server = member.guild
    if server.id == 554641659888140308:
        wlc = bot.get_channel(557774869719416844)
        embed=discord.Embed(title="Welcome to the Crew!", url="https://discord.gg/9SVUNya", description=f"Welcome to the the AnimatedStick Crew Discord Server,\n {member.name} :wave:\n\nMake sure to check out the AnimatedStick YouTube Channel\nSubscribe & Support : [Channel Link](https://www.youtube.com/channel/UC0bZpIWLn_YEjkyTyvAadtQ?view_as=subscriber)\n`Have Great Time At the AnimatedStick Server`", color=0xfbb420)
        embed.set_author(name=member.name, icon_url=str(member.avatar_url))
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"the AnimatedStick Crew | Welcome {member.name}!",icon_url=str(server.icon_url))
        await wlc.send(embed=embed)

    elif server.id == 572346295830970370:
        wlc = bot.get_channel(572761367933747200)
        embed=discord.Embed(title="Charlie Support Server!!", url="https://discord.gg/9SVUNya", description=f"Welcome to the Charlie Support Server,\n {member.name} :wave:\n\nMake sure to vote Charlie at the Discord Bot List\nVote & Support : [Link](https://www.youtube.com/channel/UC0bZpIWLn_YEjkyTyvAadtQ?view_as=subscriber)\n`Have Great Time At the Charlie Support Server`", color=0xfe8601)
        embed.set_author(name=member.name, icon_url=str(member.avatar_url))
        embed.set_thumbnail(url=str(member.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"Charlie Support Server | Welcome {member.name}!",icon_url=str(server.icon_url))
        await wlc.send(embed=embed)
        wembed=discord.Embed(title="Welcome To The Support Server ", url="https://discordapp.com/oauth2/authorize?client_id=568492275504775178&scope=bot&permissions=8", description="\n\n\n Hey There {user},\nThanks You For Joining Our Support Server!\nMake Sure to Vote & Share Our Bot to Others :wink:\n\n:link: **Invite Link:** [Link](https://discordapp.com/oauth2/authorize?client_id=568492275504775178&scope=bot&permissions=8)\n**Discord Bot List Vote:** [Link](https://discordbots.org/bot/568492275504775178\n\nThanks For Using Our Bot! Have a Nice Day! :tada:    ", color=0xfa9205)
        wembed.set_author(name="Charlie", icon_url=str(bot.user.avatar_url))
        wembed.timestamp = datetime.datetime.utcnow()
        wembed.set_footer(text=f"{member}",icon_url=str(member.avatar_url))
        await member.send(wembed=embed)
    else:
        return

@bot.event
async def on_guild_remove(guild):
    join = bot.get_channel(572773776039739452)
    embed=discord.Embed(title="Server Gone!!")
    embed.set_thumbnail(url=str(guild.icon_url))
    embed.add_field(name='Server Name', value=guild.name, inline=True)
    embed.add_field(name='Server ID', value=guild.id, inline=True)
    embed.add_field(name='Server Owner', value=guild.owner, inline=True)
    embed.add_field(name='Server Owner ID', value=guild.owner.id, inline=True)
    embed.add_field(name='Server Members', value=len(guild.members), inline=True)
    embed.add_field(name='Server Members', value=len(guild.members), inline=True)
    await join.send(embed=embed)





if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()



bot.run(os.getenv("BOT_TOKEN"), bot=True, reconnect=True)

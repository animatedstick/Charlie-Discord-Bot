import discord
from discord.ext import commands
import random 
import datetime
import time
import aiohttp
import asyncio

class Fun(commands.Cog, name='Fun'):
    def __init__(self,bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
    
    def __embed_json(self, data, key="message"):
        em = discord.Embed(color=0xfe8601)
        em.set_image(url=data[key])
        return em   
    
    async def __get_image(self, ctx, user=None):
        if user:
            if user.is_avatar_animated():
                return str(user.avatar_url_as(format="gif"))
            else:
                return str(user.avatar_url_as(format="png"))

        await ctx.trigger_typing()

        message = ctx.message

        if len(message.attachments) > 0:
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            await ctx.send("Send me an image!")
            x = await self.bot.wait_for('message', check=check, timeout=15)
        except:
            return await ctx.send("Timed out...")

        if not len(x.attachments) >= 1:
            return await ctx.send("No images found.")

        return x.attachments[0].url

    @commands.command(aliases = ["hack"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def virus(self , ctx , user:discord.Member=None):
        lod = self.bot.get_emoji(568851263140265992)
        done = self.bot.get_emoji(560383768372838400)
        if user == None:
            user = ctx.guild
        msg = await ctx.send(f"{lod} Downloading Virus.")
	   
        await asyncio.sleep(1)
        await msg.edit(content = f"{lod} Downloading Virus..")
	   
        await asyncio.sleep(0.5)
        await msg.edit(content = f"{lod} Downloading Virus...")
       
        await asyncio.sleep(1.5)
        await msg.edit(content = f"{lod} Packing Files.")
	   
        await asyncio.sleep(1.2)
        await msg.edit(content = f"{lod} Packing Files..")
	   
        await asyncio.sleep(1)
        await msg.edit(content = f"{lod} Installing.")
	   
        await asyncio.sleep(1.5)
        await msg.edit(content = f"{lod} Installation Complete.")
	   
        await asyncio.sleep(2)
        await msg.edit(content = f"{lod} Running Setup!")
       
        await asyncio.sleep(1)
        await msg.edit(content = f"**{user}** Was Hacked Successfully! {done}")


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def phcom(self, ctx, *, comment: str):
        """PronHub Comment Image"""
        await ctx.trigger_typing()
        async with self.session.get(f"https://nekobot.xyz/api/imagegen?type=phcomment"
                          f"&image={ctx.author.avatar_url_as(format='png')}"
                          f"&text={comment}&username={ctx.author.name}") as r:
            res = await r.json()
        if not res["success"]:
            return await ctx.send("**Failed to successfully get image.**")
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tweet(self, ctx, username: str, *, text: str):
        """Tweet as someone."""
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=tweet"
                          "&username=%s"
                          "&text=%s" % (username, text,)) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def threats(self, ctx, user: discord.Member):
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=threats&url=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clyde(self, ctx, *, text: str):
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=clyde&text=%s" % text) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lolice(self, ctx):
        """KNOCK KNOCK KNOCK"""
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=lolice&url=%s" % ctx.author.avatar_url_as(format="png")) as r:
            res = await r.json()
        em = discord.Embed(color=0xfe8601)
        await ctx.send(embed=em.set_image(url=res["message"]))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def captcha(self, ctx, user: discord.Member):
        """Captcha a User OWO"""
        await ctx.trigger_typing()
        url = user.avatar_url_as(format="png")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=captcha&url=%s&username=%s" % (url, user.name,)) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))    

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def trash(self, ctx, user: discord.Member):
        """trash smh"""
        await ctx.trigger_typing()
        url = user.avatar_url_as(format="jpg")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=trash&url=%s" % (url,)) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def whowouldwin(self, ctx: commands.Context, user1: discord.Member, user2: discord.Member = None):
        """Who would win"""
        await ctx.trigger_typing()
        if user2 is None:
            user2 = ctx.author
        user1url = user1.avatar_url
        user2url = user2.avatar_url

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=whowouldwin&user1=%s&user2=%s" % (user1url, user2url,)) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))   


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def magik(self, ctx, user: discord.Member = None):
        """Magikify a member"""
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=magik&image=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))


    #@commands.command(name='lovecal')
    #async def quickgive(self,ctx,time:int=None,channel:discord.channel=None,name:str=None):
    #    if time = None:
    #        pass
    #    elif channel = None: pass
    #    elif name = None:
    #        pass
    #    else:
    #        users = await reaction.users().flatten()
            # users is now a list...
     #       winner = random.choice(users)
     #       await channel.send('{} has won the raffle.'.format(winner))
 
    @commands.command(name='gaycal',aliases = ["howgay"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gaycal(self, ctx ,* ,user=None):
        if user == None:
            embed=discord.Embed()
            embed.add_field(name="Name?!", value=" `Please Mention a Name | c!howgay [name]`", inline=True)
            await ctx.send(embed=embed)    
        else:
            embed=discord.Embed(title="Gay Percentage!", description="**{}** is **{}%** Gay ".format(user, random.randint(1 , 100)))
            embed.set_author(name="Gay", icon_url="https://cdn.discordapp.com/attachments/418005628255207424/462845519925084163/tumblr_p8us2iXWsD1viisjvo1_500.png")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=ctx.message.guild.name , icon_url=ctx.message.guild.icon_url)
            await ctx.send(embed=embed)    

    @commands.command(name='lovecal',aliases = ["lovecalc"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def luvcal(self ,ctx , user1=None,user2=None):
        user = user1
        user = user2
        if user == None:
            embed=discord.Embed()
            embed.add_field(name="Name?!", value=" `Please Mention a Name | c!lovecal [partner1] [partner2]`\nNo Space Between Partner1 & Partner2", inline=True)
            await ctx.send(embed=embed)    
        else:
            embed=discord.Embed(title="Love Percentage!", description="**{}** & **{}**\n**{}%** Loving Each Other!! <3".format(user1 ,user2 ,random.randint(1 , 100)))
            embed.set_author(name="💖 Love!")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=ctx.message.guild.name , icon_url=ctx.message.guild.icon_url)
            await ctx.send(embed=embed)    

    @commands.command(name='say')
    async def say(self ,ctx , *,args=None):
        if args is None:
            await ctx.message.delete()
            return
        if args == '@everyone':
            return
        if args == '@here':
            return
        else:
            await ctx.message.delete()
            await ctx.send(args)
 
    @commands.command(name='embedsay')
    async def esay(self ,ctx , *,args=None):
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:],16)
        color = discord.Color(value=color)
        if args is None:
            await ctx.message.delete()
            return
        if args == '@everyone':
            return
        if args == '@here':
            return
        else:
            await ctx.message.delete()
            emb = discord.Embed(color=color,description=args)
            await ctx.send(embed=emb)




    @commands.command()
    async def afk (self,ctx , *args):
        name = ' '.join(args)
        if "@everyone" in name: return
        elif "@here" in name: return
        else:
            embed=discord.Embed(color=0xfe8601)
            embed.set_thumbnail(url=str(ctx.author.avatar_url))
            embed.add_field(name="AFK" , value=name, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"{ctx.author.name} | {ctx.guild.name}",icon_url=str(ctx.author.avatar_url))            
            await ctx.send(embed=embed)
            await ctx.message.delete()
          #  def check(message):
           #      return ctx.message.author
           # await self.bot.wait_for('message', check=check)
          # await self.bot.wait_for_message(author=ctx.message.author)
           # embed=discord.Embed()
            #embed.add_field(name="{} is Now Back! :wave:".format(ctx.message.author.name), value="**{}**, Welcome Back !".format(ctx.message.author.name), inline=False)
           # await ctx.send(embed=embed)
    
 
    @commands.command(name='8ball')
    async def ball(self , ctx , question:str=None):
        try:
            if question is None:
                question = "Undefined"

            text = random.choice([":8ball: | **{},** It is Certain ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** It is Decidedly, So ?".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Without a doubt ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Yes, definitely  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** You may rely on it ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** As I see it, yes  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Most likely  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Outlook Looks Good  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Yes Bro ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Signs point to yes ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Reply lazy try again ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Ask again later ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Better not tell you now ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Cannot predict now ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Concentrate and ask again ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Don't count on it  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** My reply is no ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** My sources say no ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Outlook is Not So Good  ".format(ctx.message.author.name),
                                                                  ":8ball: | **{},** Very doubtful  ".format(ctx.message.author.name)])
            
            embed=discord.Embed(color=ctx.author.color)
            embed.add_field(name="Question:", value=question, inline=False)
            embed.add_field(name="Anwser:", value=text, inline=True)
            await ctx.send(embed=embed)
        except:
            return
            
 
def setup(bot):
    bot.add_cog(Fun(bot))

import discord
from discord.ext import commands
import random 
import time
import datetime
import urllib.parse , urllib.request , re
import requests

class Information(commands.Cog, name='Information'):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="bitcoin" , aliases = ["bcoin" , "btc"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bitc (self ,ctx,currency:str=None):
        try:
            if currency is None:
                currency = 'USD'
        
            #btc = self.bot.get_emoji(573731025126031370)
            url = 'https://blockchain.info/ticker'
            resp = requests.get(url)
            btc = resp.json()[currency]
            price = btc['symbol'] + ' ' + str(btc['last'])
            embed=discord.Embed()
            embed.add_field(name=":dollar: Current Bit Coin Price", value=f"{currency} : **{price}**", inline=False)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"{ctx.author.name} | {ctx.guild.name}",icon_url=str(ctx.author.avatar_url))            
            await ctx.send(embed=embed)            
        except:
            await ctx.send(f"`{currency}` is Not in Our Database :(")            
          
          
    @commands.command(name="invites" , aliases = ["invs"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def inv (self ,ctx ,user:discord.Member=None):
        uses = 0
        invites = await ctx.guild.invites()
        if user is None:
            user = ctx.author
        
        for invite in invites:
            if invite.inviter == ctx.message.author:
                uses += invite.uses

        embed=discord.Embed()
        embed.add_field(name="Server Invites", value=f"**{user}** Has **{uses}** Invites!", inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f"{user.name} | {ctx.guild.name}",icon_url=str(user.avatar_url))
        await ctx.send(embed=embed)


    @commands.command(name="youtube" , aliases = ["yt","ytsearch"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def youtube (self ,ctx ,* ,search=None):
        if search == None:
            embed=discord.Embed()
            embed.add_field(name="Search Term ?" , value="Search Term is Missing it is Required `c!youtube [Search Terms]`", inline=False)
            await ctx.send(embed=embed)
        else:
            query_string = urllib.parse.urlencode({
                'search_query' : search
            })
            htm_content = urllib.request.urlopen(
                'https://www.youtube.com/results?' + query_string 
            )
            serach_results = re.findall('href=\"\\/watch\\?v=(.{11})',htm_content.read().decode())
            link = 'https://www.youtube.com/watch?v=' + serach_results[0]
            embed=discord.Embed(title="New Search", url="https://cdn.discordapp.com/attachments/557766927070658564/573555443004342302/youtube-logo-png-picture-13.png")
            embed.set_author(name="YouTube", icon_url="https://cdn.discordapp.com/attachments/557766927070658564/573555443004342302/youtube-logo-png-picture-13.png")
            embed.add_field(name="Search Terms", value=search, inline=False)
            embed.add_field(name="Link", value=f"[Click Me]({link})", inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"{ctx.author.name}",icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)


    @commands.command(name="botinfo" , aliases = ["info","binfo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def binfo (self ,ctx):
        embed=discord.Embed(title="Join Our Support Server!", url="https://discord.gg/XHQhCJ")
        embed.set_author(name="Charlie", icon_url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024")
        embed.add_field(name="Name", value="Charlie", inline=True)
        embed.add_field(name="ID", value=self.bot.user.id, inline=True)
        embed.add_field(name="Users", value=len(set(self.bot.get_all_members())), inline=True)
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Channels", value=len([c for c in self.bot.get_all_channels()]), inline=True)
        embed.add_field(name="Bot Owner", value="the AnimatedStick#4797", inline=True)
        embed.add_field(name="Library", value="Python", inline=True)
        embed.add_field(name="Discord API Version", value=discord.__version__, inline=True)
        embed.add_field(name="Invite Link", value="[Link](https://discordapp.com/oauth2/authorize?client_id=568492275504775178&scope=bot&permissions=8)", inline=True)
        embed.add_field(name="Support Server Link", value="[Link](https://discord.gg/XHQhCJ)", inline=True)
        embed.add_field(name="Discord Bots Vote", value="Soon!", inline=True)
        embed.add_field(name="Help?", value="c!help", inline=True)
        embed.set_footer(text="the AnimatedStick #4797 | Charlie",icon_url=str(ctx.message.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name="links")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def links (self ,ctx):
        embed=discord.Embed(title="Links!")
        embed.set_author(name="Charlie", icon_url=str(self.bot.user.avatar_url))
        embed.add_field(name="Invite Link", value="[Link](https://discordapp.com/oauth2/authorize?client_id=568492275504775178&scope=bot&permissions=8)", inline=True)
        embed.add_field(name="Support Server Link", value='[Link](https://discord.gg/XHQhCJ)', inline=True)
        embed.add_field(name="Discord Bots Server Link", value='Soon', inline=True)
        embed.add_field(name="Owner Server", value='[Link](https://discord.gg/VNxu7fS)', inline=True)
        embed.set_footer(text="Charlie Links!",icon_url=str(ctx.message.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name="status" , aliases = ["membercount","stats"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def status (self ,ctx):
        #server = ctx.guild
        s = ctx.guild
        bots = 0
        for member in s.members:
            if member.bot:
                bots +=  1
        embed=discord.Embed(title="Server Status")
        embed.set_author(name=s.name, icon_url=str(ctx.message.guild.icon_url))
        embed.set_thumbnail(url=str(ctx.message.guild.icon_url))
        embed.add_field(name="Members", value=len(s.members), inline=False)
        embed.add_field(name="Bots", value=bots, inline=False)
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=False)
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=False)
        embed.set_footer(text="Server Status Requested By {} | {} ".format(ctx.message.author.name , ctx.message.guild.name),icon_url=str(ctx.message.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#
    @commands.command(name="members" , aliases = ["rmembers"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rmem(self , ctx ,*,roleN=None):
        
        if roleN is None:
            embed=discord.Embed()
            embed.add_field(name="Role Name Required!" , value="Provide a Role Name | `c!members [role name]`", inline=False)
            await ctx.send(embed=embed)
        else:
            role = discord.utils.get(ctx.guild.roles, name=roleN)
            embed=discord.Embed(title="Members With Role Name {}".format(role.name), url="https://discord.gg/DyPu726", color=role.colour)
            embed.set_author(name=role.name)
            embed.add_field(name="Members:", value=role.members, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="{}".format(ctx.message.guild.name),icon_url="{}".format(str(ctx.message.guild.icon_url)))
            await ctx.send(embed=embed)
#


    @commands.command(name="roleinfo" , aliases = ["rinfo"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def roleinfo(self , ctx , *,roleN=None):
        if roleN is None:
            embed=discord.Embed()
            embed.add_field(name="Role Name Required!" , value="Provide a Role Name | `c!roleinfo [role name]`", inline=False)
            await ctx.send(embed=embed)
        else:
            role = discord.utils.get(ctx.guild.roles, name=roleN)

            embed=discord.Embed(title="Role Information", url="https://discord.gg/DyPu726", color=role.colour)
            embed.set_author(name=role.name)
            embed.add_field(name="Role Name", value=role.name, inline=True)
            embed.add_field(name="Role ID", value=role.id, inline=True)
            embed.add_field(name="Members", value=len(role.members), inline=True)
            embed.add_field(name="Colour", value=role.colour, inline=True)
            embed.add_field(name="Position", value=role.position, inline=True)
            embed.add_field(name="Created", value=role.created_at, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="{}".format(ctx.message.guild.name),icon_url="{}".format(str(ctx.message.guild.icon_url)))
            await ctx.send(embed=embed)

    @commands.command(name="servericon" , aliases = ["sicon"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self , ctx):
        embed=discord.Embed(title="{} Server Icon".format(ctx.message.guild.name), url="https://discord.gg/DyPu726")
        embed.set_image(url=str(ctx.message.guild.icon_url))
        embed.set_author(name=ctx.message.guild.name, icon_url=ctx.message.guild.icon_url)
        embed.set_footer(text="Requested By {}".format(ctx.message.author.name) , icon_url=str(ctx.message.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self ,ctx, user: discord.Member = None):
        if not user:
            if not str(ctx.message.author.avatar_url):
                embed=discord.Embed()
                embed=discord.Embed(title="Your Avatar Link", url="{}".format(str(ctx.message.author.default_avatar_url)))
                embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(str(ctx.message.author.default_avatar_url)))
                embed.set_image(url=str(ctx.message.author.default_avatar_url))
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="{}".format(ctx.message.guild.name),icon_url="{}".format(str(ctx.message.guild.icon_url)))
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed()
                embed=discord.Embed(title="Your Avatar Link", url="{}".format(str(ctx.message.author.avatar_url)))
                embed.set_author(name="{}".format(ctx.message.author.name), icon_url="{}".format(str(ctx.message.author.avatar_url)))
                embed.set_image(url=str(ctx.message.author.avatar_url))
                embed.set_footer(text="{}".format(ctx.message.guild.name),icon_url="{}".format(ctx.message.guild.icon_url))
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
        else:
            if not user.avatar_url:
                embed=discord.Embed()
                embed=discord.Embed(title="{}'s Avatar Link".format(user.name), url="{}".format(str(user.default_avatar_url)))
                embed.set_author(name="{}".format(user.name), icon_url="{}".format(str(user.default_avatar_url)))
                embed.set_image(url=user.default_avatar_url)
                embed.set_footer(text="Requested By {}".format(ctx.message.author.name) ,icon_url="{}".format(str(ctx.message.guild.icon_url)))
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

            else:
                embed=discord.Embed()
                embed.set_author(name="{}".format(user.name), icon_url="{}".format(str(user.avatar_url)))
                embed=discord.Embed(title="{}'s Avatar Link".format(user.name), url="{}".format(str(user.avatar_url)))
                embed.set_author(name="{}".format(user.name), icon_url="{}".format(str(user.avatar_url)))
                embed.set_image(url=str(user.avatar_url))
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text="Requested By {}".format(ctx.message.author.name) ,icon_url="{}".format(ctx.message.guild.icon_url))
                await ctx.send(embed=embed)

    @commands.command(name="serverinfo" , aliases = ["sinfo", "server"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sinfo(self ,ctx):
     
        embed=discord.Embed(title="Server Information", url="https://discordapp.com/branding")
        embed.set_author(name=ctx.guild.name, icon_url=str(ctx.guild.icon_url))
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Server Owner ID", value=ctx.guild.owner.id, inline=True)
        embed.add_field(name="Server Roles", value=len(ctx.guild.roles), inline=True)
        embed.add_field(name="Server Members", value=len(ctx.guild.members), inline=True)
        embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=True)
        embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
        embed.add_field(name="Server Reigon", value=ctx.guild.region, inline=True)
        embed.add_field(name="Server Created", value=ctx.guild.created_at.strftime("%d %b %Y %H:%M"))
        embed.set_footer(text="Server Information Requested By {} | {} ".format(ctx.author.name , ctx.guild.name),icon_url=str(ctx.author.avatar_url))
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    

    @commands.command(name="userinfo",aliases = ["uinfo", "user" , "whois"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def userinfo(self ,ctx, user: discord.Member = None):
        if user is None:
            if not ctx.author.avatar_url:
                avatar = str(ctx.author.default_avatar_url)
            else:
                avatar = str(ctx.author.avatar_url)

            embed=discord.Embed(title="{}'s Information".format(ctx.message.author.name), url=avatar , color=ctx.author.color)
            embed.set_author(name=ctx.message.author.name, icon_url=avatar)
            embed.set_thumbnail(url=avatar)
            embed.add_field(name="User Name", value=ctx.message.author.name, inline=True)
            embed.add_field(name="User Tag", value="#" + ctx.message.author.discriminator, inline=True)
            embed.add_field(name="User ID", value=ctx.message.author.id, inline=True)
            embed.add_field(name="User Status", value=ctx.message.author.status, inline=True)
            embed.add_field(name="User Top Role", value=ctx.message.author.top_role, inline=True)
            embed.add_field(name="Bot User", value=ctx.message.author.bot, inline=True)
            embed.add_field(name="Join This Server", value=ctx.message.author.joined_at.strftime("%d %b %Y %H:%M"), inline=True)
            embed.add_field(name="User Created On", value=ctx.message.author.created_at.strftime("%d %b %Y %H:%M"), inline=True)
            embed.add_field(name="Nickname", value=ctx.message.author.display_name, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="{}".format(ctx.guild.name) ,icon_url="{}".format(str(ctx.guild.icon_url)))
            await ctx.send(embed=embed)

        else:
            if not user.avatar_url:
                ava = str(user.default_avatar_url)
            else:
                ava = str(user.avatar_url)

            embed=discord.Embed(title="{}'s Information".format(user.name), url=ava , color=user.color)
            embed.set_author(name=user.name, icon_url=ava)
            embed.set_thumbnail(url=ava)
            embed.add_field(name="User Name", value=user.name, inline=True)
            embed.add_field(name="User Tag", value="#" + user.discriminator, inline=True)
            embed.add_field(name="User ID", value=user.id, inline=True)
            embed.add_field(name="User Status", value=user.status, inline=True)
            embed.add_field(name="User Top Role", value=user.top_role, inline=True)
            embed.add_field(name="Bot User", value=user.bot, inline=True)
            embed.add_field(name="Joined Discord", value=user.joined_at.strftime("%d %b %Y %H:%M"), inline=True)
            embed.add_field(name="User Created On", value=user.created_at.strftime("%d %b %Y %H:%M"), inline=True)
            embed.add_field(name="Nickname", value=user.display_name, inline=True)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text="{}".format(ctx.author.name) ,icon_url="{}".format(str(ctx.guild.icon_url)))
            await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(Information(bot))

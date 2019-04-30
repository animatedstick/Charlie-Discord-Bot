from discord.ext import commands
import random 
import time
import datetime
import discord

class Events(commands.Cog, name='Events'):
    def __init__(self,bot):
        self.bot = bot
   
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        invite = await self.bot.create_invite(destination=ctx.message.channel, xkcd = True)
        join = self.bot.get_channel(572773776039739452)
        embed=discord.Embed(title="New Server!!")
        embed.set_thumbnail(url=str(guild.icon_url))
        embed.add_field(name='Server Name', value=guild.name, inline=True)
        embed.add_field(name='Server ID', value=guild.id, inline=True)
        embed.add_field(name='Server Owner', value=guild.owner, inline=True)
        embed.add_field(name='Server Owner ID', value=guild.owner.id, inline=True)
        embed.add_field(name='Server Members', value=len(guild.members), inline=True)
        embed.add_field(name='Server Invite', value=invite, inline=True)
        await join.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        server = member.guild
        if server.id == 554641659888140308:
            wlc = self.bot.get_channel(557774869719416844)
            embed=discord.Embed(title="Welcome!", url="https://discord.gg/9SVUNya", description=f"Welcome to the the AnimatedStick Crew Discord Server,\n **{member.name}** :wave:\n\nMake sure to check out the AnimatedStick YouTube Channel\nSubscribe & Support : [Channel Link](https://www.youtube.com/channel/UC0bZpIWLn_YEjkyTyvAadtQ?view_as=subscriber)\n`Have Great Time At the AnimatedStick Server`", color=0xfbb420)
            embed.set_author(name=member.name, icon_url=str(member.avatar_url))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"the AnimatedStick Crew",icon_url=str(server.icon_url))
            await wlc.send(embed=embed)

        elif server.id == 572346295830970370:
            wlc = self.bot.get_channel(572761367933747200)
            embed=discord.Embed(title="Charlie Support Server", url="https://discord.gg/9SVUNya", description=f"Welcome to the Charlie Support Server,\n **{member.name}** :wave:\n\nMake sure to vote Charlie at the Discord Bot List\nVote & Support : [Link](https://www.youtube.com/channel/UC0bZpIWLn_YEjkyTyvAadtQ?view_as=subscriber)\n`Have Great Time At the Charlie Support Server`", color=0xfe8601)
            embed.set_author(name=member.name, icon_url=str(member.avatar_url))
            embed.set_thumbnail(url=str(member.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text=f"Charlie Support Server",icon_url=str(server.icon_url))
            await wlc.send(embed=embed)
        else:
            return

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        invite = await self.bot.create_invite(destination=ctx.message.channel, xkcd = True)
        join = self.bot.get_channel(572773776039739452)
        embed=discord.Embed(title="Server Gone!!")
        embed.set_thumbnail(url=str(guild.icon_url))
        embed.add_field(name='Server Name', value=guild.name, inline=True)
        embed.add_field(name='Server ID', value=guild.id, inline=True)
        embed.add_field(name='Server Owner', value=guild.owner, inline=True)
        embed.add_field(name='Server Owner ID', value=guild.owner.id, inline=True)
        embed.add_field(name='Server Members', value=len(guild.members), inline=True)
        embed.add_field(name='Server Invite', value=invite, inline=True)
        await join.send(embed=embed)



def setup(bot):
    bot.add_cog(Events(bot))

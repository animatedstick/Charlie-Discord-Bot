import discord
from discord.ext import commands
import datetime
import asyncio

class Help(commands.Cog, name='Help'):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name='help', aliases = ["helpme","helpboi"])
    async def help(self,ctx,plug=None):
      try:
        if plug is None:
            embed=discord.Embed(title="Help & Support!", url="https://discord.gg/XHQhCJ", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024")
            embed.add_field(name="Information Commands", value="`c!help info`", inline=False)
            embed.add_field(name="Fun Commands", value="`c!help fun`", inline=False)
            embed.add_field(name="Moderation Commands", value="`c!help mod`", inline=False)
            embed.add_field(name="Tanki Online Commands", value="`c!help tanki`", inline=False)
            embed.add_field(name="Calculator Commands", value="`c!help calc`", inline=False)
            embed.add_field(name="Other Commands", value="`c!help other`", inline=False)
    #        embed.add_field(name="Prefixes" , value="`c! , C! , charlie , c , @Charlie`", inline=True)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        elif plug == 'info':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Information Commands", value="`c!btc [Currency]` - Check the Bitcoin Price!\n`c!youtube [Search Terms]` - Get The Video Link Without Seaching On YouTube\n`c!invites [User]` - Check How Many Invites a User Got!\n`c!avatar [user]` - Get Someone's Avatar\n`c!botinfo` - Some Information About Charlie\n`c!links` - Get Bot Realated Useful Links\n`c!userinfo [user]` - Get Information About a User!\n`c!serverinfo` - Get Server Information\n`c!roleinfo [role name]` - Gets Some Role Information\n`c!servericon` - Gets The Current Server Icon\n`c!stats` - Shows the Server Status!\n`c!ping` - Shows the Bot Ping\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        elif plug == 'fun':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Fun Commands", value="`c!virus [User]` - Send a fake virus to your firend!\n`c!8ball [Question]` - Ask a Question a From Charlie\n`c!captcha [User]` Captcha From a User\n`c!clyde [Text]` - Clyde Says Something..\n`c!gaycal [User]` - Let's Check How Gay Are You!\n`c!lolice [User]` - Look Who Joined the Police\n`c!lovecal [User1] [User2]` - Check the True Love!\n`c!magik [User]` - Make Your Avatar Awesome xD\n`c!phcom [User] [Text]` - Bad Boi Commenting On Po-- Hub\n`c!say [Text]` - Did you said Something?\n`c!threats [User]` - Who's the Threat For Us Lets Check!\n`c!trash [User]` - i Know You're Tranks Hmm\n`c!tweet [User] [Text]` - Someone Tweeted Something!\n`c!whowouldwin [User1] [User2]` - Who Would Win It ? Lets See!\n`c!embedsay [Text]` - The Bot Will Say Content In Embed\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)            
        elif plug == 'mod':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Moderation Commands", value="`c!mute [User] [Reason]` - Mutes a User & DM\n`c!unmute [User]` - Unmutes Muted Users!\n`c!ban [User] [Reason]` - Bans a Discord User From the Guild\n`c!kick [User] [Reason]` - Kicks a Discord User from the Server\n`c!addrole [User] [Role]` - Adds a Role to a User !\n`c!removerole [User] [Role]` - Removes a Role from a User\n`c!prune [Amount]` - Bulk Message Deleting In a Channel!\n`c!rename [User] [New Nick]` - Changes the Nickname of a Discord User.\n`c!softban [User]` - Deletes All User Messages Without Getting Banned.\n`c!warn [User] [Warn]` - Warns a Discord User !\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)            
        elif plug == 'tanki':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Tanki Online Commands", value="`c!ratings [Player Nickname]` - Check Ratings Of a Player!\n`c!container` - Opens a Container\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed) 
        elif plug == 'calc':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Calculator Commands", value="`c!add [Num1] [Num2]` - Adds 2 Numbers\n`c!substract [Num1] [Num2]` - Substract 2 Numbers\n`c!multiply [Num1] [Num2]` - Multiply 2 Numbers\n`c!divide [Num1] [Num2]` - Divide 2 Numbers\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed) 
        elif plug == 'other':
            embed=discord.Embed(title="Help & Support!", url="https://cdn.discordapp.com/avatars/568789990297829379/8c18c635c4933dac687e4c3c3e6e5e75.webp?size=1024", color=0xf4800b)
            embed.set_author(name="Charlie", icon_url="https://discordapp.com/api/users/568789990297829379/avatars/8c18c635c4933dac687e4c3c3e6e5e75.jpg")
            embed.add_field(name="Other Commands", value="`c!help` - Shows Help Message\n`c!uptime` - Check the Bot's Uptime\n`c!usages` - Check How Many Commands Have Been Used After Reboot\n\n**More Commands Coming Soon!**", inline=False)
            embed.set_footer(text="Charlie Help & Support!",icon_url=str(ctx.message.author.avatar_url))
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed) 


        else:
            return            
   
        
      except:
        pass
    

        
def setup(bot):
    bot.add_cog(Help(bot))

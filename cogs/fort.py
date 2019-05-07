import discord
from discord.ext import commands
import datetime
import asyncio
import requests
import os


FORTNITE_API_TOKEN = os.getenv("FT_TOKEN")

class Fortnite(commands.Cog, name='Fortnite'):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='ft', aliases = ["fortnite","ftstats"])
    async def fortnite(self,ctx,platform=None,words=None):
        if platform is None: 
            embed=discord.Embed()
            embed.add_field(name="Platform Required", value="Usage : `c!ft [Platform] [Nickname]`", inline=True)
            await ctx.send(embed=embed)
        elif words is None:
            embed=discord.Embed()
            embed.add_field(name="Nickname Required", value="Usage : `c!ft [Platform] [Nickname]`", inline=True)
            await ctx.send(embed=embed)
        else:
            res = fortnite_tracker_api(platform,words)

            if res:
                matches_played = res[0]['value']
                wins = res[1]['value']
                win_percent = res[2]['value']
                kills = res[3]['value']
                kd = res[4]['value']


                embed=discord.Embed(title="Fortnite Stats", url="https://www.epicgames.com/fortnite/buy-now", color=0x8000ff)
                embed.set_author(name=words, icon_url="https://cdn.discordapp.com/attachments/567025926756499458/575005939015352351/Fortnite_large.jpg")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/567025926756499458/575005939015352351/Fortnite_large.jpg")
                embed.add_field(name="Name", value=words, inline=True)
                embed.add_field(name="Matches Played", value="{}".format(matches_played), inline=True)
                embed.add_field(name="Wins", value="{}".format(wins), inline=True)
                embed.add_field(name="Win Percentage", value=win_percent, inline=True)
                embed.add_field(name="Kills", value="{}".format(kills), inline=True)   
                embed.add_field(name="K/D", value=kd, inline=True)
                embed.set_footer(text=f"Fortnite Stats For {words}",icon_url=str(ctx.author.avatar_url))
                await ctx.send(embed=embed)
           # else:
           #     embed=discord.Embed()
           #     embed.add_field(name="Nickname Invalid", value="The Nickname is Invalid , Double Check Your Spellings!", inline=True)
           #     await ctx.send(embed=embed)

def fortnite_tracker_api(platform, nickname):
  URL = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/' + nickname
  req = requests.get(URL, headers={"TRN-Api-Key": FORTNITE_API_TOKEN})

  if req.status_code == 200:
    try:
      #print(req.json())
      lifetime_stats = req.json()['lifeTimeStats']
      return lifetime_stats[7:]
    except KeyError:
      return False
  else:
    return False

        
def setup(bot):
    bot.add_cog(Fortnite(bot))

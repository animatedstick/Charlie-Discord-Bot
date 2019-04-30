import discord
from discord.ext import commands
import random 
import aiohttp
import datetime
import time

class Tanki(commands.Cog, name='Tanki'):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def container(self,ctx):
        smoky=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Smoky XT** !\n\n")
        smoky.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483134853450170368/Smoky_XT.png")
        smoky.timestamp = datetime.datetime.utcnow()
        smoky.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        railgun=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Railgun XT** !\n\n")
        railgun.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483134979014918155/Railgun_XT_M3.png")
        railgun.timestamp = datetime.datetime.utcnow()
        railgun.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        h=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Hornet XT** !\n\n")
        h.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483135744324403200/Hornet_XT_M3.png")
        h.timestamp = datetime.datetime.utcnow()
        h.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        gold=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **5 Gold Boxes** !\n\n")
        gold.set_image(url="https://cdn.discordapp.com/attachments/418005628255207424/484385707779948557/2BAGUnn.png")
        gold.timestamp = datetime.datetime.utcnow()
        gold.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        armour=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Double Armors** !\n\n")
        armour.set_image(url="https://images-ext-2.discordapp.net/external/tJBHwCrvNRZ53T8ETS7zWBsW0e-IStFtI3N0K_8gX-g/https/i.imgur.com/HfrwpgC.png")
        armour.timestamp = datetime.datetime.utcnow()
        armour.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))


        damage=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Double Damage** !\n\n")
        damage.set_image(url="https://images-ext-1.discordapp.net/external/vHRbVQW3OmIl6cEhbwkxGOK4OhoSvmg1tZuuG7AnaKg/https/i.imgur.com/FWXPzIR.png")
        damage.timestamp = datetime.datetime.utcnow()
        damage.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        speed=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Speed Boosts** !\n\n")
        speed.set_image(url="https://images-ext-2.discordapp.net/external/6hXUSOXZxxf3HssVQpCktvf-fa3N83hkrm_Dx-KOTmo/https/i.imgur.com/prSNowH.png")
        speed.timestamp = datetime.datetime.utcnow()
        speed.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        mines=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **125 Mines** !\n\n")
        mines.set_image(url="https://images-ext-2.discordapp.net/external/_lMR1l16QJePjZ7XhBvF-FZIMKxekvvH_k9vjcov7a8/https/i.imgur.com/RAahEO7.png")
        mines.timestamp = datetime.datetime.utcnow()
        mines.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        xll=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **100 Of All Supplies Pack** !\n\n")
        xll.set_image(url="https://images-ext-2.discordapp.net/external/coqjnOiCxy39C4-nK5u0q-UWrKEzBzIHRn4Oy6S-60g/https/i.imgur.com/wTvTgWn.png")
        xll.timestamp = datetime.datetime.utcnow()
        xll.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))
    
        inf=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Inferno Paint** !\n\n")
        inf.set_image(url="https://cdn.discordapp.com/attachments/418008017712447500/483139532170985472/Coloring_inferno.png")
        inf.timestamp = datetime.datetime.utcnow()
        inf.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        f=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Flora Paint** !\n\n")
        f.set_image(url="https://en.tankiwiki.com/images/en/9/94/Coloring_flora.png")
        f.timestamp = datetime.datetime.utcnow()
        f.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        c=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Corrosion Paint** !\n\n")
        c.set_image(url="https://en.tankiwiki.com/images/en/f/f2/Coloring_corrosion.png")
        c.timestamp = datetime.datetime.utcnow()
        c.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        l=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Lava Paint** !\n\n")
        l.set_image(url="https://en.tankiwiki.com/images/en/7/7e/Coloring_lava.png")
        l.timestamp = datetime.datetime.utcnow()
        l.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        e=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Eternity Paint** !\n\n")
        e.set_image(url="https://en.tankiwiki.com/images/en/a/af/Coloring_eternity.png")
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        m=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Moonwalker Paint** !\n\n")
        m.set_image(url="https://en.tankiwiki.com/images/en/a/a8/Coloring_Moonwalker.png")
        m.timestamp = datetime.datetime.utcnow()
        m.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        g=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Ginga Paint** !\n\n")
        g.set_image(url="https://en.tankiwiki.com/images/en/5/54/Ginga_paint.png")
        g.timestamp = datetime.datetime.utcnow()
        g.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        gg=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Galaxy Paint** !\n\n")
        gg.set_image(url="https://en.tankiwiki.com/images/en/4/41/Galaxy_paint.png")
        gg.timestamp = datetime.datetime.utcnow()
        gg.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        p=discord.Embed(title="Container Opened ", url="https://discord.gg/QP6ZdwK", description="\n\nYou've Just Received **Prodigy 2.0 Paint** !\n\n")
        p.set_image(url="https://en.tankiwiki.com/images/en/c/c6/Paint_Prodigy2.png")
        p.timestamp = datetime.datetime.utcnow()
        p.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))

        x = random.choice([smoky , railgun , h , speed , damage , armour , gold ,inf , xll , mines , f , c , l , e , g ,gg , m  ])
        await ctx.send(embed=x)        
 
    @commands.command()
    async def ratings(self,ctx, user: str=None ):
        url = "http://ratings.tankionline.com/get_stat/profile/?user={}&lang=en".format(user)
        async with aiohttp.ClientSession() as cs:
          async with cs.get(url) as r:
            if r.status == 200:
             #   try:
                    response = (await r.json())["response"]
                    #await bot.send_typing(ctx.message.channel)
                    kills = response["kills"]
                    deaths = response["deaths"]
                    crystals = response["earnedCrystals"]
                    gold = response["caughtGolds"]
                    exp = response["score"]
                    pre = response["hasPremium"]
                    name = response["name"]
                    gScore = response["gearScore"]

                    if user is None:
                        embed=discord.Embed()
                        embed.add_field(name="Nickname?", value="Please Enter a Nickname `c!ratings [Nickname]`", inline=True)
                        await ctx.send(embed=embed)

                    if exp > 0:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879078966493195/big_1.png"
                    if exp > 100:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879252652621824/big_2.png"
                    if exp > 500:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879413642330112/big_3.png"
                    if exp > 1500:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879626998448149/big_4.png"
                    if exp > 3700:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482879847518044190/big_5.png"
                    if exp > 7100:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883178219044864/big_6.png"
                    if exp > 12300:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883279947563009/big_7.png"
                    if exp > 20000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883347090243624/big_8.png"
                    if exp > 29000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883424017973258/big_9.png"
                    if exp > 41000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883518662311974/big_10.png"
                    if exp > 57000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883595636310017/big_11.png"
                    if exp > 76000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883736195694602/big_12.png"
                    if exp > 98000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883803552153610/big_13.png"
                    if exp > 125000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883928911511552/big_14.png"
                    if exp > 156000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482883976353153063/big_15.png"
                    if exp > 192000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884062843764756/big_16.png"
                    if exp > 233000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884115994116127/big_17.png"
                    if exp > 280000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884221191585792/big_18.png"
                    if exp > 332000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884285506912277/big_19.png"
                    if exp > 390000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884357032509440/big_20.png"
                    if exp > 450000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884406504194059/big_21.png"
                    if exp > 527000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884467170738186/big_22.png"
                    if exp > 606000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884523382669312/big_23.png"
                    if exp > 692000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884602596425728/big_24.png"
                    if exp > 787000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884667503149057/big_25.png"
                    if exp > 889000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884729151029248/big_26.png"
                    if exp > 1000000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884798138941441/big_27.png"
                    if exp > 1122000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884854883811329/big_28.png"
                    if exp > 1225000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884925784195082/big_29.png"
                    if exp > 1400000:
                        thumb = "https://cdn.discordapp.com/attachments/418008017712447500/482884995195863050/big_30.png"
                    if exp > 1600000:
                        thumb = "https://cdn.discordapp.com/attachments/418005628255207424/486047056092332042/big_31.png"

                    embed=discord.Embed(title="Ratings For {}".format(name), url="http://ratings.tankionline.com/en/user/{}/".format(name), description="\n\n\n")
                    embed.set_author(name=name)
                    embed.set_thumbnail(url=thumb)
                    embed.add_field(name="Nickname", value=name, inline=True)
                    embed.add_field(name="Experience" , value="{:,}".format(exp), inline=True)
                    embed.add_field(name="Premium Status" , value=pre , inline=True)
                    embed.add_field(name="Kills", value="{:,}".format(kills), inline=True)
                    embed.add_field(name="Deaths", value="{:,}".format(deaths), inline=True)
                    embed.add_field(name="K/D", value="{0:.2f}".format(kills/deaths), inline=True)
                    embed.add_field(name="Gear Score", value="{:,}".format(gScore), inline=True)
                    embed.add_field(name="Crystals Obtained", value="{:,}".format(crystals), inline=True)
                    embed.add_field(name="Gold Boxes Caught", value="{:,}".format(gold), inline=True)
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.set_footer(text=ctx.message.guild.name,icon_url=str(ctx.message.guild.icon_url))
                    await ctx.send(embed=embed)

              #  except:
                #    embed=discord.Embed()
                #    embed.add_field(name="Account Invalid", value="Account Does Not Exist !", inline=False)
                 #   await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Tanki(bot))

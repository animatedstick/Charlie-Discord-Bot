import discord
from discord.ext import commands
#import erorrs
import datetime
import asyncio

class Moderation(commands.Cog, name='Moderation Commands'):
    def __init__(self,bot):
        self.bot = bot
    @commands.command(name='addrole', aliases = ["role","giverole"])
    @commands.has_permissions(manage_roles=True)
    async def addrole(self,ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Add a role ! `c!addrole [user] [role]`", inline=True)
            await ctx.send(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role Name?!?", value="Please Mention a Role Name `c!addrole [user] [role]`", inline=True)
            await ctx.send(embed=embed)
        else:
            newrole = discord.utils.get(ctx.guild.roles, name=role)
            await user.add_roles(newrole)
            embed=discord.Embed()
            embed.add_field(name="Role Added :ok_hand:" , value="Role **{}**  Was Added to {}\n**Admin/Moderator:** {}".format(role,user,ctx.message.author), inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='removerole', aliases = ["rmvrole","roleremove"])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self,ctx,user:discord.Member=None,role:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Remove a role ! `c!removerole [user] [role]`", inline=True)
            await ctx.send(embed=embed)
        if role is None:
            embed=discord.Embed()
            embed.add_field(name="Role Name?", value="Please Mention a Role to Remove `c!removerole [user] [role]`", inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            newrole = discord.utils.get(ctx.message.guild.roles, name=role)
            await user.remove_roles(newrole)
            embed=discord.Embed()
            embed.add_field(name="Role Removed :ok_hand:" , value="Role **{}** Was Removed From {}\n**Admin/Moderator:** {}".format(role,user,ctx.message.author), inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='prune', aliases = ["delete","clear"])
    @commands.has_permissions(manage_messages=True)  
    async def prune(self,ctx , amount:int=None):
        if amount is None:
            embed=discord.Embed()
            embed.add_field(name="Provide a Amount Please!", value="Provide How Much Messages to Should Delete! `c!prune [amount]`", inline=True)
            await ctx.send(embed=embed)
        else:
            deleted = await ctx.channel.purge(limit=amount+1)
            embed=discord.Embed()
            embed.add_field(name="Deleted", value="**{}** Messages Deleted!\n**Admin/Moderator:** {}".format(len(deleted),ctx.message.author.name), inline=True)
            x = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await ctx.message.delete(x)

    @commands.command(name='rename', aliases = ["reset","setnick","resetnick"])
    @commands.has_permissions(manage_nicknames=True)
    async def rename(self,ctx,user:discord.Member=None,*,nick:str=None):
        if user is None:
            embed=discord.Embed()
            embed.add_field(name="User Required", value="Mention a User to Change Nickname ! `c!rename [user] [new nickname]`", inline=True)
            await ctx.send(embed=embed)
        elif nick is None:
            embed=discord.Embed()
            embed.add_field(name="Provide a New Nickname", value="We Need a New Nickname to Rename `c!rename [user] [new nickname]`", inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete()
            await user.edit(nick=nick)
            embed=discord.Embed()
            embed.add_field(name="User Was Rename! :ok_hand:", value="{}'s Nickname Was Changed to {} In {}\n**Admin/Moderator:** {}".format(user,nick,ctx.message.guild.name,ctx.author), inline=True)
            await ctx.send(embed=embed)
    
    @commands.command(name='mute')
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member=None,*,reason=None):
            if member is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Mute ! `c!mute [user]`", inline=False)
                await ctx.send(embed=embed)

            else:
                if reason is None:
                    Mreason = "Not Mentioned!"
                else:
                    Mreason = reason
              
                await ctx.message.delete()
                #overwrite = discord.PermissionOverwrite()
                #overwrite.read_messages = True
                #overwrite.send_messages = False
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages=False, add_reactions=False))
                for channel in ctx.guild.voice_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False))
                embed=discord.Embed(title="Member Muted!", url="https://discord.gg/DyPu726")
                embed.set_author(name=f"Mute | {member.name} ", icon_url=str(member.avatar_url))
                embed.set_thumbnail(url=str(member.avatar_url))
                embed.add_field(name="Muted User", value=member.mention, inline=False)
                embed.add_field(name="Admin/Moderator", value=ctx.author, inline=True)
                embed.add_field(name="Reason", value=Mreason, inline=True)
                embed.set_footer(text="Member Muted On {}".format(ctx.guild.name),icon_url=str(ctx.author.avatar_url))
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

                dembed=discord.Embed()
                dembed.add_field(name="Muted!", value=f"You Were Muted in **{ctx.guild.name}** !", inline=True)
                dembed.timestamp = datetime.datetime.utcnow()
                await member.send(embed=dembed)


    @commands.command(name='unmute')
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member=None):
            if member is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Unmute ! `c!unmute [user]`", inline=False)
                await ctx.send(embed=embed)

            else:
                await ctx.message.delete()
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(member, overwrite=None)
                for channel in ctx.guild.voice_channels:
                    await channel.set_permissions(member, overwrite=None)              
                embed=discord.Embed(title="Member Unmuted!", url="https://discord.gg/DyPu726")
                embed.set_author(name=f"Unmuted | {member.name} ", icon_url=str(member.avatar_url))
                embed.set_thumbnail(url=str(member.avatar_url))
                embed.add_field(name="Muted User", value=member.mention, inline=False)
                embed.add_field(name="Admin/Moderator", value=ctx.author, inline=True)
                embed.set_footer(text="Member Unmuted On {}".format(ctx.guild.name),icon_url=str(ctx.author.avatar_url))
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

                dembed=discord.Embed()
                dembed.add_field(name="Unmuted!", value=f"You Were Unmuted in **{ctx.guild.name}** !", inline=True)
                dembed.timestamp = datetime.datetime.utcnow()
                await member.send(embed=dembed)

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kick(self , ctx , user:discord.Member=None , reason:str=None):
            if reason is None:
                embed=discord.Embed()
                embed.add_field(name="Reason Required" , value="Provide a Reasons to Kick ! `c!kick [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Kick ! `c!kick [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user.id == ctx.message.guild.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="What a Noob , No Need to Kick Your Boss?", inline=True)
                await ctx.send(embed=embed)
            else:
                await user.kick()
                await ctx.message.delete()
                embed=discord.Embed(title=ctx.message.guild.name)
                embed.set_author(name="{} Was Kicked!".format(user))
                embed.add_field(name='Admin/Moderator', value=ctx.message.author, inline=False)
                embed.add_field(name='Channel', value=ctx.message.channel, inline=False)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='{} | {} Kicked!'.format(ctx.message.guild.name,user) , icon_url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed)


    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban(self , ctx , user:discord.Member=None,* , reason=None):
            if reason is None:
                embed=discord.Embed()
                embed.add_field(name="Reason Required" , value="Provide a Reasons to ban ! `c!ban [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Ban ! `c!ban [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user.id == ctx.message.guild.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="What a Noob , No Need to Ban Your Boss?", inline=True)
                await ctx.send(embed=embed)
            else:
                await user.ban()
                await ctx.message.delete()
                embed=discord.Embed(title=ctx.message.guild.name)
                embed.set_author(name="{} Was Banned!".format(user))
                embed.add_field(name='Admin/Moderator', value=ctx.message.author, inline=False)
                embed.add_field(name='Channel', value=ctx.message.channel, inline=False)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='{} | {} Banned!'.format(ctx.message.guild.name,user) , icon_url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed)

    @commands.command(name="softban")
    @commands.has_permissions(ban_members=True)
    async def softb(self , ctx , user:discord.Member=None,* , reason=None):
            if reason is None:
                embed=discord.Embed()
                embed.add_field(name="Reason Required" , value="Provide a Reasons to Softban ! `c!softban [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Ban ! `c!softban [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            elif user.id == ctx.message.guild.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Please No Epic Trolls Thanks!", inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.message.delete()
                await user.ban()
                await user.unban()
                embed=discord.Embed(title=ctx.message.guild.name)
                embed.set_author(name="{} Was SoftBanned!".format(user))
                embed.add_field(name='Admin/Moderator', value=ctx.message.author, inline=False)
                embed.add_field(name='Channel', value=ctx.message.channel, inline=False)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text='{} | {} SoftBanned!'.format(ctx.message.guild.name,user) , icon_url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed)                            
       

    
    @commands.command(name='warn')
    @commands.has_permissions(manage_messages=True)
    async def warn(self , ctx , user:discord.Member ,*, reason=None):
            if reason is None:
                embed=discord.Embed()
                embed.add_field(name="Reason Required" , value="Provide a Reasons to Mute ! `c!mute [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            if user is None:
                embed=discord.Embed()
                embed.add_field(name="User Required" , value="Mention a User to Ban ! `c!mute [user] [reason]`", inline=False)
                await ctx.send(embed=embed)
            if user.id == ctx.message.guild.owner.id:
                embed=discord.Embed()
                embed.add_field(name="Dude", value="Please No Epic Trolls Thanks!", inline=True)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Member Warned!")
                embed.set_author(name=user)
                embed.add_field(name='Member', value=user, inline=False)
                embed.add_field(name='Admin/Moderator', value=ctx.message.author, inline=True)
                embed.add_field(name='Reason', value=reason, inline=False)
                embed.timestamp = datetime.datetime.utcnow()
                embed.set_footer(text=ctx.message.guild.name,icon_url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Moderation(bot))

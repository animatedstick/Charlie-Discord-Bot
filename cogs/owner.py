from discord.ext import commands

command_attrs = {'hidden':True}

class OwnerCog(commands.Cog, name='Owner Commands', command_attrs=command_attrs):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='shutdown')
  #  @commands.is_owner()
    async def shut(self , ctx):
        await ctx.send('Bye :wave:!')
        self.bot.logout()

    @commands.command(name='load', hidden=True)
   # @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**Loaded**')

    @commands.command(name='unload')
   # @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**Unloaded**')

    @commands.command(name='reload')
   # @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**Reloaded**')

    async def cog_check(self, ctx):
        if not await ctx.bot.is_owner(ctx.author):
            raise commands.NotOwner(':face_plam: I am Not Your Boss!')
        return True

def setup(bot):
    bot.add_cog(OwnerCog(bot))

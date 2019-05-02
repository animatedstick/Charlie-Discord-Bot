import discord
from discord.ext import commands
import random 
import time
import datetime

class Calculator(commands.Cog, name='Calculator'):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def add(self,ctx,num1:int=None,num2:int=None):
        numbers = num1 and num2
        try:
            if numbers:
                await ctx.send("Please Specify the Numbers!! `c!add [Num1] [Num2]`")
            else:
                await ctx.send(num1 + num2)
        except:
            await ctx.send('Please Enter Numbers Only!')

    @commands.command()
    async def substract(self,ctx,num1:int,num2:int):
        numbers = num1 and num2
        try:
            if numbers:
                await ctx.send("Please Specify the Numbers!! `c!substract [Num1] [Num2]`")
            else:
                await ctx.send(num1 - num2)
        except:
            await ctx.send('Please Enter Numbers Only!')
    
    @commands.command()
    async def multiply(self,ctx,num1:int,num2:int):
        numbers = num1 and num2
        try:
            if numbers:
                await ctx.send("Please Specify the Numbers!! `c!multiply [Num1] [Num2]`")
            else:
                await ctx.send(num1 * num2)
        except:
            await ctx.send('Please Enter Numbers Only!')

    @commands.command()
    async def divide(self,ctx,num1:int,num2:int):
        numbers = num1 and num2
        try:
            if numbers:
                await ctx.send("Please Specify the Numbers!! `c!divide [Num1] [Num2]`")
            else:
                await ctx.send(num1 / num2)
        except:
            await ctx.send('Please Enter Numbers Only!')

def setup(bot):
    bot.add_cog(Calculator(bot))

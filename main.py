import discord
from discord.ext import commands
from keyP import token

slave = commands.Bot(command_prefix=':',case_insensitive='True')

@slave.command()
async def Hello(ctx):
    await ctx.send('Hi')
@slave.command()
async def pubg(ctx):
    await ctx.send('https://i.redd.it/wwmw37gr8gt01.png')


slave.run(token)
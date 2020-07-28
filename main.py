import discord
from discord.ext import commands
from keyP import token

slave = commands.Bot(command_prefix=':',case_insensitive='True')

@slave.event
async def on_ready():
    print('Ready to use')

@slave.command()
async def Hello(ctx):
    await ctx.send('Hi')
@slave.command()
async def pubg(ctx):
    await ctx.message.delete()
    await ctx.send('https://i.redd.it/wwmw37gr8gt01.png')
@slave.command()
async def clean(ctx,num = 1):
    await ctx.message.delete()
    async for message in ctx.channel.history(limit=num):
        await message.delete()

slave.run(token)
import discord
from discord.ext import commands
from keyP import token

slave = commands.Bot(command_prefix=':',case_insensitive='True')

slave.remove_command('help')

@slave.event
async def on_ready():
    await slave.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" :help"))
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


@slave.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send('**``` :pubg  -Vous montre une image des stats d\'arme de pubg \n :clean [nombre] -Supprime un nombre défini de messages dans le channel où cette commande est faite```**')

slave.run(token)
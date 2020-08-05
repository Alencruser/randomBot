import discord
import youtube_dl
from discord.ext import commands
from keyP import token

slave = commands.Bot(command_prefix=':',case_insensitive='True')
ytdl = youtube_dl.YoutubeDL()
slave.remove_command('help')

musics = {}


@slave.event
async def on_ready():
    await slave.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" :help"))
    print('Ready to use')

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download =False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url, before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)

    client.play(source,after=next)


@slave.command()
async def playlist(ctx,idx,url):
    await ctx.message.delete()
    video = Video(url)
    if len(musics[ctx.guild]) > 0 :
        musics[ctx.guild].insert(idx-1,video)


@slave.command()
async def play(ctx, url):
    await ctx.message.delete()

    server = ctx.guild.voice_client

    if server and server.channel:
        # ici append la musique si il joue ou jouer une musique si il est co
        video = Video(url)
        if len(musics[ctx.guild])>0:
            musics[ctx.guild].append(video)
        else:
            play_song(server, musics[ctx.guild], video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        connected = False
        server = await channel.connect()
        play_song(server, musics[ctx.guild], video)

@slave.command()
async def clear(ctx):
    await ctx.message.delete()
    del musics[ctx.guild]

@slave.command()
async def disconnect(ctx):
    await ctx.message.delete()
    await ctx.voice_client.disconnect()

@slave.command()
async def leave(ctx):
    await ctx.message.delete()
    await ctx.voice_client.disconnect()

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
async def join(ctx):
    await ctx.message.delete()
    channel = ctx.author.voice.channel
    await channel.connect()

@slave.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send('**``` :pubg  -Vous montre une image des stats d\'arme de pubg \n :clean [nombre] -Supprime un nombre défini de messages dans le channel où cette commande est faite```**')

slave.run(token)
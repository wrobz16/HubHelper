import discord
from discord.ext import commands, tasks



# import bot token
from apikeys import *

#################################################
# IMPORTANT STUFF
#################################################

# Name and Version
name = 'Hub Helper'
version = '0.1'

# some important stuff
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '-', intents=intents)

# start message in terminal
@client.event
async def on_ready():
    print('------------------------------------')
    print('Logged into ' + name + ' v' + version)
    print('------------------------------------')
    
# test command to verify bot is running
@client.command()
async def test(ctx):
    await ctx.send("test passed")

#################################################
# EVENTS
#################################################

# -----------------------------------------------
# When a member joins
@client.event
async def on_member_join(user):
    channel = client.get_channel(1055300125972512788)
    await channel.send('Welcome ' + user)

# -----------------------------------------------
# When a member leaves
@client.event
async def on_member_leave(user):
    channel = client.get_channel(1055300125972512788)
    await channel.send('Goodbye ' + user)

# -----------------------------------------------

#################################################
# COMMANDS
#################################################

# -----------------------------------------------
# PING COMMAND
# Continuously pings a user on a interval in seconds
@client.command()
async def ping(ctx, user, status, seconds=600):
    if (status.lower() == 'stop'):
        await ctx.send('Pinging stopped!')
        pingLoop.stop()
    elif (status.lower() == 'start'):
        await ctx.send('Pinging started for ' + user + ' every ' + str(seconds) + ' seconds!')
        pingLoop.change_interval(seconds=int(seconds))
        pingLoop.start(ctx, user)

# helper for ping
@tasks.loop(seconds=600)
async def pingLoop(ctx, user):
    await ctx.send(user)

# -----------------------------------------------
# allows the bot to join a voice channel
@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel!")

# -----------------------------------------------
# allows bot to leave the voice channel
@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I have left the voice channel!")
    else:
        await ctx.send("I'm not in a voice channel!")

# to start the bot
client.run(BOT_TOKEN)
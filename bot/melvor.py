import discord
from discord.ext import commands

client = commands.Bot(command_prefix=';')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run('ODU2Mjc4MTAwNzE4NTE4MzAy.YM-tIA.jJ9AyjhqP0pbJhKaiUD-JqRk1Z8')

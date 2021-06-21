import discord
import random
import numpy as np
from discord.ext import commands
from monsterlist import monsterDic, aliases

client = commands.Bot(command_prefix=';')

currentMonster = {}
droplist = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command
async def slay(ctx, monster, attempts):
    if monster < 0 or monster > 2:
        print('invalid monster')
        return

    for i in range(attempts):
        odds = random.uniform(0.00, 100.0)
        droplist.append(np.random.choice(monsterDic.keys(), attempts, replace=True, p=monsterDic.values()))
        print(droplist)
        return


client.run('ODU2Mjc4MTAwNzE4NTE4MzAy.YM-tIA.jJ9AyjhqP0pbJhKaiUD-JqRk1Z8')

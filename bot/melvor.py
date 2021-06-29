import discord
import numpy as np
from discord.ext import commands
import slayertools

client = commands.Bot(command_prefix=';')

droplist = []


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def slay(ctx, monster_name, attempts):
    if int(attempts) > 10000:
        await ctx.send("Don't kill my pc pls")
        return

    loot_table, always_drops = slayertools.get_monsterloot_table(monster_name)

    chances = np.array(loot_table['Chance.1'])
    chances /= chances.sum()

    for i in range(int(attempts)):

        droplist.append(np.random.choice(loot_table['Item'], p=chances))
        droplist.append(always_drops.iat[0, 0])

    neat = slayertools.neat_table(droplist)
    await ctx.send("```yaml\n" + neat + "\n```")
    droplist.clear()


client.run('ODU2Mjc4MTAwNzE4NTE4MzAy.YM-tIA.jJ9AyjhqP0pbJhKaiUD-JqRk1Z8')
import requests
import pandas as pd
import yaml
from collections import OrderedDict

# main_dic = {}

# scraped the monster list from the wiki
# and edited the monster list using Excel because python hurts my brain
# enemy_dataframe = pd.read_csv("shiny sheet.csv")

no_pop = False

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
}


def get_monsterloot_table(monster_name):
    monster_name.replace("_", " ")
    monster_url = "https://wiki.melvoridle.com/w/" + monster_name
    response = requests.get(monster_url, headers=headers)
    pd_list = pd.read_html(response.text)

    always_drops = pd_list[3]
    monster_loot = pd_list[4]

    # This block removes one of the Chance columns, removes the percentage symbol, and then divides probabilities by 100
    monster_loot.drop(labels='Chance', axis=1, inplace=True)
    monster_loot['Chance.1'] = list(map(lambda x: x[:-1], monster_loot['Chance.1'].values))
    monster_loot['Chance.1'] = [float(x) for x in monster_loot['Chance.1'].values]
    monster_loot['Chance.1'].div(100)

    total = monster_loot['Chance.1'].iloc[-1]
    total = total / 100

    edited_loot = pd.DataFrame()

    # The way df are processed changes based on the contents of the table
    if monster_loot.shape[0] == 1:
        edited_loot = single_drop(monster_loot)
    elif total < 1:
        edited_loot = partially_weighted(monster_loot)
    elif total == 1:
        edited_loot = fully_weighted(monster_loot)

    return edited_loot, always_drops


def neat_table(drop_list):
    loot_list = {i: drop_list.count(i) for i in drop_list}

    global no_pop

    if not no_pop:  # Removes the 'nothing' item
        loot_list.pop('')

    ordered_loot = sorted(loot_list, reverse=True)
    ordered_loot = yaml.dump(loot_list, allow_unicode=True, default_flow_style=False)

    no_pop = False

    return ordered_loot


def fully_weighted(monster_loot):
    number_of_indexes = len(monster_loot.index) - 1
    monster_loot.drop(number_of_indexes, axis=0, inplace=True)
    global no_pop
    no_pop = True
    return monster_loot


def partially_weighted(monster_loot):
    # This block calculates the chance of obtaining nothing, and adds it to the dataframe
    total_weight = 100 - monster_loot['Chance.1'][monster_loot.index[-1]]
    bad_luck = {'Item': '', 'Qty': '', 'Price': '', 'Chance.1': total_weight}
    monster_loot = monster_loot.append(bad_luck, ignore_index=True)
    number_of_indexes = len(monster_loot.index) - 2
    monster_loot.drop(number_of_indexes, axis=0, inplace=True)

    return monster_loot


def single_drop(monster_loot):
    total_weight = 100 - monster_loot['Chance.1'].iloc[-1]

    bad_luck = {'Item': '', 'Qty': '', 'Price': '', 'Chance.1': total_weight}
    monster_loot = monster_loot.append(bad_luck, ignore_index=True)

    return monster_loot

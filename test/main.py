monster = 'Black Knight'
attempts = 10
import random
import pprint
import numpy as np

BlackKnightDic = {
    'Black Boots': [0.0245, 1],
    'Black Helmet': [0.0147, 1],
    'Black Dagger': [0.0147, 1],
    'Black 2H Sword': [0.0098, 1],
    'Black Battleaxe': [0.0098, 1],
    'Black Sword': [0.0098, 1],
    'Black Shield': [0.0098, 1],
    'Black Scimitar': [0.0039, 1],
    'Black Platelegs': [0.0025, 1],
    'Black Platebody': [0.0005, 1],
}

BlackKnightDic1 = {
    'Black Boots': 0.0245,
    'Black Helmet': 0.0147,
    'Black Dagger': 0.0147,
    'Black 2H Sword': 0.0098,
    'Black Battleaxe': 0.0098,
    'Black Sword': 0.0098,
    'Black Shield': 0.0098,
    'Black Scimitar': 0.0039,
    'Black Platelegs': 0.0025,
    'Black Platebody': 0.0005,
    'Nothing': 0.9
}

HillGiantDic = {
    'Iron Arrows': [0.1825, 15],
    'Mantalyme Seeds': [0.1825, 1],
    'Onion Seeds': [0.1825, 10],
    'Cabbage Seed': [0.1825, 10],
    'Steel Arrows': [0.1825, 15],
    'Watermelon Seeds': [0.073, 5],
    'Sapphire': [0.00725, 1],
    'Ruby': [0.00725, 1],
}

AlwaysDropsDic = {
    'Black Knight': ['Bone', 1],
    'Hill Giant': ['Giant Bone', 1]
}

MonsterDic = {'Black Knight': BlackKnightDic,
              'Hill Giant': HillGiantDic
              }
drops = {}
drop = 0
droplist = random.choices(list(BlackKnightDic1.keys()), weights=BlackKnightDic1.values(), k=1000)
#print(droplist)
for i in range(1000):
    drops[droplist[i]] = drops.get(droplist[i], 0) + 1

sort_orders = sorted(drops.items(), key=lambda x: x[1], reverse=True)
pprint.pprint(sort_orders)
#print(sort_orders)

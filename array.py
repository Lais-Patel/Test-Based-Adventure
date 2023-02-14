"""
This is the guide basis for how the store array's will work
potion_seller = [name, cost, effect]
armour_store = [name, cost, defence, weight]
shield_store = [name, cost, block , weight]
weapon_store = [name, cost, attack, speed]
inventory = [weapon[], shield[],  armour[] , potion[]]"""

weapon_store = [["wooden sword", 10, 5, 5],["metal sword", 10, 10, 3],["iron sword", 10, 15, 4],["steel sword", 10, 20, 3],["diamond sword", 10, 30, 5],["mithryl sword", 10, 50, 3],["orichalcum sword", 10, 65, 6]]
shield_store = [["wooden shield", 10, 10, 3],["metal shield", 10, 15, 5],["iron shield", 10, 25, 7]]
armour_store = [["leather robes", 10, 3, 1],["chainmail", 10, 9, 5],["iron armour", 10, 20, 15]]
potion_seller = [["bad", 10, 5],["average", 10, 10],["good", 10, 20],["great", 10, 40],["elixir", 10, 100]]

inventory = [weapon_store[0],shield_store[0],armour_store[0],potion_seller[0]]

print(weapon_store[0][1])

"""
This is the guide basis for how my battle grounds array's will work
battle_field = [name, enemy_spawns]
enemy_spawns = [name, gold drops, health, damage, defense, speed]
enemy spawns will be out of"""

#not needed atm - enemy = ["Harry The Benson","Goblin","Hobgoblin","Orc","Troll","Dark Elf","Cobold","Dylan The Destroyer","Small Child","Theif","Bandit","Chiwawa","Dylan The Dominater","Dylan","Angry Mother","Rampant Belt"]

forest_spawns = [["Elf", 10, 6, 10, 2, 20],["Golbin", 5, 5, 5, 0, 5],["Golbina", 5, 5, 5, 0, 5],["One-horned Bunny", 5, 5, 5, 0, 5],["Green Slime", 5, 5, 5, 0, 5]]
deep_forest_spawns = [["Dark Elf", 10, 25, 15, 10, 25],["Orc", 5, 5, 5, 0, 5],["Kobold", 5, 5, 5, 0, 5],["Blue", 5, 5, 5, 0, 5]]
swamp_spawns = [["Witch", 10, 25, 25, 10, 30],["Red Slime", 5, 5, 5, 0, 5],["Lizard Newt", 5, 5, 5, 0, 5]]

battle_field = [["Forest",forest_spawns],["Deep Forest",deep_forest_spawns],["Swamp"],swamp_spawns]
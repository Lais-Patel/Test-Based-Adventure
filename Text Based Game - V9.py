import tkinter as tk
import random

#call my crazy but this is just needed like this, they're used everywhere
global encounter_text
global left_button
global right_button
global back_button
global forward_button
global window
global gold_label
global health_label
global health
global gold_image
global health_image
global title
global select_pointer_location
global location_check
global style
global gold

fruit_machine_icons = ["🍒","🔔","🍋","🍊","⭐","💀"]
direction_in_town = 0
gold = 100
health = 1000000
select_pointer_location = 0
location_check = 0
style = 1 #You can change what the gui color palette is here

weapons = [["wooden sword", 10, 500, 5],["metal sword", 10, 10, 3],["iron sword", 10, 15, 4],["steel sword", 10, 20, 3],["diamond sword", 10, 30, 5],["mithryl sword", 10, 50, 3],["orichalcum sword", 10, 65, 6]]
shields = [["wooden shield", 10, 10, 3],["metal shield", 10, 15, 5],["iron shield", 10, 25, 7],["steel shield", 10, 30, 3],["diamond shield", 10, 40, 5],["mithryl shield", 10, 60, 3],["orichalcum shield", 10, 70, 6]]
armours = [["leather robes", 10, 3, 1],["chainmail", 10, 9, 5],["iron armour", 10, 20, 15]]
potions = [["low quality potion", 10, 5],["average quality potion", 10, 10],["good quality potion", 10, 20],["great quality potion", 10, 40],["elixir", 10, 100]]

player_inventory = [weapons[0],shields[0],armours[0],potions[0]]

forest_spawns = [["Elf", 10, 6, 10, 2, 20],["Golbin", 5, 5, 5, 0, 5],["Golbina", 5, 5, 5, 0, 5],["One-horned Bunny", 5, 5, 5, 0, 5],["Green Slime", 5, 5, 5, 0, 5]]
deep_forest_spawns = [["Dark Elf", 10, 25, 15, 10, 25],["Orc", 5, 5, 5, 0, 5],["Kobold", 5, 5, 5, 0, 5],["Blue", 5, 5, 5, 0, 5]]
swamp_spawns = [["Witch", 10, 25, 25, 10, 30],["Red Slime", 5, 5, 5, 0, 5],["Lizard Newt", 5, 5, 5, 0, 5]]

battle_field = [["Forest",forest_spawns],["Deep Forest",deep_forest_spawns],["Swamp",swamp_spawns]]

def add_text(msg): #Adds a line of text on a new line to the text box
    global encounter_text  
    encounter_text.insert("end", "\n"+msg)

def wipe(): #Deletes all the text in the text box
    global encounter_text
    encounter_text.delete("1.0", "end")  

def unavailable(): #Placeholder for buttons
    print("Unavailable - Command Not Implemented")

def select_pointer_up(): #Detects the location and moves the select pointer up if possible
    global select_pointer_location
    if select_pointer_location != 0:
        encounter_text.delete((str(select_pointer_location+6)+".end-7c"),(str(select_pointer_location+6)+".end"))
        select_pointer_location -= 1
        encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

def select_pointer_down():  #Detects the location and moves the select pointer down if possible
    global location_check
    global select_pointer_location

    if location_check == 0:
        count = len(weapons)
    elif location_check == 1:
        count = len(shields)
    elif location_check == 2:
        count = len(armours)
    elif location_check == 3:
        count = len(potions)
    elif location_check == 4:
        count = len(battle_field)

    if select_pointer_location != count-1:
        encounter_text.delete((str(select_pointer_location+6)+".end-7c"),(str(select_pointer_location+6)+".end"))
        select_pointer_location += 1
        encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

def battlefield_selected_check():
    global select_pointer_location
    
    def leaving_back_to_town():
        global health
        global health_label
        wipe()
        add_text("")
        add_text("Accomplished from your win you leave")
        add_text("Arriving at the Town Gates you safetly enter")
        add_text("Due to the fatigue of your trip you go back")
        add_text("to your inn to rest for the night")
        add_text("")
        add_text("A revilatalising feeling engrosses your body")

        health = 100
        health_label.configure(text=health)

        left_button.configure(text = "Leave Inn", command = go_main_square)
        forward_button.configure(text = "<ADD>", command = unavailable)
        right_button.configure(text = "Stats", command = unavailable)
        back_button.configure(text = "Quit", command = window.destroy)

    def player_died(): 
        left_button.configure(text = "You", command = window.destroy)
        forward_button.configure(text = "Died", command = window.destroy)
        right_button.configure(text = "So", command = window.destroy)
        back_button.configure(text = "QUIT", command = window.destroy)
        health_label.configure(text="Dead")

    def enemy_died():
        global gold
        global gold_label

        gold += current_enemy[1]
        gold_label.configure(text=gold)
        left_button.configure(text = "Bring", command = battlefield_selected_check)
        forward_button.configure(text = "Next", command = battlefield_selected_check)
        right_button.configure(text = "Enemy", command = battlefield_selected_check)
        back_button.configure(text = "Return", command = leaving_back_to_town)

    def running_back_to_town():
        global health
        global health_label
        wipe()
        add_text("")
        add_text("You make a run for it, heading back to town")
        add_text("Arriving at the Town Gates you safetly enter")
        add_text("Due to the fatigue of your trip you go back")
        add_text("to your inn to rest for the night")
        add_text("")
        add_text("A revilatalising feeling engrosses your body")

        health = 100
        health_label.configure(text=health)

        left_button.configure(text = "Leave Inn", command = go_main_square)
        forward_button.configure(text = "<ADD>", command = unavailable)
        right_button.configure(text = "Stats", command = unavailable)
        back_button.configure(text = "Quit", command = window.destroy)

    def attack_enemy():
        encounter_text.delete("8.0","end")
        add_text("You thrust your sword toward the enemy")
        add_text("")
        player_attack_rng_change_amount = player_inventory[0][2]//5
        damage_dealt = random.randint((player_inventory[0][2]-player_attack_rng_change_amount) ,(player_inventory[0][2]+player_attack_rng_change_amount)) - current_enemy[4]
        if damage_dealt <= 0:
            add_text("The "+current_enemy[0]+" skillfully blocked the attack")
            add_text("It took no damage")
        else:
            add_text("You deal "+str(damage_dealt)+" of damage")
            add_text("Slashing the body of the enemy")
            current_enemy[2] -= damage_dealt
        if current_enemy[2] <= 0:
                enemy_died()
        elif current_enemy[2] > 0:
            #health_label.configure(text=health) Need to make an enemy indicator, so you know their stats

            add_text("")
            add_text(current_enemy[0]+" gets ready to counter")

            left_button.configure(text = "Brace", command = attacked_by_enemy)
            forward_button.configure(text = "For", command = attacked_by_enemy)
            right_button.configure(text = "Impact", command = attacked_by_enemy)
            back_button.configure(text = "Run", command = running_back_to_town)

    def attacked_by_enemy():
        global health
        global health_label
        global left_button
        global forward_button
        global right_button
        global back_button

        left_button.configure(text = "Attack", command = attack_enemy)
        forward_button.configure(text = "Block", command = unavailable)
        right_button.configure(text = "Heal", command = unavailable)
        back_button.configure(text = "Run", command = running_back_to_town)
        
        encounter_text.delete("8.0","end")
        add_text("They attack you before you can react")
        add_text("")
        enemy_attack_rng_change_amount = current_enemy[3]//5
        damage_taken = random.randint((current_enemy[3]-enemy_attack_rng_change_amount) ,(current_enemy[3]+enemy_attack_rng_change_amount)) - player_inventory[2][2]

        if damage_taken <= 0:
            add_text("Damage from incoming attack was fully nullified")
        else:
            add_text(str(damage_taken)+" damage was taken")
            health -= damage_taken
            if health <= 0:
                player_died()
            elif health > 0:
                health_label.configure(text=health)

    left_button.configure(text = "Attack", command = attack_enemy)
    forward_button.configure(text = "Block", command = unavailable)
    right_button.configure(text = "Heal", command = unavailable)
    back_button.configure(text = "Run", command = running_back_to_town)

    wipe()
    add_text("Hunting in the "+battle_field[select_pointer_location][0])
    add_text("")

    print(battle_field[select_pointer_location][1])
    current_enemy = battle_field[select_pointer_location][1][random.randint(0,(len(battle_field[select_pointer_location][1])-1))]
    print(current_enemy)

    if select_pointer_location == 0:
        add_text("You enter the local forest")
        add_text("Leaves surround you")
    elif select_pointer_location == 1:
        add_text("You venture deep into the forest")
        add_text("where light doesn't reach")
    elif select_pointer_location == 2:
        add_text("Trudging through think mud")
        add_text("you slosh into the mashy swamp")
    else:
        add_text("You go to your local battlefield")

    add_text("")
    add_text("You encounter a "+current_enemy[0])
    add_text("")

    speed_deficit = current_enemy[5] - (player_inventory[0][3]-(player_inventory[1][3]+player_inventory[2][3]))

    if speed_deficit >= 0:
        attacked_by_enemy()
    elif speed_deficit < 0:
        add_text("You spot a "+current_enemy[0]+" and ambush it")
        add_text("Getting the upperhand you attack first")
        add_text("")
        add_text("What do you do?")

def went_direction_check(): #It checks whcih direction you were facing, and then updates the button names and functions accordingly
    global left_button
    global right_button
    global back_button
    global forward_button
    global window
    global battle_field
    global location_check
    global select_pointer_location

    forward_button.configure(text = "Go Back", command = go_main_square)
    left_button.configure(command = unavailable)
    right_button.configure(command = unavailable)
    back_button.configure(text = "Quit", command = window.destroy)

    if direction_in_town == 0: #Selection area for which Battlefield to go to
        select_pointer_location = 0
        location_check = 4

        wipe()
        add_text("Currently at the Town Entrance")
        add_text("")
        add_text("You look out, wondering where you should head next")
        add_text("")

        for i in range(len(battle_field)):
            add_text(battle_field[i][0])

        encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

        left_button.configure(text = "Go up", command = select_pointer_up)
        forward_button.configure(text = "Select", command = battlefield_selected_check)
        right_button.configure(text = "Go down", command = select_pointer_down)
        back_button.configure(text = "Go Back", command = go_main_square)
    elif direction_in_town == 1:        
        def fruit_machine(): #Fruit Machine Gambaling
            import time
            global encounter_text
            global left_button
            global right_button
            global back_button
            global forward_button
            global gold_label
            global window
            global gold
            global fruit_machine_icons
            add_text("You are currently using the Fruit Machine")
            add_text("")

            def logic(rolled, gold_betted):
                global fruit_machine_icons
                global gold
                global gold_label
                if rolled[0] == rolled[1] == rolled [2] == fruit_machine_icons[5]:
                    add_text("GAME OVER")
                    gold = 0
                    gold_label.configure(text=gold)
                elif rolled[0] == fruit_machine_icons[5] or rolled[2] == fruit_machine_icons[5] or rolled [1] == fruit_machine_icons[5]:
                    add_text("SMALL LOSS")
                    gold -= int(gold_betted/5)
                    gold_label.configure(text=gold)
                elif rolled[0] == rolled[1] == fruit_machine_icons[5] or rolled[0] == rolled[2] == fruit_machine_icons[5] or rolled [1] == rolled[2] == fruit_machine_icons[5]:
                    add_text("LOSS")
                    gold -= gold_betted*2
                    if gold < 0:
                        gold = 0
                    gold_label.configure(text=gold)
                elif rolled[0] == rolled[1] == rolled [2] != fruit_machine_icons[5]:
                    add_text("Big win!")
                    gold += gold_betted
                    gold_label.configure(text=gold)
                elif rolled[0] == rolled[1] != fruit_machine_icons[5] or rolled[0] == rolled[2] != fruit_machine_icons[5] or rolled [1] == rolled[2] != fruit_machine_icons[5]:
                    add_text("Win")
                    gold += int(gold_betted/2)
                    gold_label.configure(text=gold)
                elif rolled[0] == rolled[1] == rolled [2] == fruit_machine_icons[1]:
                    add_text("Large win")
                    gold += gold_betted*2
                    gold_label.configure(text=gold)
                elif rolled[0] == rolled[1] == rolled [2] == fruit_machine_icons[4]:
                    add_text("JACKPOT!!")
                    gold += gold_betted*10
                    gold_label.configure(text=gold)
                else:
                    add_text("Nothing")
                    
                add_text("")
                encounter_text.insert("end", "You have ")
                encounter_text.insert("end", gold)
                encounter_text.insert("end", " Gold!")

            def bet_10():
                encounter_text.delete("6.0","end")
                main(10)
            def bet_100():
                encounter_text.delete("6.0","end")
                main(100)
            def bet_1000():
                encounter_text.delete("6.0","end")
                main(1000)

            def main(gold_betted):
                global gold
                global fruit_machine_icons
                if gold < gold_betted:
                    add_text("You're poor")
                elif gold >= gold_betted:
                    rolled = (fruit_machine_icons[random.randint(0,5)]),(fruit_machine_icons[random.randint(0,5)]),(fruit_machine_icons[random.randint(0,5)])
                    add_text("")
                    for i in range(3):
                        msg = rolled[i]
                        encounter_text.insert("end", msg)
                    logic(rolled, gold_betted)

            left_button.configure(text = "Bet 10", command = bet_10)
            forward_button.configure(text = "Bet 100", command = bet_100)
            right_button.configure(text = "Bet 1000", command = bet_1000)
            back_button.configure(text = "Go Back", command = went_direction_check)

        def wishing_well(): #Takes you to the wishing well
            import time
            global encounter_text
            global left_button
            global right_button
            global back_button
            global forward_button
            global gold_label
            global window
            global gold
            global fruit_machine_icons
            add_text("You stand infront of a marble well")
            add_text("Water glistens as it flies through the air")
            add_text("Wonder what happens if you throw some gold in?")

            def cry():
                encounter_text.delete("7.0","end")

                add_text("")
                add_text("Tears gently flow down your cheek")
                add_text("You gaze longlinly into the well")
                add_text("your reflection staring back at you")
                add_text("The water softly ripples as your teardrops")
                add_text("drip into the body of the well,")
                add_text('"Where did I go wrong?"')

            def pray():
                encounter_text.delete("7.0","end")

                add_text("")
                add_text("No response")

            def toss_coin():
                global gold
                global gold_label

                encounter_text.delete("7.0","end")

                if gold > 0:
                    gold -= 1
                    gold_label.configure(text=gold)

                    add_text("")
                    add_text("You throw a coin into the fountain, it sinks")
                    add_text("to the bottom, piling onto its predecessors")
                    add_text("")
                    add_text("You hope you've been blessed with better luck")
                else:
                    add_text("")
                    add_text("You gaze into your empty pockets full of air,")
                    add_text("with not a single trace of any gold")
                    add_text("The well lightly shakes with a sense of pity")
                    add_text("")
                    add_text("You walk away feeling worse about yourself")
                    forward_button.configure(text = "Cry", command = cry)

            left_button.configure(text = "<ADD>", command = unavailable)
            forward_button.configure(text = "Toss coin", command = toss_coin)
            right_button.configure(text = "Pray", command = pray)
            back_button.configure(text = "Go Back", command = went_direction_check)

        wipe()
        add_text("Currently on the Golden Road")
        add_text("")
        left_button.configure(text = "Fruit Machine", command = fruit_machine)
        right_button.configure(text = "Wishing Well", command = wishing_well)
    elif direction_in_town == 2:
        def buy_shop_item(): #Checks item and gold held, and allows to buy items
            global gold
            global gold_label
            global location_check

            if location_check == 0:
                selected_item = weapons[select_pointer_location]
                selected_item_cost = weapons[select_pointer_location][1]
            elif location_check == 1:
                selected_item = shields[select_pointer_location]
                selected_item_cost = shields[select_pointer_location][1]
            elif location_check == 2:
                selected_item = armours[select_pointer_location]
                selected_item_cost = armours[select_pointer_location][1]

            if gold >= selected_item_cost:
                gold -= selected_item_cost
                gold_label.configure(text=gold)
                if location_check == 0:
                    player_inventory[0] = selected_item
                elif location_check == 1:
                    player_inventory[1] = selected_item
                elif location_check == 2:
                    player_inventory[2] = selected_item

                add_text("")
                add_text("Item has been bought and equipped")
                print(player_inventory)
            else:
                add_text("")
                add_text("You don't have enough gold for this item")

        def select_to_shop(): # Middle man to ensure Go Back works correctly
            global location_check
            if location_check == 0:
                weapon_store_location()
            elif location_check == 1:
                shield_store_location()
            elif location_check == 2:
                armour_store_location()
            elif location_check == 3:
                potion_seller_location()

        def item_store_selected(): #Checks store location and displays buy menu for selected item
            global select_pointer_location
            global location_check

            encounter_text.delete("4.0", "end")
            add_text("")

            if location_check == 0:
                selected_item_name = weapons[select_pointer_location][0]
                selected_item_cost = weapons[select_pointer_location][1]
                selected_item_stat = weapons[select_pointer_location][2]
                selected_item_speed = weapons[select_pointer_location][3]
                stat_name = "Attack"
            elif location_check == 1:
                selected_item_name = shields[select_pointer_location][0]
                selected_item_cost = shields[select_pointer_location][1]
                selected_item_stat = shields[select_pointer_location][2]
                selected_item_speed = shields[select_pointer_location][3]
                stat_name = "Block"
            elif location_check == 2:
                selected_item_name = armours[select_pointer_location][0]
                selected_item_cost = armours[select_pointer_location][1]
                selected_item_stat = armours[select_pointer_location][2]
                selected_item_speed = armours[select_pointer_location][3]
                stat_name = "Defence"
            elif location_check == 3:
                selected_item_name = potions[select_pointer_location][0]
                selected_item_cost = potions[select_pointer_location][1]
                selected_item_stat = potions[select_pointer_location][2]
                stat_name = "Health Restored"
            
            add_text("Selected Item: ")
            encounter_text.insert("end",str(selected_item_name))
            add_text("")

            add_text("Cost: ")
            encounter_text.insert("end",str(selected_item_cost))
            add_text("")

            add_text(stat_name+": ")
            encounter_text.insert("end",str(selected_item_stat))
            add_text("")

            if location_check != 3:
                add_text("Speed: ")
                encounter_text.insert("end",str(selected_item_speed))
                add_text("")

            left_button.configure(text = "Buy item", command = buy_shop_item)
            forward_button.configure(text = "Buy item", command = buy_shop_item)
            right_button.configure(text = "Buy item", command = buy_shop_item)
            back_button.configure(text = "Go Back", command = select_to_shop)

        def potion_seller_location():#Displays the store of potions
            global location_check
            global select_pointer_location
            select_pointer_location = 0
            location_check = 3

            encounter_text.delete("4.0", "end")

            add_text("You are currently at the Potion Seller")
            add_text("")

            encounter_text.delete("6.0", "end")

            for i in range(len(potions)):
                add_text(potions[i][0])

            encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

            left_button.configure(text = "Go up", command = select_pointer_up)
            forward_button.configure(text = "Select", command = item_store_selected)
            right_button.configure(text = "Go down", command = select_pointer_down)
            back_button.configure(text = "Go Back", command = black_smith)

        def weapon_store_location(): #Displays the store of weapons
            global location_check
            global select_pointer_location
            select_pointer_location = 0
            location_check = 0

            encounter_text.delete("4.0", "end")

            add_text("You are currently at the Weapon Store")
            add_text("")

            encounter_text.delete("6.0", "end")

            for i in range(len(weapons)):
                add_text(weapons[i][0])

            encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

            left_button.configure(text = "Go up", command = select_pointer_up)
            forward_button.configure(text = "Select", command = item_store_selected)
            right_button.configure(text = "Go down", command = select_pointer_down)
            back_button.configure(text = "Go Back", command = black_smith)

        def shield_store_location(): #Displays the store of shields
            global location_check
            global select_pointer_location
            select_pointer_location = 0
            location_check = 1

            encounter_text.delete("4.0", "end")

            add_text("You are currently at the Shield Store")
            add_text("")

            encounter_text.delete("6.0", "end")

            for i in range(len(shields)):
                add_text(shields[i][0])

            encounter_text.insert((str(select_pointer_location+6)+".999"), "   <---")

            left_button.configure(text = "Go up", command = select_pointer_up)
            forward_button.configure(text = "Select", command = item_store_selected)
            right_button.configure(text = "Go down", command = select_pointer_down)
            back_button.configure(text = "Go Back", command = black_smith)

        def armour_store_location(): #Displays the store of armour
            global location_check
            global select_pointer_location
            select_pointer_location = 0
            location_check = 2

            encounter_text.delete("4.0", "end")

            add_text("You are currently at the Armour Store")
            add_text("")

            encounter_text.delete("6.0", "end")

            for i in range(len(armours)):
                add_text(armours[i][0])

            encounter_text.insert((str(select_pointer_location+6)+".999"), "   <---")
            
            left_button.configure(text = "Go up", command = select_pointer_up)
            forward_button.configure(text = "Select", command = item_store_selected)
            right_button.configure(text = "Go down", command = select_pointer_down)
            back_button.configure(text = "Go Back", command = black_smith)

        def black_smith(): #Takes you the the Blacksmith store selection
            global select_pointer_location
            select_pointer_location = 0

            encounter_text.delete("4.0", "end")

            add_text("You are currently at the Loacl dwarf's Blacksmith")
            add_text("It's split into different sectors,")
            add_text("for all types of gear you may need")
            add_text("The quality is of a type you've never seen before")
            add_text("")
            add_text("A short dwarf comes up to you and asks")
            add_text('"so what is it that you want today?"')

            left_button.configure(text = "Weapon Shop", command = weapon_store_location)
            forward_button.configure(text = "Shield Shop", command = shield_store_location)
            right_button.configure(text = "Armour Shop", command = armour_store_location)
            back_button.configure(text = "Go Back", command = went_direction_check)

        def luxury_shop(): #Takes you the the Noble store selection
            global select_pointer_location
            select_pointer_location = 0

            left_button.configure(text = "Potion Seller", command = potion_seller_location)
            forward_button.configure(text = "Enchanting", command = unavailable)
            right_button.configure(text = "<ADD>", command = unavailable)
            back_button.configure(text = "Go Back", command = went_direction_check)

        wipe()
        add_text("Currently in the Shopping Plaza")
        add_text("")
        left_button.configure(text = "Luxury Shop", command = luxury_shop)
        right_button.configure(text = "Black Smithy", command = black_smith)
    elif direction_in_town == 3:
        wipe()
        add_text("Currently outside Guild House")
        add_text("")
        left_button.configure(text = "Guild")
        right_button.configure(text = "<ADD AREA>")

def go_main_square(): #Sets the buttons to send you to the main square
    global left_button
    global right_button
    global back_button
    global forward_button
    global window

    def direction_check(): #Adds a gui indicator of which direction you are looking, by checking and then inserting based on that
        global encounter_text
        global direction_in_town
        
        encounter_text.delete("3.0", "end") 
        
        if direction_in_town == 0:
            add_text("")
            add_text("Facing the Town Entrance")
            add_text("")
            add_text("You look towards the Gate of the city")
            add_text("Guards stand below the massive arch way")
            add_text("Beyond those walls is the wild, where monsters")
            add_text("and bandits alike roam, ready to attack")
        elif direction_in_town == 1:
            add_text("")
            add_text("Facing the Golden Road")
            add_text("")
            add_text("Gold lines the road, money in the air")
            add_text("A large overbearing casino dominates the")
            add_text("landscape, a small well infront emmitting")
            add_text("a sense of oppitunity and luck")
        elif direction_in_town == 2:
            add_text("")
            add_text("Facing the Shopping Plaza")
            add_text("")
            add_text("The sounds of busy sales men fill the air,")
            add_text("shelves stacked to the sky of products")
            add_text("and crowded with people trying there best to")
            add_text("buy prime for the low low price of £20 per")
        elif direction_in_town == 3:
            add_text("")
            add_text("Facing the Guild House")
            add_text("")
            add_text("A waft of blood and sweat sweeps the area")
            add_text("Ahead it a tall building full of oppitunity")
            add_text("but accompined by dangers to great to imagine")

    def change_town_scene_left(): #When right is pressed, changes direction accordingly, checking to make sure it doesn't go over the min value
        global direction_in_town
        direction_in_town -= 1
        if direction_in_town == -1:
            direction_in_town += 4
        print(direction_in_town)
        direction_check()

    def change_town_scene_right(): #When right is pressed, changes direction accordingly, checking to make sure it doesn't go over the max value
        global direction_in_town
        direction_in_town += 1
        if direction_in_town == 4:
            direction_in_town -= 4
        print(direction_in_town)
        direction_check()

    wipe()
    add_text("Currently in Main Square")
    add_text("")
    direction_check()

    left_button.configure(text = "Turn Left", command = change_town_scene_left)
    forward_button.configure(text = "Go Forward", command = went_direction_check)
    right_button.configure(text = "Turn Right", command = change_town_scene_right)
    back_button.configure(text = "Quit", command = window.destroy)

def game_window_assembly(): #Making the base for the gui with no functions yet
    import os
    global encounter_text
    global left_button
    global right_button
    global back_button
    global forward_button
    global window
    global gold_label
    global gold_image
    global health_label
    global health_image
    global title
    global style

    window = tk.Tk()
    #window.geometry("473x500")#Sets the size of the window lxh
    window.minsize(500,550)    #Makes it so you can't resize the window
    #window.maxsize(473,500)   #to make it larger or smaller
    window.title("Battle RPG Game")

    encounter_text = tk.Text(window,bd=10)
    encounter_text.config(height=20, width=50, padx=20)

    """Yeah I just stole this off the internet cause I was getitng annoyed 
    at the image not being found, but hey it works :)"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "gold_coin.png")
    gold_coin_image = tk.PhotoImage(master=window, file=file_path)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "heart.png")
    heart_image = tk.PhotoImage(master=window, file=file_path)
    current_directory = os.path.dirname(os.path.abspath(__file__))

    health_image = tk.Label(window,image=heart_image)
    health_label = tk.Label(window, text=health, bd=1)
    gold_image = tk.Label(window,image=gold_coin_image)
    gold_label = tk.Label(window, text=gold, bd=1)

    if style == 1: #Dusty Ancient Ruin Color Scheme
        file_path = os.path.join(current_directory, "title_dusty.png")
        title_image = tk.PhotoImage(master=window, file=file_path)
        title = tk.Label(window,image=title_image)
    elif style == 2: #Wintry Cold Color Scheme
        file_path = os.path.join(current_directory, "title_cold.png")
        title_image = tk.PhotoImage(master=window, file=file_path)
        title = tk.Label(window,image=title_image)
    elif style == 3: #Firey Magma Color Scheme
        file_path = os.path.join(current_directory, "title_fire.png")
        title_image = tk.PhotoImage(master=window, file=file_path)
        title = tk.Label(window,image=title_image)
    elif style == 4: #Space Nebula Color Scheme
        file_path = os.path.join(current_directory, "title_nebula.png")
        title_image = tk.PhotoImage(master=window, file=file_path)
        title = tk.Label(window,image=title_image)

    left_button = tk.Button(window,bd=4)
    forward_button = tk.Button(window,bd=4)
    right_button = tk.Button(window,bd=4)
    back_button = tk.Button(window,bd=4)

    def asthetics(style):
        import os
        global encounter_text
        global left_button
        global right_button
        global back_button
        global forward_button
        global window
        global gold_label
        global gold_image
        global health_label
        global health_image
        global title
        
        if style == 1: #Dusty Ancient Ruin Color Scheme
            left_button.configure(background="#866345", foreground="#ECCEB0", activebackground="#7a5e3b", activeforeground="yellow")
            forward_button.configure(background="#866345", foreground="#ECCEB0", activebackground="#7a5e3b", activeforeground="yellow")
            right_button.configure(background="#866345", foreground="#ECCEB0", activebackground="#7a5e3b", activeforeground="yellow")
            back_button.configure(background="#866345", foreground="#FFAEAE", activebackground="#7a5e3b", activeforeground="red")
            encounter_text.configure(background="#d0baa6", foreground="black")

            health_image.configure(background="#c7a587", foreground="white")
            health_label.configure(background="#c7a587", foreground="black", activebackground="#7a5e3b", activeforeground="red")
            gold_image.configure(background="#c7a587", foreground="white")
            gold_label.configure(background="#c7a587", foreground="black", activebackground="#7a5e3b", activeforeground="red")
            title.configure(background="#c7a587", foreground="white")
            window.configure(background="#c7a587")
        elif style == 2: #Wintry Cold Color Scheme
            left_button.configure(background="#80B5C6", foreground="#DBF0F6", activebackground="#5c8c9c", activeforeground="yellow")
            forward_button.configure(background="#80B5C6", foreground="#DBF0F6", activebackground="#5c8c9c", activeforeground="yellow")
            right_button.configure(background="#80B5C6", foreground="#DBF0F6", activebackground="#5c8c9c", activeforeground="yellow")
            back_button.configure(background="#80B5C6", foreground="#FFAEAE", activebackground="#5c8c9c", activeforeground="red")
            encounter_text.configure(background="#d4e0e5", foreground="black")

            health_image.configure(background="#b8cfd5", foreground="white")
            health_label.configure(background="#b8cfd5", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            gold_image.configure(background="#b8cfd5", foreground="white")
            gold_label.configure(background="#b8cfd5", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            title.configure(background="#b8cfd5", foreground="white")
            window.configure(background="#b8cfd5")
        elif style == 3: #Firey Magma Color Scheme
            left_button.configure(background="#bf481d", foreground="#FAB15D", activebackground="#e5be22", activeforeground="yellow")
            forward_button.configure(background="#bf481d", foreground="#FAB15D", activebackground="#e5be22", activeforeground="yellow")
            right_button.configure(background="#bf481d", foreground="#FAB15D", activebackground="#e5be22", activeforeground="yellow")
            back_button.configure(background="#bf481d", foreground="#FFAEAE", activebackground="#e5be22", activeforeground="red")
            encounter_text.configure(background="#e5be22", foreground="#bf481d")

            health_image.configure(background="#d97e16", foreground="white")
            health_label.configure(background="#d97e16", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            gold_image.configure(background="#d97e16", foreground="white")
            gold_label.configure(background="#d97e16", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            title.configure(background="#d97e16", foreground="white")
            window.configure(background="#d97e16")
        elif style == 4: #Space Nebula Color Scheme
            left_button.configure(background="#5C4C9A", foreground="#D085DD", activebackground="#8a4e95", activeforeground="yellow")
            forward_button.configure(background="#5C4C9A", foreground="#D085DD", activebackground="#8a4e95", activeforeground="yellow")
            right_button.configure(background="#5C4C9A", foreground="#D085DD", activebackground="#8a4e95", activeforeground="yellow")
            back_button.configure(background="#5C4C9A", foreground="#FFAEAE", activebackground="#8a4e95", activeforeground="red")
            encounter_text.configure(background="#8a4e95", foreground="#141433")

            health_image.configure(background="#6B4290", foreground="white")
            health_label.configure(background="#6B4290", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            gold_image.configure(background="#6B4290", foreground="white")
            gold_label.configure(background="#6B4290", foreground="black", activebackground="#5c8c9c", activeforeground="red")
            title.configure(background="#6B4290", foreground="white")
            window.configure(background="#6B4290")

    def positioning():
        global encounter_text
        global left_button
        global right_button
        global back_button
        global forward_button
        global window
        global gold_label
        global gold_image
        global health_label
        global health_image
        global title

        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.columnconfigure(3, weight=1)

        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)

        left_button.configure(width=15, height=2)
        forward_button.configure(width=15, height=2)
        right_button.configure(width=15, height=2)
        back_button.configure(width=7, height=2)

        title.grid(row=0, column=0, columnspan=10,padx=10,pady=20)
        encounter_text.grid(row=1, column=0, columnspan=4,padx=10,pady=10)
        health_image.grid(row=2, column=0, columnspan=1,sticky="w",padx=20,pady=10)
        health_label.grid(row=2, column=0, columnspan=1,sticky="w",padx=44,pady=10)
        gold_image.grid(row=2, column=1, columnspan=1,sticky="w",padx=10,pady=10)
        gold_label.grid(row=2, column=1, columnspan=1,sticky="w",padx=30,pady=10)
        left_button.grid(row=3, column=0, columnspan=1,sticky="w",padx=10,pady=10)
        forward_button.grid(row=3, column=1, columnspan=1,sticky="w",padx=10,pady=10)
        right_button.grid(row=3, column=2, columnspan=1,sticky="w",padx=10,pady=10)
        back_button.grid(row=3, column=3, columnspan=1,sticky="w",padx=10,pady=10)

        encounter_text.grid_columnconfigure(0, weight=1)
        left_button.grid_columnconfigure(0, weight=1)
        forward_button.grid_columnconfigure(0, weight=1)
        right_button.grid_columnconfigure(0, weight=1)
        back_button.grid_columnconfigure(0, weight=1)

    asthetics(style)
    positioning()

    go_main_square()

    window.mainloop()

game_window_assembly()
import tkinter as tk
#not needed atm - enemy = ["Harry The Benson","Goblin","Hobgoblin","Orc","Troll","Dark Elf","Cobold","Dylan The Destroyer","Small Child","Theif","Bandit","Chiwawa","Dylan The Dominater","Dylan","Angry Mother","Rampant Belt"]
global encounter_text
global left_button
global right_button
global back_button
global forward_button
global window
global gold_label
global health_label
global health
global select_pointer_location
global shop_location_check
fruit_machine_icons = ["🍒","🔔","🍋","🍊","⭐","💀"]
direction_in_town = 0
gold = 100
health = 100
select_pointer_location = 0
shop_location_check = 0

weapons = [["wooden sword", 10, 5, 5],["metal sword", 10, 10, 3],["iron sword", 10, 15, 4],["steel sword", 10, 20, 3],["diamond sword", 10, 30, 5],["mithryl sword", 10, 50, 3],["orichalcum sword", 10, 65, 6]]
shields = [["wooden shield", 10, 10, 3],["metal shield", 10, 15, 5],["iron shield", 10, 25, 7],["steel shield", 10, 30, 3],["diamond shield", 10, 40, 5],["mithryl shield", 10, 60, 3],["orichalcum shield", 10, 70, 6]]
armours = [["leather robes", 10, 3, 1],["chainmail", 10, 9, 5],["iron armour", 10, 20, 15]]
potions = [["low quality potion", 10, 5],["average quality potion", 10, 10],["good quality potion", 10, 20],["great quality potion", 10, 40],["elixir", 10, 100]]

player_inventory = [weapons[0],shields[0],armours[0],potions[0]]

def add_text(msg): #Adds a line of text on a new line to the text box
    global encounter_text  
    encounter_text.insert("end", "\n"+msg)
    
def wipe(): #Deletes all the text in the text box
    global encounter_text
    encounter_text.delete("1.0", "end")  

def unavailable(): #Placeholder for buttons
    print("Unavailable - Command Not Implemented")

def fruit_machine(): #Fruit Machine Gambaling
    import random
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
    import random
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

    def pray():
        encounter_text.delete("7.0","end")

        add_text("")
        add_text("No response")

    def toss_coin():
        global gold
        global gold_label

        encounter_text.delete("7.0","end")

        gold -= 1
        gold_label.configure(text=gold)

        add_text("")
        add_text("You throw a coin into the fountain, it sinks")
        add_text("to the bottom, piling onto its predecessors")
        add_text("")
        add_text("You hope you've been blessed with better luck")

    left_button.configure(text = "<ADD>", command = unavailable)
    forward_button.configure(text = "Toss coin", command = toss_coin)
    right_button.configure(text = "Pray", command = pray)
    back_button.configure(text = "Go Back", command = went_direction_check)

def select_pointer_up(): #Detects the location and moves the select pointer up if possible
    global select_pointer_location
    if select_pointer_location != 0:
        encounter_text.delete((str(select_pointer_location+6)+".end-7c"),(str(select_pointer_location+6)+".end"))
        select_pointer_location -= 1
        encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

def select_pointer_down():  #Detects the location and moves the select pointer down if possible
    global shop_location_check
    global select_pointer_location

    if shop_location_check == 0:
        count = len(weapons)
    elif shop_location_check == 1:
        count = len(shields)
    elif shop_location_check == 2:
        count = len(armours)
    elif shop_location_check == 3:
        count = len(potions)

    if select_pointer_location != count-1:
        encounter_text.delete((str(select_pointer_location+6)+".end-7c"),(str(select_pointer_location+6)+".end"))
        select_pointer_location += 1
        encounter_text.insert((str(select_pointer_location+6)+".end"), "   <---")

def buy_shop_item(): #Checks item and gold held, and allows to buy items
    global gold
    global gold_label
    global shop_location_check

    if shop_location_check == 0:
        selected_item = weapons[select_pointer_location]
        selected_item_cost = weapons[select_pointer_location][1]
    elif shop_location_check == 1:
        selected_item = shields[select_pointer_location]
        selected_item_cost = shields[select_pointer_location][1]
    elif shop_location_check == 2:
        selected_item = armours[select_pointer_location]
        selected_item_cost = armours[select_pointer_location][1]

    if gold >= selected_item_cost:
        gold -= selected_item_cost
        gold_label.configure(text=gold)
        if shop_location_check == 0:
            player_inventory[0] = selected_item
        elif shop_location_check == 1:
            player_inventory[1] = selected_item
        elif shop_location_check == 2:
            player_inventory[2] = selected_item

        add_text("")
        add_text("Item has been bought and equipped")
        print(player_inventory)
    else:
        add_text("")
        add_text("You don't have enough gold for this item")

def select_to_shop(): # Middle man to ensure Go Back works correctly
    global shop_location_check
    if shop_location_check == 0:
        weapon_store_location()
    elif shop_location_check == 1:
        shield_store_location()
    elif shop_location_check == 2:
        armour_store_location()
    elif shop_location_check == 3:
        potion_seller_location()

def item_store_selected(): #Checks store location and displays buy menu for selected item
    global select_pointer_location
    global shop_location_check

    encounter_text.delete("4.0", "end")
    add_text("")

    if shop_location_check == 0:
        selected_item_name = weapons[select_pointer_location][0]
        selected_item_cost = weapons[select_pointer_location][1]
        selected_item_stat = weapons[select_pointer_location][2]
        selected_item_speed = weapons[select_pointer_location][3]
        stat_name = "Attack"
    elif shop_location_check == 1:
        selected_item_name = shields[select_pointer_location][0]
        selected_item_cost = shields[select_pointer_location][1]
        selected_item_stat = shields[select_pointer_location][2]
        selected_item_speed = shields[select_pointer_location][3]
        stat_name = "Block"
    elif shop_location_check == 2:
        selected_item_name = armours[select_pointer_location][0]
        selected_item_cost = armours[select_pointer_location][1]
        selected_item_stat = armours[select_pointer_location][2]
        selected_item_speed = armours[select_pointer_location][3]
        stat_name = "Defence"
    elif shop_location_check == 3:
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

    if shop_location_check != 3:
        add_text("Speed: ")
        encounter_text.insert("end",str(selected_item_speed))
        add_text("")

    left_button.configure(text = "Buy item", command = buy_shop_item)
    forward_button.configure(text = "Buy item", command = buy_shop_item)
    right_button.configure(text = "Buy item", command = buy_shop_item)
    back_button.configure(text = "Go Back", command = select_to_shop)

def potion_seller_location():#Displays the store of potions
    global shop_location_check
    global select_pointer_location
    select_pointer_location = 0
    shop_location_check = 3

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
    global shop_location_check
    global select_pointer_location
    select_pointer_location = 0
    shop_location_check = 0

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
    global shop_location_check
    global select_pointer_location
    select_pointer_location = 0
    shop_location_check = 1

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
    global shop_location_check
    global select_pointer_location
    select_pointer_location = 0
    shop_location_check = 2

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

def went_direction_check(): #It checks whcih direction you were facing, and then updates the button names and functions accordingly
    global left_button
    global right_button
    global back_button
    global forward_button
    global window

    forward_button.configure(text = "Go Back", command = go_main_square)
    left_button.configure(command = unavailable)
    right_button.configure(command = unavailable)
    back_button.configure(text = "Quit", command = window.destroy)

    if direction_in_town == 0:
        wipe()
        add_text("Currently at the Town Entrance")
        add_text("")
        left_button.configure(text = "Hunting Grounds")
        right_button.configure(text = "<ADD AREA>")
    elif direction_in_town == 1:
        wipe()
        add_text("Currently on the Golden Road")
        add_text("")
        left_button.configure(text = "Fruit Machine", command = fruit_machine)
        right_button.configure(text = "Wishing Well", command = wishing_well)
    elif direction_in_town == 2:
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

    wipe()
    add_text("Currently in Main Square")
    add_text("")
    direction_check()

    left_button.configure(text = "Turn Left", command = change_town_scene_left)
    forward_button.configure(text = "Go Forward", command = went_direction_check)
    right_button.configure(text = "Turn Right", command = change_town_scene_right)
    back_button.configure(text = "Quit", command = window.destroy)

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
    
def game_window_assembly(): #Making the base for the gui with no functions yet
    import os
    global encounter_text
    global left_button
    global right_button
    global back_button
    global forward_button
    global window
    global gold_label
    global health_label

    window = tk.Tk()
    window.geometry("473x500") #Sets the size of the window lxh
    window.minsize(473,500)    #Makes it so you can't resize the window
    #window.maxsize(473,500)    #to make it larger or smaller
    window.title("Battle RPG Game")

    encounter_text = tk.Text(window,bd=10)

    encounter_text.config(height=20, width=50, padx=20)

    #Yeah I just stole this off the internet cause I was getitng annoyed 
    #at the image not being found, but hey it works :)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "gold_coin.png")
    gold_coin_image = tk.PhotoImage(master=window, file=file_path)
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "heart.png")
    heart_image = tk.PhotoImage(master=window, file=file_path)

    health_image= tk.Label(window, image=heart_image)
    health_label= tk.Label(window, text=health, bd=1)
    gold_image= tk.Label(window, image=gold_coin_image)
    gold_label= tk.Label(window, text=gold, bd=1)

    left_button = tk.Button(window,bd=4)
    forward_button = tk.Button(window,bd=4)
    right_button = tk.Button(window,bd=4)
    back_button = tk.Button(window,bd=4)

    title = tk.Label(window, text = "Simple Adventure RPG")
    title.config(font =("Courier", 15))
    
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

    title.grid(row=0, column=0, columnspan=10,padx=10,pady=10)
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

    go_main_square() 
    window.mainloop()

game_window_assembly()
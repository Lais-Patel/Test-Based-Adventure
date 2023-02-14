import tkinter as tk
enemy = ["Harry The Benson","Goblin","Hobgoblin","Orc","Troll","Dark Elf","Cobold","Dylan The Destroyer","Small Child","Theif","Bandit","Chiwawa","Dylan The Dominater","Dylan","Angry Mother","Rampant Belt"]
global encounter_text
global left_button
global right_button
global back_button
global forward_button
global window
direction = 0

def add_text(msg):
    global encounter_text
    encounter_text.delete("1.0", "end")    
    encounter_text.insert("end", "\n"+msg)




def unavailable():
    print("Unavailable - Command Not Implemented")

def went_direction_check():
    global left_button
    global right_button
    global back_button
    global forward_button
    global window

    forward_button.configure(text = "Go Back", command = go_main_square)
    left_button.configure(command = unavailable)
    right_button.configure(command = unavailable)
    if direction == 0:
        add_text("Currently in Entrance")
        left_button.configure(text = "Hunting Grounds")
        right_button.configure(text = "<ADD AREA>")
    elif direction == 1:
        add_text("Currently in Gambaling Vegas")
        left_button.configure(text = "Casino")
        right_button.configure(text = "Wishing Well")
    elif direction == 2:
        add_text("Currently in Shopping Area")
        left_button.configure(text = "Luxury Shop")
        right_button.configure(text = "Market Stand")
    elif direction == 3:
        add_text("Currently in Quests")
        left_button.configure(text = "Guild")
        right_button.configure(text = "<ADD AREA>")

def go_main_square():
    global left_button
    global right_button
    global back_button
    global forward_button
    global window

    add_text("Currently in Main Square")

    left_button.configure(text = "Turn Left", command = change_town_scene_left)
    forward_button.configure(text = "Go Forward", command = went_direction_check)
    right_button.configure(text = "Turn Right", command = change_town_scene_right)
    back_button.configure(text = "Quit", command = window.destroy)

def change_town_scene_left():
    global direction
    direction -= 1
    if direction == -1:
        direction += 4
    print(direction)
def change_town_scene_right():
    global direction
    direction += 1
    if direction == 4:
        direction -= 4
    print(direction)

def gui():
    global encounter_text
    global left_button
    global right_button
    global back_button
    global forward_button
    global window

    window = tk.Tk()
    window.geometry("470x350")
    window.minsize(470,350)
    window.maxsize(470,350)
    window.title("Battle RPG Game")

    encounter_text = tk.Text(window,bd=10)
    encounter_text.config(height=10, width=50, padx=20)

    left_button = tk.Button(window, text = "Turn Left", command = change_town_scene_left,bd=4)
    forward_button = tk.Button(window, text = "Go Forward", command = went_direction_check,bd=4)
    right_button = tk.Button(window, text = "Turn Right", command = change_town_scene_right,bd=4)
    back_button = tk.Button(window, text = "Quit", command = window.destroy,bd=4)

    title = tk.Label(window, text = "Simple Adventure RPG")
    title.config(font =("Courier", 15))

    window.columnconfigure(0, weight=3)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=10)

    left_button.configure(width=15, height=2)
    forward_button.configure(width=15, height=2)
    right_button.configure(width=15, height=2)
    back_button.configure(width=7, height=2)

    title.grid(row=0, column=0, columnspan=10,padx=10,pady=10)
    encounter_text.grid(row=1, column=0, columnspan=5,padx=10,pady=10)
    left_button.grid(row=2, column=0, columnspan=1,sticky="w",padx=10,pady=10)
    forward_button.grid(row=2, column=1, columnspan=1,sticky="w",padx=10,pady=10)
    right_button.grid(row=2, column=2, columnspan=1,sticky="w",padx=10,pady=10)
    back_button.grid(row=2, column=3, columnspan=1,sticky="e",padx=10,pady=10)

    encounter_text.grid_columnconfigure(0, weight=1)
    left_button.grid_columnconfigure(0, weight=1)
    forward_button.grid_columnconfigure(0, weight=1)
    right_button.grid_columnconfigure(0, weight=1)
    back_button.grid_columnconfigure(0, weight=1)

    window.mainloop()

gui()
from tkinter import *
import random

parent = Tk()
parent.title("Rock Paper Scissor Game")
parent.geometry("400x400")
parent.config(background = "light pink")

def start():
    global player_score,comp_score
    parent.withdraw()
    root = Tk()
    root.title("Rock Paper Scissor Game")

    # Possibilities for winning
    outcomes = {
        "rock": {"rock": 1, "paper": 0, "scissors": 2},
        "paper": {"rock": 2, "paper": 1, "scissors": 0},
        "scissors": {"rock": 0, "paper": 2, "scissors": 1}
    }

    comp_score = 0
    player_score = 0


    # Functions
    def converted_outcome(number):
        if number == 1:
            return "rock"
        elif number == 2:
            return "paper"
        elif number == 3:
            return "scissors"


    def outcome_handler(user_choice):
        global comp_score
        global player_score
        random_number = random.randint(1, 3)
        computer_choice = converted_outcome(random_number)
        outcome = outcomes[user_choice][computer_choice]

        player_choice_label.config(fg="green", text="Player Choice : " + str(user_choice))
        computer_choice_label.config(fg="green", text="Computer Choice : " + str(computer_choice))

        if outcome == 2:
            player_score = player_score + 2
            player_score_label.config(text="Player : " + str(player_score))
            outcome_label.config(fg="blue", text="Outcome : Player Won")

        elif outcome == 0:
            comp_score = comp_score + 2
            computer_score_label.config(text="Computer : " + str(comp_score))
            outcome_label.config(fg="blue", text="Outcome : Computer Won")

        elif outcome == 1:
            player_score = player_score + 1
            comp_score = comp_score + 1
            player_score_label.config(text="Player : " + str(player_score))
            computer_score_label.config(text="Computer : " + str(comp_score))
            outcome_label.config(fg="blue", text="Outcome : Draw")

    # New Function
    def new():
        player_choice_label.grid_forget()
        computer_choice_label.grid_forget()
        player_score_label.grid_forget()
        computer_score_label.grid_forget()
        outcome_label.grid_forget()
        root.withdraw()
        start()



    # Add menu to the game
    my_menu = Menu(root)
    root.config(menu = my_menu)
    # Add items
    items = Menu(my_menu,tearoff = 0)
    my_menu.add_cascade(label = "File",menu = items)
    items.add_command(label = "New Game",command = new)
    items.add_separator()
    items.add_command(label = "Exit",command = root.quit)


    # Labels
    Label(root, text="Rock, Paper, Scissors", font=("Calibri", 14,'bold')).grid(row=0, sticky=N, pady=10, padx=200)
    Label(root, text="Please select an option!!", font=("Calibri", 12),fg = "red").grid(row=1, sticky=N)


    player_score_label = Label(root, text="Player : 0", font=("Calibri", 12))
    player_score_label.grid(row=2, sticky=W)


    computer_score_label = Label(root, text="Computer : 0", font=("Calibri", 12))
    computer_score_label.grid(row=2, sticky=E)


    player_choice_label = Label(root, font=("Calibri", 12))
    player_choice_label.grid(row=3, sticky=W)


    computer_choice_label = Label(root, font=("Calibri", 12))
    computer_choice_label.grid(row=3, sticky=E)


    outcome_label = Label(root, font=("Calibri", 12))
    outcome_label.grid(row=3, sticky=N)


    # Buttons
    rock_btn = Button(root, text="Rock", width=15, command=lambda: outcome_handler("rock"))
    paper_btn = Button(root, text="Paper", width=15, command=lambda: outcome_handler("paper"))
    scis_btn = Button(root, text="Scissors", width=15, command=lambda: outcome_handler("scissors"))

    rock_btn.grid(row=4, sticky=W, padx=5, pady=5)
    paper_btn.grid(row=4, sticky=N, pady=5)
    scis_btn.grid(row=4, sticky=E, padx=5,pady=5)

    # Sample for test
    Label(root).grid(row=5)

    root.mainloop()


# Create Heading
h = Label(parent,text = "Rock, Paper & Scissor",font = ("Helevetica",20,'bold'),bg = "light pink")
h.pack(pady = 80)

# Start button
start_btn = Button(parent,text = "Start Game",bg = "lightskyblue",activebackground = "yellow",relief = "raised",command = start)
start_btn.pack(pady = 10)


parent.mainloop()



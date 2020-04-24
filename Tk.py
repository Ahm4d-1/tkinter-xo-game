from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import *
from random import random, randint

# start tkinter
root = Tk()
root.title("XO Game by Ahmed Ibrahim")

# globals
player_turn = 1
counter = 1
player_list = []         # this list will contain IDs for the buttons' positions for player
ai_list = []             # this list will contain IDs for the buttons' positions for AI
player_letter = ' '
ai_letter = ' '

# buttons positions and attributes
button1 = Button(root, text=' ', command=lambda: button_click(1))
button1.grid(row=0, column=0, sticky='snew', ipadx=80, ipady=80)

button2 = Button(root, text=' ', command=lambda: button_click(2))
button2.grid(row=0, column=1, sticky='snew', ipadx=80, ipady=80)

button3 = Button(root, text=' ', command=lambda: button_click(3))
button3.grid(row=0, column=2, sticky='snew', ipadx=80, ipady=80)

button4 = Button(root, text=' ', command=lambda: button_click(4))
button4.grid(row=1, column=0, sticky='snew', ipadx=80, ipady=80)

button5 = Button(root, text=' ', command=lambda: button_click(5))
button5.grid(row=1, column=1, sticky='snew', ipadx=80, ipady=80)

button6 = Button(root, text=' ', command=lambda: button_click(6))
button6.grid(row=1, column=2, sticky='snew', ipadx=80, ipady=80)

button7 = Button(root, text=' ', command=lambda: button_click(7))
button7.grid(row=2, column=0, sticky='snew', ipadx=80, ipady=80)

button8 = Button(root, text=' ', command=lambda: button_click(8))
button8.grid(row=2, column=1, sticky='snew', ipadx=80, ipady=80)

button9 = Button(root, text=' ', command=lambda: button_click(9))
button9.grid(row=2, column=2, sticky='snew', ipadx=80, ipady=80)


# decides who plays first randomly by returning a boolean expression to player_turn variable
def player_goes_first():
    # random() will give you a value between 1 and 0
    random_value = random()

    # True means player will go first
    if random_value > 0.5:
        return True
    return False


# for the player to decide which letter to play with
def select_letter():
    global player_letter
    global ai_letter

    choice = askyesno("Most people prefer 'X' as their letter", message="Do you prefer to play with X ?")
    print(choice)

    if choice == True:  # that means they prefer letter X
        player_letter = 'X'
        ai_letter = 'O'
    else:
        player_letter = 'O'
        ai_letter = 'X'


# for switching turns on clicks
def button_click(id):
    global player_turn
    global player_letter
    global counter

    if player_turn == 1:
        set_board(id, player_letter, 'lightblue')
        player_list.append(id)
        check_winner()
        check_draw()
        player_turn = 0
        counter += 1
        print("Player List: {}".format(player_list))
    ai_turn()


# intelligently chooses position for AI
def ai_turn():
    global ai_letter
    global player_turn
    global counter

    played = False   # to make sure ai does not play twice
    valid = False
    counter += 1
    while not valid:
        if not played:
            # winning cases

            # rows
            if (1 in ai_list) and (2 in ai_list) and (3 not in player_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'orange')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (2 not in player_list) and (3 in ai_list):
                if 2 not in ai_list:
                    set_board(2, ai_letter, 'orange')
                    ai_list.append(2)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (2 in ai_list) and (3 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'orange')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (4 in ai_list) and (5 in ai_list) and (6 not in player_list):
                if 6 not in ai_list:
                    set_board(6, ai_letter, 'orange')
                    ai_list.append(6)
                    player_turn = 1
                    valid = True
                    played = True
            elif (4 in ai_list) and (5 not in player_list) and (6 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'orange')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (4 not in player_list) and (5 in ai_list) and (6 in ai_list):
                if 4 not in ai_list:
                    set_board(4, ai_letter, 'orange')
                    ai_list.append(4)
                    player_turn = 1
                    valid = True
                    played = True

            elif (7 in ai_list) and (8 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'orange')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (7 in ai_list) and (8 not in player_list) and (9 in ai_list):
                if 8 not in ai_list:
                    set_board(8, ai_letter, 'orange')
                    ai_list.append(8)
                    player_turn = 1
                    valid = True
                    played = True
            elif (7 not in player_list) and (8 in ai_list) and (9 in ai_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'orange')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True


            # columns
            elif (1 in ai_list) and (4 in ai_list) and (7 not in player_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'orange')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (4 not in player_list) and (7 in ai_list):
                if 4 not in ai_list:
                    set_board(4, ai_letter, 'orange')
                    ai_list.append(4)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (4 in ai_list) and (7 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'orange')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (2 in ai_list) and (5 in ai_list) and (8 not in player_list):
                if 8 not in ai_list:
                    set_board(8, ai_letter, 'orange')
                    ai_list.append(8)
                    player_turn = 1
                    valid = True
                    played = True
            elif (2 in ai_list) and (5 not in player_list) and (8 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'orange')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (2 not in player_list) and (5 in ai_list) and (8 in ai_list):
                if 2 not in ai_list:
                    set_board(2, ai_letter, 'orange')
                    ai_list.append(2)
                    player_turn = 1
                    valid = True
                    played = True

            elif (3 in ai_list) and (6 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'orange')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 in ai_list) and (6 not in player_list) and (9 in ai_list):
                if 6 not in ai_list:
                    set_board(6, ai_letter, 'orange')
                    ai_list.append(6)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 not in player_list) and (6 in ai_list) and (9 in ai_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'orange')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True


            # diagonals
            elif (1 in ai_list) and (5 in ai_list) and (9 not in player_list):
                if 9 not in ai_list:
                    set_board(9, ai_letter, 'orange')
                    ai_list.append(9)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 in ai_list) and (5 not in player_list) and (9 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'orange')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (1 not in player_list) and (5 in ai_list) and (9 in ai_list):
                if 1 not in ai_list:
                    set_board(1, ai_letter, 'orange')
                    ai_list.append(1)
                    player_turn = 1
                    valid = True
                    played = True

            elif (3 in ai_list) and (5 in ai_list) and (7 not in player_list):
                if 7 not in ai_list:
                    set_board(7, ai_letter, 'orange')
                    ai_list.append(7)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 in ai_list) and (5 not in player_list) and (7 in ai_list):
                if 5 not in ai_list:
                    set_board(5, ai_letter, 'orange')
                    ai_list.append(5)
                    player_turn = 1
                    valid = True
                    played = True
            elif (3 not in player_list) and (5 in ai_list) and (7 in ai_list):
                if 3 not in ai_list:
                    set_board(3, ai_letter, 'orange')
                    ai_list.append(3)
                    player_turn = 1
                    valid = True
                    played = True
            else:

                # blocking player's win
                # rows
                if (1 not in ai_list) and (2 in player_list) and (3 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'orange')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (2 not in ai_list) and (3 in player_list):
                    if 2 not in player_list:
                        set_board(2, ai_letter, 'orange')
                        ai_list.append(2)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (2 in player_list) and (3 not in ai_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'orange')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True

                elif (4 not in ai_list) and (5 in player_list) and (6 in player_list):
                    if 4 not in player_list:
                        set_board(4, ai_letter, 'orange')
                        ai_list.append(4)
                        player_turn = 1
                        valid = True
                        played = True
                elif (4 in player_list) and (5 not in ai_list) and (6 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'orange')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (4 in player_list) and (5 in player_list) and (6 not in ai_list):
                    if 6 not in player_list:
                        set_board(3, ai_letter, 'orange')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True

                elif (7 not in ai_list) and (8 in player_list) and (9 in player_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'orange')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True
                elif (7 in player_list) and (8 not in ai_list) and (9 in player_list):
                    if 8 not in player_list:
                        set_board(8, ai_letter, 'orange')
                        ai_list.append(8)
                        player_turn = 1
                        valid = True
                        played = True
                elif (7 in player_list) and (8 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'orange')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True


                # columns

                elif (1 not in ai_list) and (4 in player_list) and (7 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'orange')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (4 not in ai_list) and (7 in player_list):
                    if 4 not in player_list:
                        set_board(4, ai_letter, 'orange')
                        ai_list.append(4)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (4 in player_list) and (7 not in ai_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'orange')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True

                elif (2 not in ai_list) and (5 in player_list) and (8 in player_list):
                    if 2 not in player_list:
                        set_board(2, ai_letter, 'orange')
                        ai_list.append(2)
                        player_turn = 1
                        valid = True
                        played = True
                elif (2 in player_list) and (5 not in ai_list) and (8 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'orange')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (2 in player_list) and (5 in player_list) and (8 not in ai_list):
                    if 8 not in player_list:
                        set_board(8, ai_letter, 'orange')
                        ai_list.append(8)
                        player_turn = 1
                        valid = True
                        played = True

                elif (3 not in ai_list) and (6 in player_list) and (9 in player_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'orange')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (6 not in ai_list) and (9 in player_list):
                    if 6 not in player_list:
                        set_board(6, ai_letter, 'orange')
                        ai_list.append(6)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (6 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'orange')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True


                # diagonals
                elif (1 not in ai_list) and (5 in player_list) and (9 in player_list):
                    if 1 not in player_list:
                        set_board(1, ai_letter, 'orange')
                        ai_list.append(1)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (5 not in ai_list) and (9 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'orange')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (1 in player_list) and (5 in player_list) and (9 not in ai_list):
                    if 9 not in player_list:
                        set_board(9, ai_letter, 'orange')
                        ai_list.append(9)
                        player_turn = 1
                        valid = True
                        played = True

                elif (3 not in ai_list) and (5 in player_list) and (7 in player_list):
                    if 3 not in player_list:
                        set_board(3, ai_letter, 'orange')
                        ai_list.append(3)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (5 not in ai_list) and (7 in player_list):
                    if 5 not in player_list:
                        set_board(5, ai_letter, 'orange')
                        ai_list.append(5)
                        player_turn = 1
                        valid = True
                        played = True
                elif (3 in player_list) and (5 in player_list) and (7 not in ai_list):
                    if 7 not in player_list:
                        set_board(7, ai_letter, 'orange')
                        ai_list.append(7)
                        player_turn = 1
                        valid = True
                        played = True

        check_winner()
        check_draw()

        # if none of the above intelligent positions are available, then choose randomly
        if not played:
            ai_answer = randint(1, 9)
            if (ai_answer not in player_list) and (ai_answer not in ai_list):
                set_board(ai_answer, ai_letter, 'orange')
                ai_list.append(ai_answer)
                player_turn = 1
                check_winner()
                check_draw()
                print("AI List: {}".format(ai_list))
                return


# changes the interface according to the flow of the game
def set_board(id, letter, color):

    # argument id indicates the position, as in a matrix
    if id == 1:
        button1.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 2:
        button2.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 3:
        button3.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 4:
        button4.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 5:
        button5.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 6:
        button6.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 7:
        button7.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 8:
        button8.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)
    elif id == 9:
        button9.config(text=letter, state='disabled', font=('arial', 13, 'bold'), bg=color)


# checks if player or AI won
def check_winner():
    player_won = False
    ai_won = False

    if (1 in player_list) and (2 in player_list) and (3 in player_list):
        player_won = True
    if (1 in ai_list) and (2 in ai_list) and (3 in ai_list):
        ai_won = True

    if (4 in player_list) and (5 in player_list) and (6 in player_list):
        player_won = True
    if (4 in ai_list) and (5 in ai_list) and (6 in ai_list):
        ai_won = True

    if (7 in player_list) and (8 in player_list) and (9 in player_list):
        player_won = True
    if (7 in ai_list) and (8 in ai_list) and (9 in ai_list):
        ai_won = True

    if (1 in player_list) and (4 in player_list) and (7 in player_list):
        player_won = True
    if (1 in ai_list) and (4 in ai_list) and (7 in ai_list):
        ai_won = True

    if (2 in player_list) and (5 in player_list) and (8 in player_list):
        player_won = True
    if (2 in ai_list) and (5 in ai_list) and (8 in ai_list):
        ai_won = True

    if (3 in player_list) and (6 in player_list) and (9 in player_list):
        player_won = True
    if (3 in ai_list) and (6 in ai_list) and (9 in ai_list):
        ai_won = True

    if (1 in player_list) and (5 in player_list) and (9 in player_list):
        player_won = True
    if (1 in ai_list) and (5 in ai_list) and (9 in ai_list):
        ai_won = True

    if (3 in player_list) and (5 in player_list) and (7 in player_list):
        player_won = True
    if (3 in ai_list) and (5 in ai_list) and (7 in ai_list):
        ai_won = True

    if player_won:
        messagebox.showinfo(title="Congrats.. You Won !", message="You are the winner", commad=root.quit())
    elif ai_won:
        messagebox.showinfo(title="Good Luck Next Time..", message="AI is the winner", command=root.quit())


# checks if draw occurred
def check_draw():
    global counter

    # when 9 turns have passed and nobody won, it's a draw
    if counter == 10:
        messagebox.showinfo(title="Draw Game", message="Game ended with a Draw", command=root.quit())


# first thing on the program, to set player's letter, and decide who plays first
def main():
    select_letter()
    if player_goes_first():
        messagebox.showinfo(title="first to play will randomly be selected!",
                            message="You are first to play ! Go ahead")
    else:
        messagebox.showinfo(title="first to play will randomly be selected!", message="AI will go first, you're Next")
        ai_turn()


main()
root.mainloop()

#!/usr/bin/env python3

import tkinter as tk
import random, os
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.ttk as ttk

import tkinter.font as tkFont


class Data:
    people = []
    winner = []
    x = 0

counter = int

def empty():
    pass


def decide(n, repeat):
    i = random.randrange(n)
    # winner_name = Data.people[i]
    # selected_winner = f"And the winner is: {winner_name}"
    winner_announcement["text"] = "And the winner is:"
    output_label["text"] = Data.people[i]
    if Data.x < repeat:
        root.after(50, decide, n, repeat)
        Data.x += 1
    else:
        Data.x = 0


def run():
    n = len(Data.people)
    if n >= 1:
        decide(n, 100)
    else:
        clear_output_labels()
        output_label["text"] = "You need at least 1 person."


def run_event(event):
    run()


def add():
    new_person = add_person_text.get()
    if new_person != "":
        Data.people.append(new_person)
        people_listbox.insert("end", new_person)
    add_person_text.set("")

def add_event(event):
    add()

def add_winner():
    winner_person = output_label["text"]
    if winner_person != "":
        Data.winner.append(winner_person)
        winner_listbox.insert("end", winner_person)
        i = people_listbox.get(0, "end").index(winner_person)
        Data.people.pop(i)
        people_listbox.delete(i)
        n = len(Data.winner)
        winner = f"The number of winners: {n}"
        counter_label["text"] = winner
    #add_person_text.set("")

def add_winner_event(event):
    add_winner()

def save_to_file():
    path = asksaveasfilename(defaultextension=".txt")
    with open(path, "w", encoding="utf-8") as lines:
        for person in Data.winner:
            lines.writelines(person)
            lines.write("\n")


def load_from_file():
    path = askopenfilename()
    with open(path, "r", encoding="utf-8") as lines:
        Data.people.extend(lines)

    for person in Data.people:
        people_listbox.insert("end", person)

    people_label["text"] = "Customers:"


def remove():
    try:
        i = people_listbox.curselection()[0]
        Data.people.pop(i)
        people_listbox.delete(i)
        clear_output_labels()
    except IndexError:
        clear_output_labels()
        output_label["text"] = "You haven't selected anyone."


def remove_event(event):
    remove()

def remove_winner():
    try:
        i = winner_listbox.curselection()[0]
        Data.winner.pop(i)
        winner_listbox.delete(i)
        clear_output_labels()
    except IndexError:
        clear_output_labels()
        output_label["text"] = "You haven't selected anyone."

def remove_winner_event(event):
    remove_winner()

def clear():
    Data.people = []
    people_listbox.delete(0, "end")
    clear_output_labels()


def clear_output_labels():
    output_label["text"] = ""
    arrow_label["text"] = ""
    people_label["text"] = "Customers:"


bgc = ""
WT_BLUE = "#0a47ed"
WT_CYAN = "#00d1d9"
WT_PINK = "#e661b2"
WT_YELLOW = "#ffe330"
WT_RUBY = "#af3b6e"



root = tk.Tk()
root.title("Shell Customer Raffler")
width = 1000
height = 720
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.config(bg=WT_CYAN)

header = tk.Label(root, text="WT Winner Picker", font=("Roboto", 44), padx=10, pady=10, bg=WT_CYAN, fg=WT_RUBY,
                  highlightthickness=0, highlightbackground="red")
header.pack()

# img_path = 'C:\\Users\\jiri.pillar\\PycharmProjects\\shell_raffler\\dist\\WT_CYAN_LOGO.gif'
img_path = os.path.dirname(os.path.abspath(__file__)) + "/WT_CYAN_LOGO.GIF"
img = tk.PhotoImage(file=img_path)
img_size = (310, 233)


logo = tk.Canvas(width=img_size[0], height=img_size[1], bg=WT_CYAN, highlightthickness=0, bd=0)
logo.create_image(img_size[0] / 2, img_size[1] / 2, image=img, anchor=tk.CENTER)
logo.pack()


left_frame = tk.Frame(root, bg=WT_CYAN, highlightthickness=0, highlightbackground="red")
left_frame.pack(side="left", padx=30, pady=30, fill="both")

people_label = tk.Label(left_frame, text="Customers:", bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
people_label.pack()

people_listbox = tk.Listbox(left_frame, bg="white",highlightthickness=0, highlightbackground="red")
people_listbox.pack(side="left", fill="y")
people_listbox.bind("<BackSpace>", remove_event)

## --------------------------------------------------------------------------------------------------------------------

winner_frame = tk.Frame(root, bg=WT_CYAN, highlightthickness=0, highlightbackground="red")
winner_frame.pack(side="right", padx=30, pady=30, fill="both")

counter_label = tk.Label(winner_frame, font=("Roboto", 10), bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
counter_label.pack()

winner_label = tk.Label(winner_frame,  text="winners:", bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
winner_label.pack()

winner_listbox = tk.Listbox(winner_frame)
winner_listbox.pack(side="right", fill="y")
winner_listbox.bind("<BackSpace>", remove_event)

# add_winner_person_text = tk.StringVar()
# add_winner_entry = tk.Entry(winner_frame, textvariable=add_winner_person_text, width=100)
# add_winner_entry.pack()
# add_winner_entry.bind("<Return>", add_winner_event)

## --------------------------------------------------------------------------------------------------------------------

right_frame = tk.Frame(root, bg=WT_CYAN,highlightthickness=0, highlightbackground="blue")
right_frame.pack(side="left", padx=30, pady=30, fill="both")

add_person_text = tk.StringVar()
add_person_entry = tk.Entry(right_frame, textvariable=add_person_text, width=100, bg="white",highlightthickness=0, highlightbackground="red")
add_person_entry.pack()
add_person_entry.bind("<Return>", add_event)

list_buttons = tk.Frame(right_frame, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
list_buttons.pack()

add_person_button = tk.Button(list_buttons, text="ADD", command=add, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
add_person_button.pack(side="left")

remove_person_button = tk.Button(list_buttons, text="REMOVE", command=remove, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
remove_person_button.pack(side="left")

load_from_file_button = tk.Button(list_buttons, text="LOAD FROM FILE", command=load_from_file, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
load_from_file_button.pack(side="right")

save_to_file_button = tk.Button(list_buttons, text="SAVE TO FILE", command=save_to_file, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
save_to_file_button.pack(side="right")

add_winner_person_button = tk.Button(list_buttons, text="ADD WINNER", command=add_winner, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
add_winner_person_button.pack(side="left")

remove_winner_person_button = tk.Button(list_buttons, text="REMOVE WINNER", command=remove_winner, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
remove_winner_person_button.pack(side="left")

output_frame = tk.Frame(right_frame, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
output_frame.pack(pady=80)

winner_announcement = tk.Label(output_frame, font=("Roboto", 15), bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
winner_announcement.pack()

output_label = tk.Label(output_frame, font=("Roboto", 15), bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
output_label.pack()

arrow_label = tk.Label(output_frame, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
arrow_label.pack()

buttons_frame = tk.Frame(right_frame, bg=WT_CYAN,highlightthickness=0, highlightbackground="red")
buttons_frame.pack(side="bottom")

credits = tk.Label(buttons_frame, text="coded by @Jiri", bg=WT_CYAN)
credits.pack(side="right", padx=50)

quit_button = tk.Button(buttons_frame, text="QUIT", command=root.destroy, bg=WT_CYAN)
quit_button.pack(side="right")

clear_button = tk.Button(buttons_frame, text="CLEAR", command=clear, bg=WT_CYAN)
clear_button.pack(side="right")

run_button = tk.Button(buttons_frame, text="RUN", command=run, bg=WT_CYAN)
run_button.pack(side="left")

root.lift()
root.bind("<Command-r>", run_event)
root.mainloop()

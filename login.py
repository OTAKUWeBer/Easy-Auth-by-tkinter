from sign_up import info
from tkinter import *


window = Tk()

def submit():
    username = user.get()
    psw = password.get()
    if username in info:
        if psw == info[username]:
            print("Logged in")
        else:
            print("Wrong password. Please try again.")
    else:
        print("Username not found.")


            
submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

def delete():
    user.delete(0, END)
    password.delete(0, END)
    
def backspace():
    password.delete(len(password.get()) - 1, END)

user = Entry(window,
              font=("Arial", 30),
              fg="#00FF00",
              bg="black")

password = Entry(window,
                 font=("Arial", 30),
                 fg="#00FF00",
                 bg="black",
                 show="*")

user.pack()
password.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.title("Login")
window.config(background="white")

window.mainloop()

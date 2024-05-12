from tkinter import *

window = Tk()

info = {}

def submit():
    username = user.get()
    psw = password.get()
    print("Account created as", username, "name")
    info[username] = psw
    
submit_button = Button(window, text="submit", command = submit)
submit_button.pack(side=RIGHT)
    
def delete():
    user.delete(0,END)
    password.delete(0,END)
    
    
def backspace():
    password.delete(len(password.get())-1,END)


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


delete_button = Button(window, text="delete", command = delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command = backspace)
backspace_button.pack(side=RIGHT)



window.title("Create Account")
window.config(background="white")

window.mainloop()
import os
import re
import tkinter
from asyncio import exceptions
from tkinter import messagebox

import pyperclip

import model
from tkinter import *


def main_window():
    def generate_password():
        psw: str = model.PasswordGenerator.GenerateRandomPassword(5, 5, 5)
        entry_text.set(psw)
        pyperclip.copy(psw)
        spam = pyperclip.paste()

    def check(s):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(pat, s):
            return True
        else:
            return False

    def write_file():
        if not check(input_email.get()):
            messagebox.showinfo("Email Validated", "Email Not Validated")
            return
        if messagebox.askyesno('File Writing', 'Do you want to write your password?'):
            if len(input_username.get()) <= 0 or len(input_password.get()) <= 0:
                messagebox.showinfo("Password Manager", "Please enter your password and username")
            else:
                try:
                    if not os.path.exists("pwd.txt"):
                        with open("pwd.txt", "w") as file:
                            file.write("username, email, pswd\n")
                    with open("pwd.txt", "a") as file:
                        file.write(f"{input_username.get()}, {input_email.get()}, {input_password.get()}\n")
                except IOError:
                    messagebox.showinfo("Error", "File Writing Failed")

    root = Tk()
    entry_text = tkinter.StringVar()
    root.geometry('500x500')
    root.title('Password Manager')
    root.resizable(False, False)
    label = Label(root, text='Password', font=('Arial', 16))
    label.grid(column=1, row=0)

    input_label_username = Label(root, text='Username', font=('Arial', 10))
    input_label_username.grid(column=0, row=1)
    input_username = Entry(root, font=('Arial', 10))
    input_username.grid(column=1, row=1)
    input_label_email = Label(root, text='Email', font=('Arial', 10))
    input_label_email.grid(column=0, row=2)
    input_email = Entry(root, font=('Arial', 10))
    input_email.grid(column=1, row=2)

    label_password = Label(root, text='Password', font=('Arial', 10))
    label_password.grid(column=0, row=4)
    input_password = Entry(root, font=('Arial', 10), textvariable=entry_text)
    input_password.grid(column=1, row=4)
    button_generate_password = Button(root, text='Generate Password', font=('Arial', 10), command=generate_password)
    button_generate_password.grid(column=2, row=4)
    button_confirm_password = Button(root, text='Save', font=('Arial', 10), command=write_file)
    button_confirm_password.grid(column=1, row=6)
    root.mainloop()


def main():
    main_window()


if __name__ == '__main__':
    main()

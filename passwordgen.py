import random
from random import choice
import PySimpleGUI as sg

#takes in the number imputted by the user and combines that number of words together capitalizing random letters
def combine_words():
    global password
    for i in range(int(password_length)):
        password += random.choice(wordList)
    return password

#function to randomly capitalize letters in the password
def random_capital():
    global password
    for i in range(len(password)):
        if random.randint(0, 1) == 1:
            password = password[:i] + password[i].upper() + password[i+1:]
    return password


#function to add a special character to the password, replaces characters witha  special character but only once
def special_character_replace():
    global password
    for letters in password:
        if letters == "a":
            password == password.replace("a", "@", 1)
        if letters == "o":
            password = password.replace("o", "0", 1)
        if letters == "s":
            password = password.replace("s", "$", 1)
        if letters == "e":
            password = password.replace("e", "3", 1)
        if letters == "l":
            password = password.replace("l", "1", 1)
    return password

#adds a number to the end of the password
def number_add():
    global password
    number = random.randint(0, 9)
    password = password + str(number)
    return password
        

#main function
password = ""   

# read the words from the file     
wordList = open("words.txt", "r").read().splitlines() 

sg.theme('DarkPurple6')  # color theme for window

# layout of the window
layout = [  [sg.Text('Password Generator')],
            [sg.Text('Number of words in password'), sg.InputText()],
            [sg.Text('Special Characters?'), sg.Checkbox('Yes', default=False)],
            [sg.Text('Number at end?'), sg.Checkbox('Yes', default=False)],
            [sg.Submit('Generate Password'), sg.Button('Cancel')] ]

window = sg.Window('Password Generator', layout, margins=(8, 8))

# event loop to process "events" and get the "values" of the inputs. Generates Password in popup window
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Generate Password':
        password_length = values[0]
        combine_words()
        random_capital()
        if values[1] == True:
            special_character_replace()
        if values[2] == True:
            number_add()
        sg.popup('Your password is: ', password)
        password = ""
    




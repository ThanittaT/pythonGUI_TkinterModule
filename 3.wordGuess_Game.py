from tkinter import *
import random

ws = Tk()
ws.title('AnitaCoffeeShop-Game')
ws.geometry('600x400')
ws.config(bg='#5671A6')

ranNum = random.randint(0, 10)
chance = 5
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_input = var.get()
    if chance > 0:
        if usr_input == ranNum:
            msg = f'You won! {ranNum} is the right answer.'
        elif usr_input > ranNum:
            chance -= 1
            msg = f'{usr_input} is greater. You have {chance} attempt left.'
        elif usr_input < ranNum:
            chance -= 1
            msg = f'{usr_input} is smaller. You have {chance} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


Label(
    ws,
    text='Welcome to "Number Guessing" Game ! \n \n(Hint: Please picking number from...0 to...15.)',
    font=('sans-serif', 15, 'bold'),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#F27D16'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('sans-serif', 18)
).pack(pady=(50, 10))

Button(
    ws,
    text='Submit Guess',
    font=('sans-serif', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#5671A6',
    font=('sans-serif', 14)
).pack(pady=(20,0))


ws.mainloop()
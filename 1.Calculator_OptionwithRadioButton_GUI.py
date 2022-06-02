import tkinter as tk


def calculate():
    if valRadio.get() == 1:
        res = int(e1.get())+int(e2.get())
    elif valRadio.get() == 2:
        res = int(e1.get()) - int(e2.get())
    elif valRadio.get() == 3:
        res = int(e1.get()) * int(e2.get())
    elif valRadio.get() == 4:
        res = int(e1.get()) / int(e2.get())
    else:
        res = "Check radio button"
    myText.set(res)

root = tk.Tk()
root.title("AnitaCoffee-Shop Calculator")


valRadio = tk.IntVar()
myText = tk.StringVar()
e1 = tk.StringVar()
e2 = tk.StringVar()

tk.Label(root, text="""This is GUI-Simple Calculator @designThanittaT""",font=('Arial',18,'bold')).grid(row =2, column = 0)
tk.Label(root, text="First number: ").grid(row =4, column = 0)
tk.Label(root, text="Second number: ").grid(row =5, column = 0)

tk.Label(text="The result is: ", textvariable=myText).grid(row=14, column=0)


tk.Entry(textvariable= e1).grid(row = 4, column = 1)
tk.Entry(textvariable= e2).grid(row = 5, column = 1)

r1 = tk.Radiobutton(text="Add(+)", variable=valRadio, value =1).grid(row=7, column=0)
r2 = tk.Radiobutton(text="Subtract(-)", variable=valRadio, value =2).grid(row=7, column=1)
r3 = tk.Radiobutton(text="Multiply(*)", variable=valRadio, value =3).grid(row=8, column=0)
r4 = tk.Radiobutton(text="Divide(/)", variable=valRadio, value =4).grid(row=8, column=1)

b = tk.Button(text='Calculate', command=calculate).grid(row =14, column=3)

root.mainloop()
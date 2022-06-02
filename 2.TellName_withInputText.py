from tkinter import *


class customdialog(Toplevel):
    def __init__(self, parent, prompt):
        Toplevel.__init__(self, parent)

        self.var = StringVar()

        self.label = Label(self, text=prompt)
        self.entry = Entry(self, textvariable=self.var)
        self.ok_button = Button(self, text="OK", command=self.on_Ok)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x")
        self.ok_button.pack(side="right")

        self.entry.bind("<Return>", self.on_Ok)

    def on_Ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.button = Button(self, text="Tell us about yourself!", command=self.on_Button)
        self.label = Label(self, text="", width=20)
        self.button.pack(padx=8, pady=8)
        self.label.pack(side="bottom", fill="both", expand=True)

    def on_Button(self):
        string = customdialog(self, "Please tell me your nickname:").show()
        self.label.configure(text="Your nickname is: \n" + string)


if __name__ == "__main__":
    ws = Tk()
    ws.title("AnitaCoffee @designThanittaT")
    ws.geometry("300x300")
    example(ws).pack(fill="both", expand=True)
    ws.mainloop()
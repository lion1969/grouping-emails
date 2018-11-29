from txt_bot import TextBot
from tkinter import *

jake = TextBot('...')
print(jake)
print(jake.output)
#jake.input = "hi"
jake.answer_the_questio()
print(jake.output)

root = Tk()
txt = Text(root, width=150, height=50, font='Arial 12')
txt.pack()
ary = txt.get('1.0', END)
print("TXT.get():\n", ary)

txt.insert(END, jake.output)
root.mainloop()
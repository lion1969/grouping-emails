from tkinter import *
import tkinter.filedialog as tkFileDialog


def doQuit():
    global root
    root.destroy()


def loadFile():
    fn = tkFileDialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    print('FileOpened:', fn)
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def saveFile():
    fn = tkFileDialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

def doProc():
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', 'doProc done.\n'
                          'what tac whatt')


root = Tk()
panelFrame = Frame(root, height=44, bg='light gray' )
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load', command = loadFile)
saveBtn = Button(panelFrame, text='Save', command = saveFile)
quitBtn = Button(panelFrame, text='Quit', command = doQuit)
procBtn = Button(panelFrame, text='Proc', command = doProc)

'''
loadBtn.bind("<Button-1>", loadFile)
saveBtn.bind("<Button-1>", saveFile)
quitBtn.bind("<Button-1>", doQuit)
procBtn.bind("<Button-1>", doProc)
'''

loadBtn.place(x=2, y=2, width=48, height=40)
saveBtn.place(x=52, y=2, width=48, height=40)
quitBtn.place(x=102, y=2, width=48, height=40)
procBtn.place(x=252, y=2, width=48, height=40)


root.mainloop()
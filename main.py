from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = Tk()
root.title("Text Editor")
file_path = ""

def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename()
    with open(path, 'r') as file:
        txt = file.read()
        editor.delete("1.0", END)
        editor.insert("1.0", txt)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename()
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

root.config(menu=menu_bar)

editor = Text(root, font=15)
editor.pack()

root.mainloop()


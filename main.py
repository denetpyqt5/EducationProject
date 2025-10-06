from tkinter import *
import sqlite3

def click1():
    cur.execute(f'''INSERT INTO tasks VALUES ('{entr1.get()}','{entr2.get()}','{entr3.get()}')''')
    entr1.delete(first = 0,last = END)
    entr2.delete(first = 0,last = END)
    entr3.delete(first = 0,last = END)
    db.commit()

root = Tk()
db = sqlite3.connect('data.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tasks (info TEXT,url TEXT,ad TEXT)''')
db.commit()
root.geometry("900x600")
root.title("EduHelper")
root.resizable(height = False,width = False)
root.iconbitmap('icon.ico')

entr1 = Entry()
entr1.pack()

entr2 = Entry()
entr2.pack()

entr3 = Entry()
entr3.pack()

btn1 = Button(text = "commit",command = click1)
btn1.pack()




root.mainloop()
db.close()
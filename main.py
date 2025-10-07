from tkinter import *
import sqlite3
from datetime import datetime,timedelta

def click1():
    cur.execute(f'''INSERT INTO tasks VALUES ('{entr1.get()}','{entr2.get()}','{entr3.get()}','{str(datetime.now() + timedelta(days = 1)).split(" ")[0]}','{str(datetime.now() + timedelta(weeks = 1)).split(" ")[0]}','{str(datetime.now() + timedelta(days = 30)).split(" ")[0]}','{str(datetime.now() + timedelta(days = 90)).split(" ")[0]}')''')
    entr1.delete(first = 0,last = END)
    entr2.delete(first = 0,last = END)
    entr3.delete(first = 0,last = END)
    db.commit()

root = Tk()
db = sqlite3.connect('data.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tasks (info TEXT,url TEXT,ad TEXT,p1 TEXT,p2 TEXT,p3 TEXT,p4 TEXT)''')
db.commit()
root.geometry("900x600")
root.title("EduHelper")
root.resizable(height = False,width = False)
root.iconbitmap('icon.ico')

entr1 = Entry(root)
lbl1 = Label(root,text = "Информация о изученном материале:")
lbl1.pack()
entr1.pack()

entr2 = Entry(root)
lbl2 = Label(root,text = "Ссылка на ресурс:")
lbl2.pack()
entr2.pack()

entr3 = Entry(root)
lbl3 = Label(root,text = "Заметки:")
lbl3.pack()
entr3.pack()

btn1 = Button(root,text = "Внести данные",command = click1)
btn1.pack()



cur.execute(f'''SELECT info FROM tasks WHERE p1 = "{str(datetime.now()).split(" ")[0]}" OR p2 = "{str(datetime.now()).split(" ")[0]}" OR p3 = "{str(datetime.now() ).split(" ")[0]}" OR p4 = "{str(datetime.now() ).split(" ")[0]}" ''')
text_db = cur.fetchall()
lbl4 = Label(root,width = 50,height = 25,text = text_db,background =  "Gray")
lbl4.pack()

root.mainloop()
db.close()
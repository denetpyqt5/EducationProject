from tkinter import *
import sqlite3
from datetime import datetime,timedelta

def click1():
    cur.execute(f'''INSERT INTO tasks VALUES ('{entr1.get()}','{entr2.get()}','{entr3.get()}','{str(datetime.now() + timedelta(days = 1)).split(" ")[0]}','{str(datetime.now() + timedelta(weeks = 1)).split(" ")[0]}','{str(datetime.now() + timedelta(days = 30)).split(" ")[0]}','{str(datetime.now() + timedelta(days = 90)).split(" ")[0]}')''')
    entr1.delete(first = 0,last = END)
    entr2.delete(first = 0,last = END)
    entr3.delete(first = 0,last = END)
    db.commit()

def click2():

    cur.execute(f'''SELECT info,url,ad FROM tasks WHERE info = "{list1.get(list1.curselection())}"''')
    txt = cur.fetchall()
    lbl4.config(text = txt[0][0])
    lbl5.config(text=txt[0][1])
    lbl6.config(text=txt[0][2])

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
lbl1.pack(anchor = "w")
entr1.pack(anchor = "w")

entr2 = Entry(root)
lbl2 = Label(root,text = "Ссылка на ресурс:")
lbl2.pack(anchor = "w")
entr2.pack(anchor = "w")

entr3 = Entry(root)
lbl3 = Label(root,text = "Заметки:")
lbl3.pack(anchor = "w")
entr3.pack(anchor = "w")

btn1 = Button(root,text = "Внести данные",command = click1)
btn1.pack(anchor = "w")

list1 = Listbox(root)
list1.pack(anchor = "ne")
btn2 = Button(root,text = "Получить информацию",command = click2)
btn2.pack(anchor = "ne")

lbl4 = Label(root)
lbl5 = Label(root)
lbl6 = Label(root)
lbl4.pack(anchor = "c")
lbl5.pack(anchor = "c")
lbl6.pack(anchor = "c")

cur.execute(f'''SELECT info FROM tasks WHERE p1 = "{str(datetime.now()).split(" ")[0]}" OR p2 = "{str(datetime.now()).split(" ")[0]}" OR p3 = "{str(datetime.now()).split(" ")[0]}" OR p4 = "{str(datetime.now()).split(" ")[0]}" ''')
text_db = cur.fetchall()

k = 0
for i in text_db:
    list1.insert(k,i[0])
    k+=1

root.mainloop()
db.close()
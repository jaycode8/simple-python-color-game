

#------------------python color game-----------------------------
#--------------------------------- Jaycode8 -----------------------------

from tkinter import *
from tkinter.messagebox import *

def finall():
    global count
    showinfo('COLOUR GAME','GAME OVER \n YOUR SCORE IS '+str(count))

def check_4():
    global count
    global bt_5
    if e.get().lower() == '':
        showerror('COLOUR GAME', 'BLANK SPACE NOT ALLOWED ')
    else:
        if e.get().lower() == 'black':
            showinfo('COLOUR GAME', 'CORRECT !')
            count = count + 1
            e.delete(0, END)
            bt_5.destroy()
            bt_6 = Button(text='NEXT', font=('verdana', 15), bd=0)
            bt_6.place(x=300, y=300)
            finall()

        else:
            showinfo('COLOUR GAME', 'WRONG ! THE COLOUR IS BLACK')

def check_3():
    global count
    global bt_5
    if e.get().lower() == '':
        showerror('COLOUR GAME', 'BLANK SPACE NOT ALLOWED ')
    else:
        if e.get().lower() == 'blue':
            showinfo('COLOUR GAME', 'CORRECT !')
            count = count + 1
            e.delete(0, END)
            bt_4.destroy()
            lb_2.config(bg='black')
            bt_5 = Button(text='NEXT', font=('verdana', 15), bd=0, command=check_4)
            bt_5.place(x=300, y=300)

        else:
            showinfo('COLOUR GAME', 'WRONG ! THE COLOUR IS BLUE')

def check_2():
    global count
    global bt_4
    if e.get().lower() == '':
        showerror('COLOUR GAME', 'BLANK SPACE NOT ALLOWED ')
    else:
        if e.get().lower() == 'red':
            showinfo('COLOUR GAME', 'CORRECT !')
            count = count + 1
            e.delete(0, END)
            bt_4.destroy()
            lb_2.config(bg='blue')
            bt_5 = Button(text='NEXT', font=('verdana', 15), bd=0,command=check_3)
            bt_5.place(x=300, y=300)

        else:
            showinfo('COLOUR GAME', 'WRONG ! THE COLOUR IS RED')

def check_1():
    global count
    global bt_4
    if e.get().lower()=='':
        showerror('COLOUR GAME','BLANK SPACE NOT ALLOWED ')
    else:
        if e.get().lower()=='green':
            showinfo('COLOUR GAME','CORRECT !')
            count=count+1
            e.delete(0,END)
            bt_3.destroy()
            lb_2.config(bg='red')
            bt_4 = Button(text='NEXT', font=('verdana', 15), bd=0, command=check_2)
            bt_4.place(x=300, y=300)

        else:
            showinfo('COLOUR GAME','WRONG ! THE COLOUR IS GREEN')

def start():
    global e
    global count
    global lb_2
    global bt_3
    jay.destroy()
    screen=Tk()
    screen.title('COLOUR GAME')
    screen.geometry('650x350')
    count=0
    lb_1=Label(screen,text='GIVE THE CORRECT COLOUR NAMES',font=('algerian',28),fg='#987654')
    lb_1.place(x=20,y=20)
    lb_2=Label(screen,width=50,height=8,bg='green',bd=0)
    lb_2.place(x=150,y=100)
    e=Entry(screen,font=('verdana',12),fg='red')
    e.place(x=230,y=230)
    bt_3=Button(screen,text='NEXT',font=('verdana',15),bd=0,command=check_1)
    bt_3.place(x=300,y=300)

jay=Tk()
jay.title('COLOUR GAME')
canvas=Canvas(jay,width=650,height=350)
canvas.pack()
canvas.create_text(325,50,text='A SIMPLE COLOUR GAME',font=('Mali',32,'bold'),fill='#654321')
bt_1=Button(canvas,text='EXIT',font=('verdana',15),bd=0,command=jay.destroy)
bt_1.place(x=20,y=300)
bt_2=Button(canvas,text='START',font=('verdana',15),bd=0,command=start)
bt_2.place(x=550,y=300)

mainloop()
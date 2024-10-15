import sqlite3
import tkinter
window=tkinter.Tk()
def save():
    print("user name",e1.get())
    l1.config(text=e1.get())
    print("passwrod",e2.get())
    l2.config(text=e2.get())

def reg_form():
    window2=tkinter.Tk()
    window2.title("registration")
    window2.maxsize(800,800)
    window2.minsize(500,500)
    window2.configure(bg="black")
    def reg():
        con=sqlite3.connect("python/tkinter/sample.db")
        # con.execute("create table user(uname text,password text)")
        con.execute("insert into user(uname,password)values(?,?)",(entry1.get(),entry2.get()))
        con.commit()
        window2.destroy()

    l1=tkinter.Label(window2,text="registration")
    l1.place(x=150,y=5)
    l2=tkinter.Label(window2,text="usernname",bg="yellow",fg="black")
    l2.place(x=80,y=40)
    entry1=tkinter.Entry(window2)
    entry1.place(x=200,y=40)
    l3=tkinter.Label(window2,text="password",bg="yellow",fg="black")
    l3.place(x=80,y=70)
    entry2=tkinter.Entry(window2)
    entry2.place(x=200,y=70)
    b1=tkinter.Button(window2,text="register",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10,command=reg)
    b1.place(x=150,y=120)

def home():
    window3=tkinter.Tk()
    window3.title("home")
    window3.maxsize(800,800)
    window3.minsize(500,500)
    l1=tkinter.Label(window3,text="home page")
    l1.pack()
    b1=tkinter.Button(window3,text="logout",command=window3.quit)
    b1.pack()
    window3.mainloop()

def login():
    con=sqlite3.connect("python/tkinter/sample.db")
    data=con.execute("select * from user where uname=? and password=?",(e1.get(),e2.get()))
    f=0
    for i in data:
        f=1
        home()
    if f==0:
        l3.config(text="invalid user name or password!!",fg="red")

# def register():
    # print(entry1.get())
    # print(entry2.get())





window.title("log-in")
window.maxsize(800,800)
window.minsize(500,500)
window.configure(bg="yellow")

label=tkinter.Label(window,text="welcome all",fg="green",bg="white",padx=10)
label.place(x=150,y=5)
l3=tkinter.Label(window,bg="yellow")
l3.place(x=150,y=180)
l1=tkinter.Label(window,text="username",bg="yellow",fg="black")
l1.place(x=80,y=40)
e1=tkinter.Entry(window)
e1.place(x=200,y=40)

l2=tkinter.Label(window,text="password",bg="yellow",fg="black")
l2.place(x=80,y=70)
e2=tkinter.Entry(window)
e2.place(x=200,y=70)

b1=tkinter.Button(window,text="login",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10,command=login)
b1.place(x=150,y=100)
b2=tkinter.Button(window,text="register",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10,command=reg_form)
b2.place(x=230,y=100)



window.mainloop()
import tkinter
window=tkinter.Tk()
# def save():
#     l2.configure(text=e1.get())

def reg_form():
    window2=tkinter.Tk()
    window2.title("registration")
    window2.maxsize(800,800)
    window2.minsize(500,500)
    window2.configure(bg="black")
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
    b1=tkinter.Button(window2,text="register",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10,command=register)
    b1.place(x=150,y=120)

    # l3=tkinter.Label(window2)
    # l3.place(x=150,y=200)

def register():
    print(entry1.get())
    print(entry2.get())





window.title("log-in")
window.maxsize(800,800)
window.minsize(500,500)
window.configure(bg="yellow")

label=tkinter.Label(window,text="welcome all",fg="green",bg="white",padx=10)
label.place(x=150,y=5)
l1=tkinter.Label(window,text="usernname",bg="yellow",fg="black")
l1.place(x=80,y=40)
e1=tkinter.Entry(window)
e1.place(x=200,y=40)

l2=tkinter.Label(window,text="password",bg="yellow",fg="black")
l2.place(x=80,y=70)
e2=tkinter.Entry(window)
e2.place(x=200,y=70)

b1=tkinter.Button(window,text="save",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10)
b1.place(x=150,y=100)
b2=tkinter.Button(window,text="register",bg="silver",fg="black",activebackground="gray",activeforeground="red",padx=10,pady=10,command=reg_form)
b2.place(x=230,y=100)



window.mainloop()
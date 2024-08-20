from tkinter import *
win=Tk()
win.title("Calculator")
win.config(bg='cyan')
win.geometry("400x650")
win.resizable(False,False)

data=""

def get_data(value):
    global data
    data=data+str(value)
    var.set(data)


def clear():
    global data
    data=""
    var.set(data)


def equal():
    global data
    try:
     total=str(eval(data))
     var.set(total)
     data=""
    except:
        var.set("Error")

label_cal=Label(win,text="Calculator",font=("Times New Roman",25,"bold"),fg="black",bg="cyan")
label_cal.place(x=100,y=10,width=200,height=50)
var=StringVar()
label_entry=Entry(win,font=("Times New Roman",25,"bold"),relief=SUNKEN,bd=5,textvariable=var)
label_entry.place(x=50,y=80,height=50,width=300)

#-------------------------------------------------
button_clr=Button(win,text="clear",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="red",fg="white",command=clear)
button_clr.place(x=25,y=150,height=80,width=80)

button_div=Button(win,text="/",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda :get_data("/"))
button_div.place(x=115,y=150,height=80,width=80)

button_mul=Button(win,text="*",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda :get_data("*"))
button_mul.place(x=205,y=150,height=80,width=80)

button_sub=Button(win,text="-",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda :get_data("-"))
button_sub.place(x=295,y=150,height=80,width=80)
#-------------------------------------------------
button_7=Button(win,text="7",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(7))
button_7.place(x=25,y=255,height=80,width=80)

button_8=Button(win,text="8",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(8))
button_8.place(x=115,y=255,height=80,width=80)

button_9=Button(win,text="9",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(9))
button_9.place(x=205,y=255,height=80,width=80)

button_add=Button(win,text="+",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data("+"))
button_add.place(x=295,y=255,height=175,width=80)
#-------------------------------------------------
button_4=Button(win,text="4",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(4))
button_4.place(x=25,y=350,height=80,width=80)

button_5=Button(win,text="5",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(5))
button_5.place(x=115,y=350,height=80,width=80)

button_6=Button(win,text="6",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda :get_data(6))
button_6.place(x=205,y=350,height=80,width=80)
#-----------------------------------------------------

button_1=Button(win,text="1",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(1))
button_1.place(x=25,y=445,height=80,width=80)

button_2=Button(win,text="2",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(2))
button_2.place(x=115,y=445,height=80,width=80)

button_3=Button(win,text="3",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(3))
button_3.place(x=205,y=445,height=80,width=80)

button_ent=Button(win,text="enter",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="light green",fg="white",command=equal)
button_ent.place(x=295,y=445,height=185,width=80)

#-------------------------------------------------------

button_0=Button(win,text="0",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data(0))
button_0.place(x=25,y=550,height=80,width=170)

button_dec=Button(win,text=".",font=("Times New Roman",25,"bold"),relief="raised",bd=5,bg="grey",fg="white",command=lambda:get_data("."))
button_dec.place(x=205,y=550,height=80,width=80)









win.mainloop()
from tkinter import*
import random
import time

root=Tk()
root.geometry('1600x1600+0+0')
root.title("restaurant management system")

f1=Frame(root,width=1600,height=200,relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(root,width=900,height=600,relief=SUNKEN)
f2.pack(side=LEFT)

f3=Frame(root,width=600,height=600,relief=SUNKEN)
f3.pack(side=RIGHT)
#=============================================time=============================
localtime=time.asctime(time.localtime(time.time()))
#=========================================information==================================
lbl=Label(f1,text="Restaurant Management System",font=('Arial Bold',50),bd=16,anchor='w',relief=RAISED)
lbl.grid(column=0,row=0)
lbl=Label(f1,text=localtime,font=('Arial Bold',20),bd=10,anchor='w')
lbl.grid(column=0,row=1)
#================================calculator=============================
operator=""
text_Input=IntVar()
txt=Entry(f3,font=('Arial Bold',20),insertwidth=4,bg="powder blue",justify=RIGHT,textvariable=text_Input,bd=30)
txt.grid(columnspan=4)
def click(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def clear():
   global operator
   operator = ""
   text_Input.set("")


def equals():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""
   
btn7=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="7",command=lambda:click(7))
btn7.grid(column=0,row=2)

btn8=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="8",command=lambda:click(8))
btn8.grid(column=1,row=2)

btn9=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="9",command=lambda:click(9))
btn9.grid(column=2,row=2)

Addition=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="+",command=lambda:click("+"))
Addition.grid(column=3,row=2)

btn4=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="4",command=lambda:click(4))
btn4.grid(column=0,row=3)

btn5=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="5",command=lambda:click(5))
btn5.grid(column=1,row=3)

btn6=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="6",command=lambda:click(6))
btn6.grid(column=2,row=3)

substraction=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="-",command=lambda:click("-"))
substraction.grid(column=3,row=3)

btn1=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="1",command=lambda:click(1))
btn1.grid(column=0,row=4)

btn2=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="2",command=lambda:click(2))
btn2.grid(column=1,row=4)

btn3=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="3",command=lambda:click(3))
btn3.grid(column=2,row=4)

multiply=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="*",command=lambda:click("*"))
multiply.grid(column=3,row=4)

btn0=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="0",command=lambda:click(0))
btn0.grid(column=0,row=5)


btnclear=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="c",command=clear)
btnclear.grid(column=1,row=5)


btnequal=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="=",command=equals)
btnequal.grid(column=2,row=5)

division=Button(f3,padx=16,pady=16,bd=8,fg="Black",font=('arial bold',20),bg="powder blue",text="/",command=lambda:click("/"))
division.grid(column=3,row=5)
#===============================================================================productdisplaydef Ref():
def Ref():
    x=random.randint(1000,500000)
    randomRef=str(x)
    rand.set(randomRef)
    SD=float(rand1.get())
    CB=float(rand2.get())
    VC=float(rand3.get())
    VB=float(rand4.get())
    FF=float(rand5.get())
    GB=float(rand6.get())

    sambher_dosa=SD*0.99
    chole_bhature=CB*1.44
    VEG_CHOWMIEN=VC*3.87
    veg_burger=VB*2.88
    FRENCH_FRIES=FF*3.67
    garlic_bread=GB*6.09

    cost_of_meal="$" , str('%.2f' % (sambher_dosa + chole_bhature + VEG_CHOWMIEN + veg_burger + FRENCH_FRIES +  garlic_bread))

    Paycharges = ((sambher_dosa + chole_bhature + VEG_CHOWMIEN + veg_burger + FRENCH_FRIES +  garlic_bread)*0.2)

    Totalcost =(sambher_dosa + chole_bhature + VEG_CHOWMIEN + veg_burger + FRENCH_FRIES +  garlic_bread)

    rand7.set(cost_of_meal)
    service = "$" , str('%.2f' % (Paycharges))
    rand8.set(service)
    total = "$" , str('%.2f' % (Totalcost))
    rand10.set(total)
    
    
    

def qexit():
    root.destroy()

def reset():
    rand1.set("")
    rand2.set("")
    rand3.set("")
    rand4.set("")
    rand5.set("")
    rand6.set("")
    rand7.set("")
    rand8.set("")
    rand.set("")
    rand10.set("")

rand1=StringVar()
rand2=StringVar()
rand3=StringVar()
rand4=StringVar()
rand5=StringVar()
rand6=StringVar()
rand7=StringVar()
rand8=StringVar()
rand=StringVar()
rand10=StringVar()
lbl=Label(f2,text="sambher dosa",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=0,column=0)

txt=Entry(f2,textvariable=rand1,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="powder blue")
txt.grid(row=0,column=1)

lbl=Label(f2,text="chole bhature",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=1,column=0)

txt=Entry(f2,textvariable=rand2,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="powder blue")
txt.grid(row=1,column=1)

lbl=Label(f2,text="veg chowmien",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=2,column=0)

txt=Entry(f2,textvariable=rand3,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="powder blue")
txt.grid(row=2,column=1)

lbl=Label(f2,text="veg burger",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=3,column=0)

txt=Entry(f2,textvariable=rand4,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="powder blue")
txt.grid(row=3,column=1)

lbl=Label(f2,text="french fries",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=4,column=0)

txt=Entry(f2,textvariable=rand5,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="powder blue")
txt.grid(row=4,column=1)

lbl=Label(f2,text="garlic bread",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=0,column=3)

txt=Entry(f2,textvariable=rand6,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="#ffffff")
txt.grid(row=0,column=4)

lbl=Label(f2,text="cost of meal",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=1,column=3)

txt=Entry(f2,textvariable=rand7,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="#ffffff")
txt.grid(row=1,column=4)

lbl=Label(f2,text="service charges",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=2,column=3)

txt=Entry(f2,textvariable=rand8,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="#ffffff")
txt.grid(row=2,column=4)

lbl=Label(f2,text="reference",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=3,column=3)

txt=Entry(f2,textvariable=rand,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="#ffffff")
txt.grid(row=3,column=4)

lbl=Label(f2,text="Total cost",font=('arial bold',16),bd=16,anchor='w')
lbl.grid(row=4,column=3)

txt=Entry(f2,textvariable=rand10,font=('arial bold',10),bd=10,insertwidth=4,justify=RIGHT,bg="#ffffff")
txt.grid(row=4,column=4)
#=========================================================================BUTTONS==============================================================================================
 
btnTotal=Button(f2,padx=16,pady=10,bd=16,font=('arial bold',16),fg="black",width=10,text="Total",bg="#ffffff",command=Ref)
btnTotal.grid(row=6,column=1)

btnqexit=Button(f2,padx=16,pady=10,bd=16,font=('arial bold',16),fg="black",width=10,text="exit",bg="#ffffff",command=qexit)
btnqexit.grid(row=6,column=3)

btnreset=Button(f2,padx=16,pady=10,bd=16,font=('arial bold',16),fg="black",width=10,text="reset",bg="#ffffff",command=reset)
btnreset.grid(row=6,column=2)


         
root.mainloop()












































root.mainloop()

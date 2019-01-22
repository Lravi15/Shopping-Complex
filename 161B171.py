from Tkinter import *
from tkMessageBox import *
import sqlite3
from splash import *
root=Tk()
root.geometry()
root.title("Shopping Complex")
global name
name=[]
global price
price=[]
global x
conn=sqlite3.connect('info.db')
cur=conn.cursor()
cur.execute("create table if not exists per(c_id number primary key,c_name varchar(20),c_mobno number,c_add varchar(20))")

Label(root,text='Press GO to enter in the shopping mall',font='times 15 italic',fg='blue').grid(row=0,column=0)        

def fun():
    Label(root,text="Welcome In The Shopping Complex",font="helvatica 35 italic",fg='firebrick',width=30).grid(row=2)
    Button(root,text='MAIN MENU',font='times 15 bold italic',relief='raised',bd=5,bg='sandy brown',command=bnm).grid(row=5,sticky=N)
Button(root,text='GO',relief='raised',fg='black',bg='white',font='times 15 bold italic',bd=5,command=fun).grid()
img=PhotoImage(file='shop.gif')
Label(root,image=img).grid(row=4,columnspan=5)
def des():
    root.destroy()
root.after(8000,des)


#-------Main Menu

def bnm():
    root=Tk()
    root.title("Main Menu Of Shopping Complex")

    def fun1():
        Label(root,text="The Shopping Complex",font="helvatica 35 italic",fg='brown',width=30).grid(row=8)
        Label(root,text='--------------------------------------------------------------------------------------------------------------------------').grid(row=9)
        Button(root,text='CUSTOMER INFORMATION',font='times 15 bold italic',bg='peach puff',relief='raised',bd=5,command=fun2).grid(row=10,sticky=N)
        Label(root,text='--------------------------------------------------------------------------------------------------------------------------').grid(row=11)
    def fun3():
        Label(root,text='Store Name',font='times 13 bold').grid(row=19,column=0)
        Button(root,text='SHOES',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=fun10).grid(row=20,sticky=W)
        Button(root,text='STATIONARY',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=fun11).grid(row=21,sticky=W)
        Button(root,text='CLOTHES',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=info1).grid(row=22,sticky=W)
        Button(root,text='EATABLES',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=info5).grid(row=23,sticky=W)
        Button(root,text='ACCESSORIES',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=not1).grid(row=24,sticky=W)
        Button(root,text='TOOLS',font='times 10 bold italic',relief='raised',bd=5,bg='plum',command=com1).grid(row=25,sticky=W)
        Label(root,text='Click EXIT to get Your Bill : ',fg='red',font='heartbit 15 bold italic').grid(row=26,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,fg='black',bg='maroon',command=total).grid(row=27,sticky=N)

    def fun2():
        Label(root,text='Please enter your details :',font='times 17 bold',fg='dark green').grid(row=12,column=0,sticky=W)
        Label(root,text='Enter Customer ID :',font='times 12 bold italic').grid(row=13,column=0,sticky=W)
        w=Entry(root,width=35,bd=5)
        w.grid(row=13,column=1)
        Label(root,text='Enter Your name :',font='times 12 bold italic').grid(row=14,column=0,sticky=W)
        x=Entry(root,width=35,bd=5)
        x.grid(row=14,column=1)
        Label(root,text='Enter Your Mobile No. :',font='times 12 bold italic').grid(row=15,column=0,sticky=W)    
        y=Entry(root,width=35,bd=5)
        y.grid(row=15,column=1)
        Label(root,text='Enter Your Address :',font='times 12 bold italic').grid(row=16,column=0,sticky=W)
        z=Entry(root,width=35,bd=5)
        z.grid(row=16,column=1)
        q=[]
        def insert2():
            p=[(w.get(),x.get(),y.get(),z.get())]
            i=0
            q.append(w.get())
            if(w.get()=="" or x.get()=="" or y.get()=="" or z.get()==""):
                showerror('Error','Missing Details')
            else:
                for i1 in range(len(q)-1):
                    if (q[i1]==w.get()):
                        i=i+1
                        showinfo('error','Duplicate data')
                        break;
                if i==0:
                    cur.executemany("insert into per values(?,?,?,?)",p)
                    conn.commit()
                    w.delete(0,END)
                    x.delete(0,END)
                    y.delete(0,END)
                    z.delete(0,END)
                    showinfo('database','Data succesfully inserted')
            
        Button(root,text='INSERT',relief='raised',font='times 13 bold italic',bd=5,fg='blue',command=insert2).grid(row=17,sticky=W)
        Button(root,text='STORE LIST',relief='raised',font='times 13 bold italic',bg='peach puff',bd=5,command=fun3).grid(row=18,sticky=N)
        
   
    Button(root,text="ENTER",bg='spring green',fg='black',font='times 15 bold italic',bd=5,command=fun1).grid(sticky=N)

def fun10():
    root=Toplevel()
    root.title('Shoes') 
  
    def fun5():
        b2=IntVar()
        qnt=IntVar()
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',bd=5,fg='dark blue',).grid(row=3,column=1,sticky=E)
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='550.00').grid(row=5,column=1,sticky=E)
        Label(root,text='1200.00').grid(row=6,column=1,sticky=E)
        Label(root,text='465.00').grid(row=7,column=1,sticky=E)
        Label(root,text='800.00').grid(row=8,column=1,sticky=E)
        Label(root,text='1400.00').grid(row=9,column=1,sticky=E)  
        Radiobutton(root,text='Bata',variable=b2,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Red-Chief',variable=b2,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Lakhani',variable=b2,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='Action',variable=b2,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='Adidas',variable=b2,value=5).grid(row=9,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=10,column=0,sticky=W)
        g=Entry(root,width=25,bd=5,textvariable=qnt)
        g.grid(row=10,column=1,sticky=E)

        def qwer():
            b=["Bata","Red-Chief","Lakhani","Action","Adidas"]
            c=[550,1200,465,800,1400]
            if(qnt.get()!=0):
                if(b2.get()==1):
                    showinfo('selected','You purchased Bata')
                elif(b2.get()==2):
                    showinfo('selected','You purchased Red-Chief')
                elif(b2.get()==3):
                    showinfo('selected','You purchased Lakhani')
                elif(b2.get()==4):
                    showinfo('selected','You purchased Action')
                elif(b2.get()==5):
                    showinfo('selected','You purchased Adidas')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')    
            if(b2.get()!=1 and b2.get()!=2 and b2.get()!=3 and b2.get()!=4 and b2.get()!=5):
                showinfo('Not selected','No items selected')
            else:
                if(qnt.get()==0):
                    name.append('')
                else:
                    name.append(b[b2.get()-1])
                    price.append(c[b2.get()-1]*qnt.get())
               
        Button(root,text='BUY',font='times 13 bold italic ',relief='raised',bd=5,bg='rosy brown',command=qwer).grid(row=11,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd1).grid(row=11,column=1,sticky=E)   

    def asd1():
        root.destroy()               

    def fun4():
        Label(root,text='Item List Of Shoes',font='times 15 bold',bg='orchid').grid(row=2,sticky=N)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bd=5,bg='spring green',command=fun5).grid(row=3,column=0,sticky=W)
       
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=fun4).grid(row=1,sticky=W)

def fun11():
    root=Toplevel()
    root.title('Stationary')     

    def fun7():
        c1=IntVar()
        qnt=IntVar()
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',fg='dark blue',bd=5).grid(row=3,column=1,sticky=E)
        Label(root,text='20.00').grid(row=5,column=1,sticky=E)
        Label(root,text='10.00').grid(row=6,column=1,sticky=E)
        Label(root,text='5.00').grid(row=7,column=1,sticky=E)
        Label(root,text='800.00').grid(row=8,column=1,sticky=E)
        Label(root,text='80.00').grid(row=9,column=1,sticky=E)
        Label(root,text='15.00').grid(row=10,column=1,sticky=E)
        Label(root,text='500.00').grid(row=11,column=1,sticky=E)
        Radiobutton(root,text='Pen',variable=c1,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Pencil',variable=c1,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Eraser',variable=c1,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='Magazine',variable=c1,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='Comic Books',variable=c1,value=5).grid(row=9,column=0,sticky=W)
        Radiobutton(root,text='Hand-Paper',variable=c1,value=6).grid(row=10,column=0,sticky=W)
        Radiobutton(root,text='Bags',variable=c1,value=7).grid(row=11,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=12,column=0,sticky=W)
        g=Entry(root,width=20,bd=5,textvariable=qnt)
        g.grid(row=12,column=1,sticky=E)

        def zxc1():
            b=["Pen","Pencil","Eraser","Magazine","Comic Books","Hand-Paper","Bags"]
            c=[20,10,5,800,80,15,500]
            if(qnt.get()!=0):
                if(c1.get()==1):
                    showinfo('selected','You purchased Pen')
                elif(c1.get()==2):
                    showinfo('selected','You purchased Pencil')
                elif(c1.get()==3):
                    showinfo('selected','You purchased Eraser')
                elif(c1.get()==4):
                    showinfo('selected','You purchased Magazine')
                elif(c1.get()==5):
                    showinfo('selected','You purchased Comic Books')
                elif(c1.get()==6):
                    showinfo('selected','You purchased Hand-Paper')
                elif(c1.get()==7):
                    showinfo('selected','You purchased Bags')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')

            if(c1.get()!=1 and c1.get()!=2 and c1.get()!=3 and c1.get()!=4 and c1.get()!=5 and c1.get()!=6 and c1.get()!=7):
                showinfo('Not selected','No items selected')
            else:
                if(qnt.get()==0):
                    name.append('')
                else:
                    name.append(b[c1.get()-1])
                    price.append(c[c1.get()-1]*qnt.get())

        Button(root,text='BUY',font='times 13 bold italic ',relief='raised',bd=5,bg='rosy brown',command=zxc1).grid(row=13,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd2).grid(row=13,column=1,sticky=E)
        
    def asd2():
        root.destroy()  
    def fun8():
        Label(root,text='Item List Of Stationary',font='times 15 bold',bg='orchid').grid(row=2)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bd=5,bg='spring green',command=fun7).grid(row=3,column=0,sticky=W)
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=fun8).grid(row=1,sticky=W) 

def info1():
    root=Toplevel()
    root.title('Clothes')

    def info2():
        d1=IntVar()
        qnt=IntVar()
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',fg='dark blue',bd=5).grid(row=3,column=1,sticky=E)
        Label(root,text='600.00').grid(row=5,column=1,sticky=E)
        Label(root,text='800.00').grid(row=6,column=1,sticky=E)
        Label(root,text='1000.00').grid(row=7,column=1,sticky=E)
        Label(root,text='275.00').grid(row=8,column=1,sticky=E)
        Label(root,text='350.00').grid(row=9,column=1,sticky=E)
        Label(root,text='300.00').grid(row=10,column=1,sticky=E)
        Radiobutton(root,text='Jacket',variable=d1,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Jeans ',variable=d1,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Cargos ',variable=d1,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='T-Shirts ',variable=d1,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='Shirts',variable=d1,value=5).grid(row=9,column=0,sticky=W)
        Radiobutton(root,text='Belts',variable=d1,value=6).grid(row=10,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=11,column=0,sticky=W)
        g=Entry(root,width=20,bd=5,textvariable=qnt)
        g.grid(row=11,column=1,sticky=E)

        def zxc2():
            b=["Jacket","Jeans","Cargos"," T-Shirts","Shirts","Belts"]
            c=[600,800,1000,275,300,350]
            if(qnt.get()!=0):
                if(d1.get()==1):
                    showinfo('selected','You purchased Jacket')
                elif(d1.get()==2):
                    showinfo('selected','You purchased Jeans')
                elif(d1.get()==3):
                    showinfo('selected','You purchased Cargos')
                elif(d1.get()==4):
                    showinfo('selected','You purchased  T-Shirts')
                elif(d1.get()==5):
                    showinfo('selected','You purchased Shirts')
                elif(d1.get()==6):
                    showinfo('selected','You purchased Belts ')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')     
            if(d1.get()!=1 and d1.get()!=2 and d1.get()!=3 and d1.get()!=4 and d1.get()!=5 and d1.get()!=6):
                showinfo('Not selected','No items selected')
            else:
                 if(qnt.get()==0):
                    name.append('')
                 else:
                    name.append(b[d1.get()-1])
                    price.append(c[d1.get()-1]*qnt.get())      
        Button(root,text='BUY',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=zxc2).grid(row=12,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd3).grid(row=12,column=1,sticky=E)

    def asd3():
        root.destroy()   
    def info4():
        Label(root,text='Item List Of Clothes',font='times 15 bold',bg='orchid').grid(row=2)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bg='spring green',bd=5,command=info2).grid(row=3,column=0,sticky=W)
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=info4).grid(row=1,sticky=W) 

def info5():
    root=Toplevel()
    root.title('Eatables')

    def info6():
        e1=IntVar()
        qnt=IntVar()
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',fg='dark blue',bd=5).grid(row=3,column=1,sticky=E)
        Label(root,text='400.00').grid(row=5,column=1,sticky=E)
        Label(root,text='100.00').grid(row=6,column=1,sticky=E)
        Label(root,text='40.00').grid(row=7,column=1,sticky=E)
        Label(root,text='300.00').grid(row=8,column=1,sticky=E)
        Label(root,text='50.00').grid(row=9,column=1,sticky=E)
        Label(root,text='30.00').grid(row=10,column=1,sticky=E)
        Radiobutton(root,text='Pizza ',variable=e1,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Burger',variable=e1,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Pastry ',variable=e1,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='Cake',variable=e1,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='French Fries ',variable=e1,value=5).grid(row=9,column=0,sticky=W)
        Radiobutton(root,text='Sandwich',variable=e1,value=6).grid(row=10,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=11,column=0,sticky=W)
        g=Entry(root,width=20,bd=5,textvariable=qnt)
        g.grid(row=11,column=1,sticky=E)

        def zxc3():
            b=["Pizza","Burger","Pastry"," Cake","French Fries","Sandwich"]
            c=[400,100,40,300,50,30]
            if(qnt.get()!=0):
                if(e1.get()==1):
                    showinfo('selected','You purchased Pizza')
                elif(e1.get()==2):
                    showinfo('selected','You purchased Burger')
                elif(e1.get()==3):
                    showinfo('selected','You purchased Pastry')
                elif(e1.get()==4):
                    showinfo('selected','You purchased  Cake')
                elif(e1.get()==5):
                    showinfo('selected','You purchased French Fries')
                elif(e1.get()==6):
                    showinfo('selected','You purchased  Sandwich')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')
                
            if(e1.get()!=1 and e1.get()!=2 and e1.get()!=3 and e1.get()!=4 and e1.get()!=5 and e1.get()!=6):
                showinfo('Not selected','No items selected')
            else:
                if(qnt.get()==0):
                    name.append('')
                else:
                    name.append(b[e1.get()-1])
                    price.append(c[e1.get()-1]*qnt.get())

        Button(root,text='BUY',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=zxc3).grid(row=12,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd4).grid(row=12,column=1,sticky=E)      
    def asd4():
        root.destroy()    
    def info4():
        Label(root,text='Item List Of Eatables',font='times 15 bold',bg='orchid').grid(row=2)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bg='spring green',bd=5,command=info6).grid(row=3,column=0,sticky=W)
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=info4).grid(row=1,sticky=W) 
def not1():
    root=Toplevel()
    root.title('Accessories')
    def not2():
        f1=IntVar()
        qnt=IntVar()
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',fg='dark blue',bd=5).grid(row=3,column=1,sticky=E)
        Label(root,text='400.00').grid(row=5,column=1,sticky=E)
        Label(root,text='150.00').grid(row=6,column=1,sticky=E)
        Label(root,text='250.00').grid(row=7,column=1,sticky=E)
        Label(root,text='300.00').grid(row=8,column=1,sticky=E)
        Label(root,text='175.00').grid(row=9,column=1,sticky=E)
        Radiobutton(root,text='Earings  ',variable=f1,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Head Gear',variable=f1,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Neck Pieces ',variable=f1,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='Wrist Gear  ',variable=f1,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='Anklets  ',variable=f1,value=5).grid(row=9,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=10,column=0,sticky=W)
        g=Entry(root,width=20,bd=5,textvariable=qnt)
        g.grid(row=10,column=1,sticky=E)

        def zxc4():
            b=["Earings","Head Gear","Neck Pieces","Wrist Gear ","Anklets "]
            c=[400,150,250,300,175]
            if(qnt.get()!=0):
                if(f1.get()==1):
                    showinfo('selected','You purchased Earings')
                elif(f1.get()==2):
                    showinfo('selected','You purchased Head Gear')
                elif(f1.get()==3):
                    showinfo('selected','You purchased Neck Pieces')
                elif(f1.get()==4):
                    showinfo('selected','You purchased  Wrist Gear')
                elif(f1.get()==5):
                    showinfo('selected','You purchased Anklets')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')
            
            if(f1.get()!=1 and f1.get()!=2 and f1.get()!=3 and f1.get()!=4 and f1.get()!=5 ):
                showinfo('Not selected','No items selected')
            else:
                if(qnt.get()==0):
                    name.append('')
                else:
                    name.append(b[f1.get()-1])
                    price.append(c[f1.get()-1]*qnt.get())
               
        Button(root,text='BUY',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=zxc4).grid(row=11,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd5).grid(row=11,column=1,sticky=E)

    def asd5():
        root.destroy()
    def info4():
        Label(root,text='Item List Of Accessories',font='times 15 bold',bg='orchid').grid(row=2)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bg='spring green',bd=5,command=not2).grid(row=3,column=0,sticky=W)
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=info4).grid(row=1,sticky=W) 

def com1():
    root=Toplevel()
    root.title('Tools')

    def com2():
        g1=IntVar()
        qnt=IntVar()
        Label(root,text='Please choose one at a time :',font='times 15 bold',fg='brown').grid(row=4)
        Label(root,text='Item Price ',font='times 12 bold italic',relief='raised',fg='dark blue',bd=5).grid(row=3,column=1,sticky=E)
        Label(root,text='120.00').grid(row=5,column=1,sticky=E)
        Label(root,text='75.00').grid(row=6,column=1,sticky=E)
        Label(root,text='175.00').grid(row=7,column=1,sticky=E)
        Label(root,text='70.00').grid(row=8,column=1,sticky=E)
        Label(root,text='180.00').grid(row=9,column=1,sticky=E)
        Radiobutton(root,text='Sledge Hammer  ',variable=g1,value=1).grid(row=5,column=0,sticky=W)
        Radiobutton(root,text='Screw Driver ',variable=g1,value=2).grid(row=6,column=0,sticky=W)
        Radiobutton(root,text='Axe ',variable=g1,value=3).grid(row=7,column=0,sticky=W)                                                           
        Radiobutton(root,text='Nuts & Bolts',variable=g1,value=4).grid(row=8,column=0,sticky=W)
        Radiobutton(root,text='Plier',variable=g1,value=5).grid(row=9,column=0,sticky=W)
        Label(root,text='Enter Quantity :',font='times 15 bold italic',fg='blue').grid(row=10,column=0,sticky=W)
        g=Entry(root,width=20,bd=5,textvariable=qnt)
        g.grid(row=10,column=1,sticky=E)

        def zxc5():
            b=[" Sledge Hammer "," Screw Driver"," Axe"," Nuts & Bolts "," Plier"]
            c=[120,75,175,70,180]
            if(qnt.get()!=0):
                if(g1.get()==1):
                    showinfo('selected','You purchased  Sledge Hammer ')
                elif(g1.get()==2):
                    showinfo('selected','You purchased  Screw Driver')
                elif(g1.get()==3):
                    showinfo('selected','You purchased  Axe ')
                elif(g1.get()==4):
                    showinfo('selected','You purchased Nuts & Bolts')
                elif(g1.get()==5):
                    showinfo('selected','You purchased   Plier')
            else:
                showerror('not selected','You purchased Nothing !!! ')
                showinfo('selected','Please Select Quantity !!!')

            if(g1.get()!=1 and g1.get()!=2 and g1.get()!=3 and g1.get()!=4 and g1.get()!=5 ):
                showinfo('Not selected','No items selected')
            else:
                if(qnt.get()==0):
                    name.append('')
                else:
                    name.append(b[g1.get()-1])
                    price.append(c[g1.get()-1]*qnt.get())
               
        Button(root,text='BUY',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=zxc5).grid(row=11,column=0,sticky=W)
        Button(root,text='EXIT',font='times 13 bold italic',relief='raised',bd=5,bg='rosy brown',command=asd6).grid(row=11,column=1,sticky=E)
    def asd6():
        root.destroy()
     
    def com4():
        Label(root,text='Item List Of Tools',font='times 15 bold',bg='orchid').grid(row=2)
        Button(root,text='Item Name ',font='times 12 bold italic',relief='raised',bg='spring green',bd=5,command=com2).grid(row=3,column=0,sticky=W)
    Button(root,text='Start',relief='raised',font='times 10 bold',bd=3,command=com4).grid(row=1,sticky=W) 

#-----------Bill

def total():
    root=Toplevel()
    root.title("Bill")
    Label(root,text='Enter Customer ID to see customer details  : ',font='times 15 bold italic').grid(row=1)
    Label(root,text='Enter Customer ID :',font='times 13 bold ',fg='blue').grid(row=2,column=0,sticky=W)
    h=Entry(root,width=30,bd=3)
    h.grid(row=2,column=1,sticky=E)

    def det():
        cur.execute('select * from per where c_id=(?)',[int(h.get())])
        n=cur.fetchall()      
        Label(root,text="Name  :"+str(n[0][1]),font='times 13 bold italic',bg='moccasin').grid(row=6,sticky=W)
        Label(root,text="Mobile  :"+str(n[0][2]),font='times 13 bold italic',bg='moccasin').grid(row=7,sticky=W)
        Label(root,text="Address  :"+str(n[0][3]),font='times 13 bold italic',bg='moccasin').grid(row=8,sticky=W)
        Label(root,text='Click SHOW to see purchased items :',font='times 15 bold italic',fg='orange red').grid(row=9,column=0,sticky=W)
        nameinfo=StringVar()

        def cvb1():
            showinfo('purchased items',name)
        Label(root,text='Click Bill to see total amount :',font='times 15 bold italic',fg='orange red').grid(row=9,column=1,sticky=E)

        def cvb():
            showinfo('Hello',"Amount to be paid: Rs. %d/-"%(sum(price)))
            showinfo('Thanks'," THANK YOU VISIT AGAIN")
        def tre():
            root.destroy()
        Button(root,text='BILL',relief='raised',font='times 13 bold italic',bd=5,bg='rosy brown',command=cvb).grid(row=10,column=1,sticky=E)
        Button(root,text='SHOW',relief='raised',font='times 13 bold italic',bd=5,bg='rosy brown',command=cvb1).grid(row=10,column=0,sticky=W)
        Button(root,text='EXIT',relief='raised',font='times 13 bold italic',bd=5,command=tre,fg='black',bg='cyan').grid(row=11,column=0,sticky=W)

    Button(root,text='DETAIL',font='times 15 bold italic',bd=5,bg='saddle brown',fg='white',command=det).grid(row=3,sticky=W)


root.mainloop()

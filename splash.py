from Tkinter import *

root=Tk()
#------Splash Screen

imag=PhotoImage(file='fsplash.gif')
Label(root,text=' Shopping Complex',font='times 25 bold italic',bg='spring green',fg='black',width=29).grid(row=0,sticky=N)
def des():
    root.destroy()
Label(root,text='Name : Ravi Singh',font='times 16 bold italic',fg='dark cyan').grid(row=2,column=0,sticky=W)
Label(root,text='Enrollment no. : 161B171',font='times 16 bold italic',fg='dark cyan').grid(row=3,column=0,sticky=W)
#Label(root,text='Batch : B6',font='times 16 bold italic',fg='dark cyan').grid(row=4,column=0,sticky=W)
Label(root,text='E-Mail : raviduos15@gamil.com',font='times 16 bold italic',fg='dark cyan').grid(row=5,column=0,sticky=W)
Label(root,image=imag).grid(row=1,columnspan=3)
root.after(4000,des)
root.mainloop()

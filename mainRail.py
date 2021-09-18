from tkinter import *
from PIL import ImageTk,Image
import datetime, random
import mysql.connector as c

Detail=['','']
Signup=['','','','']
buytick=['','','','']
tickcancel=['','']
fairlist=['','','']

root=Tk()
root.geometry('888x500+300+100')
root.resizable(False, False)
root.title('RAILWAYS')
bill=0
tea=0
coff=0
L=0
mL=0
VegBk=0
NBk=0
Vmeal=0
Nmeal=0
root.iconbitmap('icon.ico')
#__________________vars for tickets_________________
clas = StringVar()
dest = StringVar()
fr = StringVar()
dt = StringVar()
tickprice=0
#_____________________________________________________logged________________________________________________________
logged=False
#___________________
tname=''
#__________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________


def Main():
    global root, logged
    for widget in root.winfo_children():
        widget.destroy()

    train_image=ImageTk.PhotoImage(Image.open('bgtrain.png'))
    tlabel=Label(image=train_image)
    tlabel.place(x=-2,y=-2)

    x=LabelFrame(root, relief=RAISED, borderwidth=3, padx=20, pady=20, bg='white')
    x.place(x=632,y=100)

    Ticket1=Button(x, text='Tickets', font=("bold", 10), padx=48, pady=5, bg='light blue', command=Ticket).grid(row=0,column=0)
    #Ticket1.place(x=30,y=100)
    Label(x, bg='white').grid(row=1,column=0)
    
    Train_info=Button(x, text='Train Informaton', font=("bold", 10), padx=23, pady=5, bg='light blue', command=train).grid(row=2,column=0)
    #Train_info.place(x=30,y=150)
    Label(x, bg='white').grid(row=3,column=0)
    
    Food1=Button(x, text='Food', font=("bold", 10), padx=54, pady=5, bg='light blue', command=Food).grid(row=4,column=0)
    #Food1.place(x=30,y=200)

    if not logged:
        sign_up=Button(root, text='Sign Up', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=signup)
        sign_up.place(x=630,y=450)
        
        Login=Button(root, text='Login', font=("bold", 10), padx=28, pady=0.8, bg='light blue', command=login)
        Login.place(x=740,y=450)
    else:
        def out():
            global logged
            logged=False
            Main()
        def sh():
            for widget in root.winfo_children():
                widget.destroy()
            db=c.connect(host='localhost', passwd='123456', user='root', database='rail')
            cur=db.cursor()
            cur.execute("select pnr from email where mail='{}'".format(Signup[1]))
            x=cur.fetchone()[0]
            print(x)
            try:
                if x!='None' or x!=0:
                    cur.execute("select * from buyed where pnr='{}'".format(x))
                    x=cur.fetchone()
                    print(x)
                    Label(root, text='Your PNR : {}\nYour Train name : {}\nSeats :{}\nClass : {}'.format(x[5],x[6],x[4],x[3]), font=('bold',14)).place(x=340,y=200)
            except:
                Label(root, text='No History', font=('bold', 24)).place(x=330,y=200)
            Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
            Main1.place(x=0,y=0)
            db.commit()
        
        log=LabelFrame(root, relief=RAISED, borderwidth=3, padx=20, pady=10, bg='white')
        log.place(x=0,y=100)
        Label(log, text='Name : {}\nEmail : {}\nAge : {}\nGender : {}'.format(Signup[0],Signup[1],Signup[2],Signup[3]), font=("bold", 12), bg='white').pack()
        sign_out=Button(root, text='Sign Out', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=out)
        sign_out.place(x=630,y=450)
        SH=Button(root, text='History', font=("bold", 10), padx=25, pady=0.8, bg='light blue', command=sh)
        SH.place(x=750,y=450)

    root.mainloop()

#__________________________________________________________________________________________________________________


    
#__________________________________________________________________________________________________________________


def Ticket():
    global root, dest, fr, dt, tickprice
    for widget in root.winfo_children():
        widget.destroy()

    clas = StringVar()
    dest = StringVar()
    fr = StringVar()
    dt = StringVar()
    seats=IntVar()
    price=0

    train_image=ImageTk.PhotoImage(Image.open('bgtick.png'))
    tlabel=Label(image=train_image)
    tlabel.place(x=-2,y=-2)
#_____________________________________________________________________________________________________________________


#_____________________________________________________________________________________________________________________
    def Show():
        d=dt.get().split('-')
        rd=''
        try:
            for i in d:
                rd+=i
            rd=int(rd)
            if len(str(rd))>=6 and len(str(rd))<=8:
                Date.config(fg='black')
                buytick[2]=dt.get()
            else:
                akdsfh
        except:
            Date.delete(0, END)
            Date.config(fg='red')
            Date.insert(0,'Enter Date')
        
        if fr.get()=='From*' or fr.get()=='' or fr.get()=='Enter Source Station':
            From.delete(0, END)
            From.config(fg='red')
            From.insert(0,'Enter Source Station')
        else:
            From.config(fg='black')
            buytick[0]=fr.get()
        if dest.get()=='To*' or dest.get()=='' or dest.get()=='Enter Destination':
            Dest.delete(0, END)
            Dest.config(fg='red')
            Dest.insert(0,'Enter Destination')
        else:
            Dest.config(fg='black')
            buytick[1]=dest.get()
        if clas.get()=='':
            f.place(x=580,y=110)
            Label(f, text='Select Class!!', width=10, font=("bold", 10), bg='white', fg='red').grid(row=6,column=1)
        else:
            f.place(x=660,y=110)
            buytick[3]=clas.get()
            Label(f, text='             '*4, font=("bold", 10), bg='white').grid(row=3,column=1)
        if fr.get()!='From*' and fr.get()!='Enter Source Station' and fr.get()!='' and dest.get()!='To*' and dest.get()!='Enter Destination' and dest.get()!='' and dt.get()!='' and clas.get()!='':
            key=random.randint(100000,999999)
            for widget in root.winfo_children():
                widget.destroy()
            if clas.get()=='Second Class':
                tickprice=random.randint(100,280)
            elif clas.get()=='Third AC':
                tickprice=random.randint(280,600)
            elif clas.get()=='Second AC':
                tickprice=random.randint(600,1200)
            elif clas.get()=='First AC':
                tickprice=random.randint(1200,2000)
            
            Enter=Entry(root, textvariable=seats, font=('bold', 10), borderwidth=5)
            Enter.place(x=610,y=170)
            Enter.insert(0,'Enter no. of Seats:')
            Label(root, text='Ticket Price : {}₹'.format(price), font=('bold',14)).place(x=600,y=100)
            Label(root, text='Train Selected : (Choose Trains from below)', font=('bold', 16)).place(x=100,y=100)
            def Setprice(x,y):
                global tname
                tname=y
                price=tickprice+int(x)
                Label(root, text=' '*100).place(x=570,y=100)
                Label(root, text='  '*100).place(x=100,y=103)
                Label(root, text='Train Selected : {}'.format(y), font=('bold', 16)).place(x=100,y=100)
                Label(root, text='Ticket Price : {}₹'.format(price), font=('bold',14)).place(x=600,y=100)
                Enter.delete(0, END)
                Enter.insert(0,'Enter no. of Seats:')

            def confirmation():
                global tname, logged
                try:
                    if seats.get()=='' or seats.get()==0 or tname=='':
                        if seats.get()=='' or seats.get()==0:
                            Enter.config(fg='red')
                            Enter.delete(0,END)
                            Enter.insert(0, 'Enter correct seats')
                        if tname=='':
                            Label(root, text='  '*100, font=(20)).place(x=100,y=103)
                            Label(root, text='Select a Train', fg='red', font=('bold', 20)).place(x=150,y=100)
                    else:
                        for widget in root.winfo_children():
                            widget.destroy()
                        seat=random.randint(1,500)
                        l=seat
                        if seats.get()>1:
                            l=seat+seats.get()-1
                        
                        Label(root, text='Grand Total: {}'.format(price*seats.get()))
                        db=c.connect(host='localhost',user='root',passwd='123456',database='rail')
                        cur=db.cursor()
                        cur.execute("update trains set seats=seats-{} where tname='{}'".format(seats.get(),tname))
                        if logged:
                            cur.execute("update email set pnr='{}' where mail='{}'".format(key,Signup[1]))
                        cur.execute("insert into buyed values('{}','{}','{}','{}','{}-{}',{},'{}')".format(buytick[0],buytick[1],buytick[2],buytick[3],seat,l,key,tname))
                        cur.execute("select train_no from trains where tname='{}'".format(tname))
                        x=cur.fetchone()
                        Label(root, text='Your PNR : {}\nYour Train name : {}\nSeats :{}-{}\nTrain Number : {}'.format(key,tname,seat,l,x[0]), font=('bold',14)).place(x=280,y=200)
                        db.commit()
                        Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
                        Main1.place(x=0,y=0)
                except:
                    Enter.config(fg='red')
                    Enter.delete(0,END)
                    Enter.insert(0, 'Enter correct seats')
                    raise
                
            db=c.connect(host='localhost',user='root',passwd='123456',database='rail')
            cur=db.cursor()
            cur.execute("select tname,price from TRAINS")
            tlist=cur.fetchall()
            db.commit()
            Button(root, text='1)'+tlist[0][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[0][1],tlist[0][0])).place(x=10,y=200)
            Button(root, text='2)'+tlist[1][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[1][1],tlist[1][0])).place(x=10,y=250)
            Button(root, text='3)'+tlist[2][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[2][1],tlist[2][0])).place(x=10,y=300)
            Button(root, text='4)'+tlist[3][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[3][1],tlist[3][0])).place(x=10,y=350)
            Button(root, text='5)'+tlist[4][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[4][1],tlist[4][0])).place(x=10,y=400)
            Button(root, text='6)'+tlist[5][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[5][1],tlist[5][0])).place(x=300,y=200)
            Button(root, text='7)'+tlist[6][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[6][1],tlist[6][0])).place(x=300,y=250)
            Button(root, text='8)'+tlist[7][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[7][1],tlist[7][0])).place(x=300,y=300)
            Button(root, text='9)'+tlist[8][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[8][1],tlist[8][0])).place(x=300,y=350)
            Button(root, text='10)'+tlist[9][0], font=('bold',14), borderwidth=0, command=lambda:Setprice(tlist[9][1],tlist[9][0])).place(x=300,y=400)
            Label(root, text='Available Trains', font=('bold',14)).place(x=175,y=170)
            #_________________________________________NEXT_______________________________________________________
            Next=Button(root, text='Next', font=('bold',14), command=confirmation).place(x=610,y=300)
            #_________________________________________BACK_______________________________________________________
            Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
            Main1.place(x=0,y=0)
            print(buytick,key,tickprice)
            root.mainloop()
#____________________________________________________________________________________________________________________


#_____________________________________________________________________________________________________________________


    def Cancel():
        for widget in root.winfo_children():
            widget.destroy()

        
        #______________________
        def Show():
            if cpnr.get()==0:
                Label(root, text='Enter PNR!!', font=("bold", 10), fg='red').place(x=570, y=100)
            else:
                tickcancel[0]=cpnr.get()
                Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=570, y=100)
            if tno.get()=='':
                Label(root, text='Enter Train No.!!', font=("bold", 10), fg='red').place(x=560, y=150)
            else:
                tickcancel[1]=tno.get()
                Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=150)
                
            if tickcancel[0]!=0 and tickcancel[1]!='':
                try:
                    db=c.connect(host='localhost',user='root',passwd='123456',database='rail')
                    cur=db.cursor()
                    cur.execute("select seatno,tno from buyed where pnr={}".format(cpnr.get()))
                    vals=cur.fetchone()
                    x=eval(vals[0])-1
                    cur.execute("update trains set seats=seats-{} where tname='{}'".format(x,vals[1]))
                    cur.execute("delete from buyed where pnr={}".format(cpnr.get()))
                    db.commit()
                    Label(root, text='Cancellation Confirmed!', font=("bold", 14)).place(x=278,y=250)
                except:
                    Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=100)
                    print(tickcancel)
                    raise
                    SUB.config(state='disabled')
        #______________________
        
        cpnr = IntVar()
        tno = StringVar()
        
        Label(root, text='Cancel Tickets', font=("bold", 30), padx=50, pady=5).place(x=240,y=0)

        Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
        Main1.place(x=0,y=0)

        Label(root, text='Enter PNR', font=("bold", 14), padx=50, pady=5).place(x=80,y=100)
        Label(root, text='Enter Train No.', font=("bold", 14), padx=50, pady=5).place(x=80,y=150)

        
        e1=Entry(root, textvariable=cpnr, borderwidth=5, font=("bold", 10))
        e1.place(x=400,y=100)
        e2=Entry(root, textvariable=tno, borderwidth=5, font=("bold", 10))
        e2.place(x=400,y=150)

        SUB=Button(root, text='Next', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Show)
        SUB.place(x=200,y=320)

        root.mainloop()

    #_______________________________________
    def PNR():
        for widget in root.winfo_children():
            widget.destroy()

        def pnrc():
            try:
                if code.get()!= 0:
                    db=c.connect(host='localhost',user='root',passwd='123456',database='rail')
                    cur=db.cursor()
                    cur.execute("select PNR from buyed where PNR='{}'".format(code.get()))
                    if code.get()==cur.fetchone()[0]:
                        Label(root, text='       '*10).place(x=650,y=105)
                        Label(root, text='TICKET CONFIRMED!', font=("bold", 14)).place(x=278,y=250)
                    else:
                        Label(root, text='TICKET NOT CONFIRMED!', font=("bold", 14)).place(x=278,y=250)
                    SUB.config(state='disabled')
                    db.commit()
                else:
                    Label(root, text='Enter PNR', font=("bold", 14), fg='red').place(x=650,y=100)
            except (c.errors.InterfaceError,TypeError):
                Label(root, text='       '*10).place(x=650,y=105)
                Label(root, text='TICKET NOT CONFIRMED!', font=("bold", 14)).place(x=278,y=250)
            except:
                Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=100)
                raise

        code=IntVar()
        Label(root, text='Enter PNR Code', font=("bold", 14), padx=50, pady=5).place(x=150,y=100)
        e1=Entry(root, textvariable=code, borderwidth=5, font=("bold", 10))
        e1.place(x=480,y=100)

        SUB=Button(root, text='Confirm', font=("bold", 10), padx=15, pady=5, bg='light blue', command=pnrc)
        SUB.place(x=300,y=160)

        Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
        Main1.place(x=0,y=0)
    
    #_______________________________________
    def fair():
        for widget in root.winfo_children():
            widget.destroy()

        d=StringVar()
        f=StringVar()
        c=StringVar()

        def show():
            
            #if len(fairlist)!=3:
            if d.get()=='':
                Label(root, text='Enter Destination!!', font=("bold", 10), fg='red').place(x=570, y=100)
            else:
                fairlist[0]=d.get()
                Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=570, y=100)
            if f.get()=='':
                Label(root, text='Enter Source Station!!', font=("bold", 10), fg='red').place(x=560, y=150)
            else:
                fairlist[1]=f.get()
                Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=150)
            if c.get()=='':
                Label(root, text='Select Seats!!', font=("bold", 10), fg='red').place(x=580, y=200)
            else:
                fairlist[2]=c.get()
                Label(root, text='              ', width=10, font=("bold", 10), fg='red').place(x=580, y=200)
                    
            x=0
            for i in range(3):
                if fairlist[i]=='':
                    x=1
                else:
                    x=0
            if x==0 and fairlist!=[]:
                print(fairlist)
                SUB.config(state='disabled')
        
        Label(root, text='Enter Destination', font=("bold", 14), padx=50, pady=5).place(x=80,y=100)
        Label(root, text='Enter From', font=("bold", 14), padx=50, pady=5).place(x=80,y=150)
        Label(root, text='Enter Class', font=("bold", 14), padx=50, pady=5).place(x=80,y=200)

        clas=StringVar()
        e1=Entry(root, textvariable=d, borderwidth=5, font=("bold", 10))
        e1.place(x=400,y=100)
        e2=Entry(root, textvariable=f, borderwidth=5, font=("bold", 10))
        e2.place(x=400,y=150)
        o=OptionMenu(root, c, 'Second Class', 'Third AC', 'Second AC' ,'First AC')
        o.place(x=400,y=200)

        SUB=Button(root, text='Get Fare', font=("bold", 10), padx=15, pady=5, bg='light blue', command=show)
        SUB.place(x=200,y=260)

        Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Ticket)
        Main1.place(x=0,y=0)

    x=LabelFrame(root, relief=RAISED, bg='white', borderwidth=3, padx=10, pady=10)
    x.place(x=100,y=40)
    #BUY FRAME=======================================================
    f=LabelFrame(root, relief=RAISED, bg='white', borderwidth=3, padx=20, pady=20)
    f.place(x=660,y=110)
    #infinity========================================================
    Label(f, text='             ', font=("bold", 10), bg='white').grid(row=3,column=1)
    
    From=Entry(f, textvariable=fr, borderwidth=5, font=("bold", 10))
    From.grid(row=0,column=0)
    Label(f, bg='white').grid(row=1,column=0)
    if fr.get()=='Enter Source Station':
        From.config(fg='red')
    if fr.get()=='':
        From.insert(0,'From*')

    Dest=Entry(f, textvariable=dest, borderwidth=5, font=("bold", 10))
    Dest.grid(row=2,column=0)
    Label(f, bg='white').grid(row=3,column=0)
    if dest.get()=='Enter Destination':
        Dest.config(fg='red')
    if dest.get()=='':
        Dest.insert(0,'To*')

    Date=Entry(f, textvariable=dt, borderwidth=5, font=("bold", 10))
    Date.grid(row=4,column=0)
    Label(f, bg='white').grid(row=5,column=0)
    if dt.get()=='Enter Date':
        Date.config(fg='red')
    if dt.get()=='':
        Date.insert(0,'{}'.format(datetime.date.today()))

    Class=OptionMenu(f, clas, 'Second Class', 'Third AC', 'Second AC' ,'First AC')
    Class.grid(row=6,column=0)

    Label(f, bg='white').grid(row=7,column=0)
    SUB=Button(f, text='Find Trains', font=("bold", 10), bg='SystemButtonFace', command=Show)
    SUB.grid(row=8,column=0)
    #Label(x).grid(row=0,column=0)
    
    Cancel=Button(x, text='Cancel Tickets', font=("bold", 10), relief=GROOVE, padx=20, command=Cancel).grid(row=0,column=0)
    #Cancel.place(x=30,y=150)
    Label(x, bg='white').grid(row=0,column=1)
    
    Pnr=Button(x, text='Check PNR', font=("bold", 10), padx=24, relief=GROOVE, command=PNR).grid(row=0,column=2)
    #pnr.place(x=30,y=200)
    Label(x, bg='white').grid(row=0,column=3)
    
    Fair_en=Button(x, text='Fair Enquiry', font=("bold", 10), padx=25, relief=GROOVE, command=fair).grid(row=0,column=4)
    #Fair_en.place(x=30,y=250)

    # to main
    Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
    Main1.place(x=0,y=0)

    # Refresh
    refresh=Button(root, text='⟲', font=("bold", 10), bg='light blue', padx=10, pady=5, command=Ticket)
    refresh.place(x=847,y=0)


    root.mainloop()




#__________________________________________________________________________________________________________________


    
#__________________________________________________________________________________________________________________



def train():
    global root
    for widget in root.winfo_children():
        widget.destroy()
    
    Tno=IntVar()
    Detail=['','']

    def show():
        try:
            print(Tno.get())
            if Tno.get()/1000<1:
                e1.delete(0, END)
                e1.config(fg='red')
                e1.insert(0,'Enter 4-Digits!!')
            else:
                Detail[0]=Tno.get()
                e1.config(fg='black')
            if Detail[0]=='':
                pass
            else:
                try:
                    db=c.connect(host='localhost', user='root',passwd='123456', database='rail')
                    cur=db.cursor()
                    cur.execute("select * from trains where train_no='{}'".format(Detail[0]))
                    vals=cur.fetchone()
                    Label(x, text='Your Train name : {}\nTrain Number : {}\nSeats : {}'.format(vals[0],vals[1],vals[3]), bg='white', font=('bold',10)).grid(row=2,column=1)
                except TypeError:
                    e1.delete(0, END)
                    e1.config(fg='red')
                    e1.insert(0,'Incorrect Train number')
        except:
            e1.delete(0, END)
            e1.config(fg='red')
            e1.insert(0,'Only Digits!!')
            raise
            
    
    train_image=ImageTk.PhotoImage(Image.open('bginfo.png'))
    tlabel=Label(image=train_image)
    tlabel.place(x=-2,y=-2)

    x=LabelFrame(root, relief=RAISED, bg='white', borderwidth=3, padx=20, pady=20)
    x.place(x=20,y=140)
    Label(x, text='         ', bg='white').grid(row=1,column=1)

    Label(x, text="Enter Train Number", font=("bold", 14), bg='white').grid(row=0,column=0)

    e1=Entry(x, textvariable=Tno, borderwidth=5, width=30, font=("bold", 10))
    e1.grid(row=0,column=2)

    if Tno.get()=='Enter Train no.':
        e1.config(fg='red')
    s=Button(x, text='Confirm', font=("bold", 10), padx=15, pady=5, bg='light blue', command=show)
    s.grid(row=1,column=1)
    
    Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
    Main1.place(x=0,y=0)

    # Refresh
    refresh=Button(root, text='⟲', font=("bold", 10), bg='light blue', padx=10, pady=5, command=train)
    refresh.place(x=847,y=0)

    root.mainloop()

#__________________________________________________________________________________________________________________


    
#__________________________________________________________________________________________________________________


def Food():
    global root, bill
    for widget in root.winfo_children():
        widget.destroy()

    def zero():
        global bill, tea, coff, L, mL, VegBk, NBk, Vmeal, Nmeal
        bill=0
        tea=0
        coff=0
        L=0
        mL=0
        VegBk=0
        NBk=0
        Vmeal=0
        Nmeal=0
        Food()
    def Total(x):
        global bill, tea, coff, L, mL, VegBk, NBk, Vmeal, Nmeal

        if x==7 or x==-7:
            if x>0:
                tea+=1
            elif bill*tea!=0:
                tea-=1
                
        elif x==8 or x==-8:
            if x>0:
                coff+=1
            elif bill*coff!=0:
                coff-=1
                
        elif x==15 or x==-15:
            if x>0:
                L+=1
            elif bill*L!=0:
                L-=1

        elif x==10 or x==-10:
            if x>0:
                mL+=1
            elif bill*mL!=0:
                mL-=1

        elif x==25 or x==-25:
            if x>0:
                VegBk+=1
            elif bill*VegBk!=0:
                VegBk-=1
                
        elif x==35 or x==-35:
            if x>0:
                NBk+=1
            elif bill*NBk!=0:
                NBk-=1

        elif x==50 or x==-50:
            if x>0:
                Vmeal+=1
            elif bill*Vmeal!=0:
                Vmeal-=1

        elif x==55 or x==-55:
            if x>0:
                Nmeal+=1
            elif bill*Nmeal!=0:
                Nmeal-=1

        if bill+x>=0:
            bill+=x
        
        l1=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=50)
        e1 = Entry(root, textvariable=tea, borderwidth=5, font=("bold", 10), width=3)
        e1.place(x=600,y=48)
        e1.delete(0, END)
        e1.insert(0, "{}".format(tea))
        e1 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e1.place(x=708,y=48)
        e1.delete(0, END)
        e1.insert(0, "{}₹".format(tea*7))

        l2=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=81)
        e2 = Entry(root, textvariable=coff, borderwidth=5, font=("bold", 10), width=3)
        e2.place(x=600,y=79)
        e2.delete(0, END)
        e2.insert(0, "{}".format(coff))
        e2 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e2.place(x=708,y=79)
        e2.delete(0, END)
        e2.insert(0, "{}₹".format(coff*8))

        l3=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=153)
        e3 = Entry(root, textvariable=L, borderwidth=5, font=("bold", 10), width=3)
        e3.place(x=600,y=151)
        e3.delete(0, END)
        e3.insert(0, "{}".format(L))
        e3 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e3.place(x=708,y=151)
        e3.delete(0, END)
        e3.insert(0, "{}₹".format(L*15))
        
        l4=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=178)
        e4 = Entry(root, textvariable=mL, borderwidth=5, font=("bold", 10), width=3)
        e4.place(x=600,y=176)
        e4.delete(0, END)
        e4.insert(0, "{}".format(mL))
        e4 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e4.place(x=708,y=176)
        e4.delete(0, END)
        e4.insert(0, "{}₹".format(mL*10))
        
        l5=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=243)
        e5 = Entry(root, textvariable=VegBk, borderwidth=5, font=("bold", 10), width=3)
        e5.place(x=600,y=241)
        e5.delete(0, END)
        e5.insert(0, "{}".format(VegBk))
        e5 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e5.place(x=708,y=241)
        e5.delete(0, END)
        e5.insert(0, "{}₹".format(VegBk*25))
        
        l6=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=278)
        e6 = Entry(root, textvariable=NBk, borderwidth=5, font=("bold", 10), width=3)
        e6.place(x=600,y=276)
        e6.delete(0, END)
        e6.insert(0, "{}".format(NBk))
        e6 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e6.place(x=708,y=276)
        e6.delete(0, END)
        e6.insert(0, "{}₹".format(NBk*35))
        
        l7=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=368)
        e7 = Entry(root, textvariable=Vmeal, borderwidth=5, font=("bold", 10), width=3)
        e7.place(x=600,y=366)
        e7.delete(0, END)
        e7.insert(0, "{}".format(Vmeal))
        e7 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e7.place(x=708,y=366)
        e7.delete(0, END)
        e7.insert(0, "{}₹".format(Vmeal*50))
        
        l8=Label(root, text="Total :          Total Cost:", font=("bold", 10)).place(x=560,y=398)
        e8 = Entry(root, textvariable=Nmeal, borderwidth=5, font=("bold", 10), width=3)
        e8.place(x=600,y=396)
        e8.delete(0, END)
        e8.insert(0, "{}".format(Nmeal))
        e8 = Entry(root, borderwidth=5, font=("bold", 10), width=3)
        e8.place(x=708,y=396)
        e8.delete(0, END)
        e8.insert(0, "{}₹".format(Nmeal*55))
        
        e9 = Entry(root, textvariable=bill, borderwidth=5, font=("bold", 10), width=10)
        e9.place(x=660,y=460)
        e9.delete(0, END)
        e9.config(state='normal')
        e9.insert(0, "{}₹".format(bill))
        e9.config(state='disabled')
    
    # Confirm Order______________


    def confirm():
        global root
        if bill>0:
            for widget in root.winfo_children():
                widget.destroy()
            tn=IntVar()
            sn=IntVar()

            def done():
                try:
                    if tn.get()!= 0:
                        Label(root, text='       '*10).place(x=650,y=165)
                    else:
                        Label(root, text='Enter Train No.', font=("bold", 14), fg='red').place(x=650,y=158)
                except:
                    Label(root, text='       '*10).place(x=650,y=165)
                    Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=158)
                #====================================================================
                try:
                    if sn.get()!= 0:
                        Label(root, text='       '*10).place(x=650,y=245)
                    else:
                        Label(root, text='Enter Seat No.', font=("bold", 14), fg='red').place(x=650,y=238)
                except:
                    Label(root, text='       '*10).place(x=650,y=245)
                    Label(root, text='Only Digits', font=("bold", 14), fg='red').place(x=650,y=238)
                #====================================================================
                try:
                    if tn.get()!=0 and sn.get()!=0:
                        e1.config(state='disabled')
                        e2.config(state='disabled')
                        Label(root, text='CONFIRMED!', font=("bold", 16)).place(x=380,y=350)
                except:
                    pass
            
            Label(root, text="Enter Train Number", font=("bold", 15)).place(x=360,y=120)

            Label(root, text="Enter Seat Number", font=("bold", 15)).place(x=360,y=200)

            e1=Entry(root, textvariable=tn, borderwidth=5, font=("bold", 10))
            e1.place(x=375,y=160)
            e2=Entry(root, textvariable=sn, borderwidth=5, font=("bold", 10))
            e2.place(x=375,y=240)
            
            Button(root, text='Confirm', font=("bold", 10), padx=15, pady=2, bg='light blue', command=done).place(x=390,y=350)

            Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=2, bg='light blue', command=Food)
            Main1.place(x=0,y=0)
        else:
            Food()

    Label(root, text='Total :', font=('bold',14)).place(x=600,y=460)
    
    FOOD=ImageTk.PhotoImage(Image.open('menu.png'))
    label1=Label(image=FOOD)
    label1.place(x=0,y=0)

    add1=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(7))
    add1.place(x=520,y=53)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-7)).place(x=755,y=53)

    add2=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(8))
    add2.place(x=520,y=78)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-8)).place(x=755,y=78)

    add3=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(15))
    add3.place(x=520,y=157)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-15)).place(x=755,y=157)

    add4=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(10))
    add4.place(x=520,y=182)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-10)).place(x=755,y=182)

    add5=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(25))
    add5.place(x=520,y=247)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-25)).place(x=755,y=247)

    add6=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(35))
    add6.place(x=520,y=282)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-35)).place(x=755,y=282)

    add7=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(50))
    add7.place(x=520,y=372)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-50)).place(x=755,y=372)

    add8=Button(root, text='⬆', font=("bold", 8), command=lambda:Total(55))
    add8.place(x=520,y=397)
    Button(root, text='⬇', font=("bold", 8), command=lambda:Total(-55)).place(x=755,y=397)
    
    show=Button(root, text='Next', font=("bold", 12), padx=20, bg='light blue', command=confirm).place(x=400,y=460)
    
    Main1=Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main)
    Main1.place(x=0,y=460)

    # Refresh
    refresh=Button(root, text='⟲', font=("bold", 10), bg='light blue', padx=10, pady=5, command=zero)
    refresh.place(x=847,y=0)

    Total(0)
    root.mainloop()


#____________________________________________________________________________________________________________________


#____________________________________________________________________________________________________________________


def signup():
    global root
    for widget in root.winfo_children():
        widget.destroy()

    def Add_account():
        global logged
        if Gender.get()==1:
            Signup[3]='Male'
        elif Gender.get()==2:
            Signup[3]='Female'
        else:
            pass
        if name.get()=='':
            Label(root, text='Enter Name!!', font=("bold", 10), fg='red').place(x=560, y=130)
        else:
            Signup[0]=name.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=130)
        if mail.get()=='':
            Label(root, text='Enter Email!!', font=("bold", 10), fg='red').place(x=560, y=180)
        else:
            Signup[1]=mail.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=180)
        if age.get()=='':
            Label(root, text='Enter Age!!', font=("bold", 10), fg='red').place(x=560, y=270)
        else:
            Signup[2]=age.get()
            Label(root, text='     '*18, font=("bold", 10), fg='red').place(x=560, y=270)

        if name.get()=='' or mail.get()=='' or age.get()=='' or Signup[3]==None:
            pass
        else:
            db=c.connect(host='localhost', user='root', passwd='123456', database='rail')
            cur=db.cursor()
            cur.execute("insert into email values('{}','{}','{}','{}','{}')".format(Signup[0], Signup[1], Signup[2], Signup[3], 0))
            db.commit()
            logged=True
        if logged:
            Main()
    
    label_0 = Label(root, text="Fill Details",width=20,font=("bold", 20))
    label_0.place(x=280,y=53)


    NAME = Label(root, text="FullName",width=20,font=("bold", 10))
    NAME.place(x=270,y=130)


    name=StringVar()


    Name = Entry(root,textvariable=name)
    Name.place(x=430,y=130)

    MAIL = Label(root, text="Email",width=20,font=("bold", 10))
    MAIL.place(x=258,y=180)


    mail=StringVar()


    Mail = Entry(root,textvariable=mail)
    Mail.place(x=430,y=180)

    GENDER = Label(root, text="Gender",width=20,font=("bold", 10))
    GENDER.place(x=260,y=230)

    Gender = IntVar()

    Radiobutton(root, text="Male",padx = 5, variable=Gender, value=1).place(x=425,y=230)
    Radiobutton(root, text="Female",padx = 20, variable=Gender, value=2).place(x=480,y=230)

    AGE = Label(root, text="Age:",width=20,font=("bold", 10))
    AGE.place(x=260,y=280)


    age=StringVar()

    
    Age = Entry(root,textvariable=age)
    Age.place(x=430,y=280)

    Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main).place(x=0,y=0)
    Button(root, text='Submit', width=20, pady=2.2, bg='light blue', command=Add_account).place(x=370,y=380)

    # Refresh
    refresh=Button(root, text='⟲', font=("bold", 10), bg='light blue', padx=10, pady=5, command=signup)
    refresh.place(x=847,y=0)

#____________________________________________________________________________________________________________________



#____________________________________________________________________________________________________________________



def login():
    global root
    for widget in root.winfo_children():
        widget.destroy()

    def confirm():
        global logged
        try:
            db=c.connect(host='localhost', user='root', passwd='123456', database='rail')
            cur=db.cursor()
            cur.execute("select * from email where mail='{}'".format(mail.get()))
            x=cur.fetchone()
            for i in range(4):
                Signup[i]=x[i]
            db.commit()
        except:
            logged=False
            raise
        if Signup[1]==mail.get():
            logged=True
            Main()
    
    label_0 = Label(root, text="Login",width=20,font=("bold", 20))
    label_0.place(x=180,y=53)

    MAIL = Label(root, text="Email",width=20,font=("bold", 14))
    MAIL.place(x=158,y=178)

    mail=StringVar()
    Mail = Entry(root,textvariable=mail, width=24, borderwidth=5, font=("bold", 10))
    Mail.place(x=330,y=180)

    Button(root, text='◄', font=("bold", 10), padx=15, pady=5, bg='light blue', command=Main).place(x=0,y=0)
    Button(root, text='→', bg='light blue', font=("bold", 10), command=confirm).place(x=506,y=180)

if __name__=='__main__':
    Main()

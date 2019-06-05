from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Management System")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

#=================================================================================
#                  TIME
#================================================================================
localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="GAT CANTEEN ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    #x=random.randint(10908,500876)
    #randomRef=str(x)
    #rand.set(randomRef)

    if (Idly.get()==""):
        CoIdly=0
    else:
        CoIdly=float(Idly.get())


    
    if (Dosa.get()==""):
        CoDosa=0
    else:
        CoDosa=float(Dosa.get())



    if (Kesari.get()==""):
        CoKesari=0
    else:
        CoKesari=float(Kesari.get())



    if (Pulav.get()==""):
        CoPulav=0
    else:
        CoPulav=float(Pulav.get())

        
    if (Karabath.get()==""):
        CoKarabath=0
    else:
        CoKarabath=float(Karabath.get())

     
    if (Drinks.get()==""):
        CoD=0
    else:
        CoD=float(Drinks.get())

                   
    CostofIdly =CoIdly * 25
    CostofDrinks=CoD * 20
    CostofDosa = CoDosa* 35
    CostofKesari = CoKesari * 25
    CostPulav = CoPulav* 35
    CostKarabath=CoKarabath * 20

    CostofMeal= "Rs", str('%.2f' % (CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath))

    PayTax=((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath) * 0.2)

    TotalCost=(CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath)
 
    Ser_Charge= ((CostofIdly+CostofDrinks+CostofDosa+CostofKesari+CostPulav+CostKarabath)/99)

    Service = "Rs", str ('%.2f' % Ser_Charge)

    OverAllCost ="Rs", str ('%.2f' % (PayTax+TotalCost+Ser_Charge))

    PaidTax= "Rs", str ('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    
def qExit():
    root.destroy()

def Reset():
    rand.set("") 
    Idly.set("")
    Dosa.set("")
    Kesari.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Pulav.set("")
    Karabath.set("")
    
#====================================Restaraunt Info 1===========================================================
rand = StringVar()
Idly=StringVar()
Dosa=StringVar()
Kesari=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Pulav=StringVar()
Karabath=StringVar()



lblReference= Label(f1, font=('arial', 16, 'bold'),text="Reference",bd=16,anchor="w")
lblReference.grid(row=0, column=0)
txtReference=Entry(f1, font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=2)

lblIdly= Label(f1, font=('arial', 16, 'bold'),text="Idly",bd=16,anchor="w")
lblIdly.grid(row=1, column=0)
txtIdly=Entry(f1, font=('arial',16,'bold'),textvariable=Idly,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtIdly.grid(row=1,column=2)


lblDosa= Label(f1, font=('arial', 16, 'bold'),text="Dosa",bd=16,anchor="w")
lblDosa.grid(row=2, column=0)
txtDosa=Entry(f1, font=('arial',16,'bold'),textvariable=Dosa,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDosa.grid(row=2,column=2)


lblKesari= Label(f1, font=('arial', 16, 'bold'),text="Kesari bath",bd=16,anchor="w")
lblKesari.grid(row=3, column=0)
txtKesari=Entry(f1, font=('arial',16,'bold'),textvariable=Kesari,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtKesari.grid(row=3,column=2)

lblPulav= Label(f1, font=('arial', 16, 'bold'),text="Pulav",bd=16,anchor="w")
lblPulav.grid(row=4, column=0)
txtPulav=Entry(f1, font=('arial',16,'bold'),textvariable=Pulav,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPulav.grid(row=4,column=2)

lblKarabath= Label(f1, font=('arial', 16, 'bold'),text="Kara Bath",bd=16,anchor="w")
lblKarabath.grid(row=5, column=0)
txtKarabath=Entry(f1, font=('arial',16,'bold'),textvariable=Karabath,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtKarabath.grid(row=5,column=2)

#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lblDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
lblDrinks.grid(row=0, column=4)
txtDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=6)

lblCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
lblCost.grid(row=1, column=4)
txtCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCost.grid(row=1,column=6)


lblService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
lblService.grid(row=2, column=4)
txtService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService.grid(row=2,column=6)


lblStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
lblStateTax.grid(row=3, column=4)
txtStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtStateTax.grid(row=3,column=6)

lblSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
lblSubTotal.grid(row=4, column=4)
txtSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=6)

lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=4)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=6)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command=Ref).grid(row=8,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=8,column=3)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=8,column=5)


root.mainloop()



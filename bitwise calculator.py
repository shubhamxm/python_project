from tkinter import *
import tkinter
top=tkinter.Tk()
res = NONE
def and1(a,b):
    global res
    res = int(a & b)
def or1(a,b):
    global res
    res  = int(a | b)
def not1(a,b):
    global res
    c=a*10
    c=c+b
    res = int(~(c))
def xor1(a,b):
    global res
    res = int((a ^ b))
def result(event=None):
    global top,res,E3
    text = StringVar()
    E3=Entry(top,textvariable=text,bd=5,bg='#4d994d')
    E3.grid(row=4,column=1)
    text.set(str(res))
def exit1(top):
    top.destroy()
def exit2(top):
    top.destroy()
def selected():
    global tfprs
    tfprs = var.get()
def expl(a,b):
    global top,tfprs,res
    binary1 = StringVar()
    binary2 = StringVar()
    top1=tkinter.Toplevel(top)
    value1 = IntVar()
    l1=Label(top1,text="Number 1",bg='#243633',fg='#ffffff').grid(row=0,column=0)
    e1=Entry(top1,textvariable = value1,bd=5,bg='#4d994d')
    value1.set(a)
    e1.grid(row=0,column=1)
    e3=Entry(top1,textvariable = binary1,bd=5,bg='#4d994d')
    l3=Label(top1,text="Binary Number 1",bg='#243633',fg='#ffffff').grid(row=0,column=2)
    binary1.set(format(a,'b'))
    e3.grid(row=0,column=3)
    value2 = IntVar()
    l2=Label(top1,text="Number 2",bg='#243633',fg='#ffffff').grid(row=1,column=0)
    e2=Entry(top1,textvariable = value2,bd=5,bg='#4d994d')
    value2.set(b)
    e2.grid(row=1,column=1)
    l4=Label(top1,text="Binary Number 2",bg='#243633',fg='#ffffff').grid(row=1,column=2)
    e4=Entry(top1,textvariable = binary2,bd=5,bg='#4d994d')
    binary2.set(format(b,'b'))
    e4.grid(row=1,column=3)
    l5=Label(top1,text="Operation",bg='#243633',fg='#ffffff').grid(row=2,column=2) #says text from previous radiobutton selection
    operator = StringVar()
    e5=Entry(top1,textvariable = operator,bd=5,bg='#4d994d')
    operator.set(tfprs)
    operator.set(tfprs)
    e5.grid(row=2,column=3)
    dres = IntVar()
    l6=Label(top1,text="Decimal Result",bg='#243633',fg='#ffffff').grid(row=3,column=1)
    e6=Entry(top1,textvariable = dres ,bd=5,bg='#4d994d')
    dres.set(res)
    e6.grid(row=3,column=2)
    b1=tkinter.Button(top1,bd=5,image=photoimageee,command=lambda top=top1:exit2(top1)).grid(row=4,column=0)
    top1['background']='#243633'
    top1.title('Explanation')
    top.mainloop()
def dotwo(a,b):
    selected()
    expl(a,b)

num1 = IntVar()
L1=Label(top,text="Number 1",bg='#243633',fg='#ffffff').grid(row=0,column=0)
E1=Entry(top,textvariable = num1,bd=5,bg='#4d994d')
num1.set(1)
E1.grid(row=0,column=1)
num2 = IntVar()
L2=Label(top,text="Number 2",bg='#243633',fg='#ffffff').grid(row=0,column=2)
E2=Entry(top,textvariable =num2,bd=5,bg='#4d994d')
num2.set(1)
E2.grid(row=0,column=3)
var=StringVar()

R1=Radiobutton(top,text="AND",variable=var,value="AND",bg='#243633',fg='#ff9900',command=lambda: and1(int(E1.get()),int(E2.get())))
R1.grid(row=1,column=0)
R2=Radiobutton(top,text="OR",variable=var,value="OR",bg='#243633',fg='#ff9900',command=lambda: or1(int(E1.get()),int(E2.get())))
R2.grid(row=1,column=1)
R3=Radiobutton(top,text="NOT",variable=var,value="NOT",bg='#243633',fg='#ff9900',command=lambda: not1(int(E1.get()),int(E2.get())))
R3.grid(row=2,column=0)
R4=Radiobutton(top,text="XOR",variable=var,value="XOR",bg='#243633',fg='#ff9900',command=lambda: xor1(int(E1.get()),int(E2.get())))
R4.grid(row=2,column=1)
label=Label(top)
label.grid()
photo = PhotoImage(file = r'C:\Users\kksja\Desktop\button_result.png')
photoimage = photo.subsample(2,2)
B1=tkinter.Button(top,image=photoimage,command=result)
B1.grid(row=3,column=0)
photoo = PhotoImage(file = r'C:\Users\kksja\Desktop\button_explanation.png')
photoimagee = photoo.subsample(2,2)
B2=tkinter.Button(top,text="Explanation",image=photoimagee,command=lambda:dotwo(int(E1.get()),int(E2.get())),bd=5)
B2.grid(row=3,column=1)
photooo = PhotoImage(file = r'C:\Users\kksja\Desktop\button_exit.png')
photoimageee = photooo.subsample(2,2)
B3=tkinter.Button(top,bd=5,image=photoimageee,command=lambda top=top:exit1(top)).grid(row=3,column=2)
L3=Label(top,text="Result is:",bg='#243633',fg='#ffffff').grid(row=4,column=0)
E3=Entry(top,bd=5,bg='#4d994d')
E3.grid(row=4,column=1)
top['background']='#243633'
top.title('BITWISE CALCULATOR')
top.mainloop()

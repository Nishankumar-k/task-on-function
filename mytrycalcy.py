from tkinter import *

box = Tk()
box.title("Calculator")

f1 = Frame(box)
f2 = Frame(box)
f1.pack()
f2.pack()

e1 = Entry(f1, width=10)
e1.pack(side='left', padx=10, pady=10)

e2 = Entry(f1, width=10)
e2.pack(side='right', padx=20, pady=20)

n1 = e1.get()
n2 = e2.get()


def add():
    k = n1 + n2
    print('the answer for addition is ', k)
    return k


def sub():
    q = n1 - n2
    print('the answer for subtraction is ', q)
    return q


def mul():
    m = n1 * n2
    print('the answer for multiplication is ', m)
    return m


def div():
    n = n1 / n2
    print('the answer for division is ', n)
    return n


def mod():
    p = n1 % n2
    print('the answer for modulus is ', p)
    return p


a = Button(box, text="ADD (+)", command=add)
a.pack(padx=10, pady=20)

b = Button(box, text="SUB (-)", command=sub)
b.pack(padx=20, pady=20)

c = Button(box, text="MUL (*)", command=mul)
c.pack(padx=30, pady=30)

d = Button(box, text="DIV (/)", command=div)
d.pack(padx=40, pady=30)

e = Button(box, text="MOD (%)", command=mod)
e.pack(padx=50, pady=40)

box.geometry('1024x768')
box.mainloop()

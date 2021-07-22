from tkinter import *

root = Tk()

root.title("Calculadora")


display = Frame(root)
display.pack()

num = StringVar(display)
num.set("")
muestra = Label(display, text = num.get(), font=("Helvetica", 16), textvariable = num, bg = "white")
muestra.pack()

entry = Entry(root, textvariable = num)

finNum = False

def cambiarNumero(n):
    numero = 48
    global finNum
    if finNum:
        num.set("")

    if num.get() != "":
        numero = float(num.get())
        numero = numero*10 + n
    else:
        numero = n
    num.set(numero)
    finNum = False

def borrarTodo():
    num.set("")

def borrar():
    numero = 48
    if num.get() != "":
        numero = float(num.get())
        numero = int(numero/10)
    else:
        numero = ""
    if numero == 0:
        numero = ""
    num.set(numero)

top = Frame(root)
top.pack()


izq = Frame(top)
izq.pack(side = LEFT)

opciones = Frame(izq)
opciones.pack()

clear = Button(opciones, text = "Borrar todo", font=("Helvetica", 16), command = borrarTodo)
clear.pack(side = RIGHT)

delete = Button(opciones, text = "Borrar", font=("Helvetica", 16), command = borrar)
delete.pack(side = LEFT)

numeros = Frame(izq)
numeros.pack()

for i in range(10):
    if i != 0:
        n = Button(numeros, text = str(i), font=("Helvetica", 16), command = lambda i=i: cambiarNumero(i))
        row = int((i-1)/3+1)
        column = int((i-1)%3+1)
        n.grid(row = row, column = column)
    elif i == 0:
        n = Button(numeros, text = str(i), font=("Helvetica", 16), command = lambda i=i: cambiarNumero(i))
        n.grid(row = 4, column = 2)

num.set("")

der = Frame(top)
der.pack(side = RIGHT)

operacion = StringVar()
operacion.set("")

numeroViejo = StringVar()
numeroViejo.set("")

def suma():
    global finNum
    operacion.set("suma")
    numeroViejo.set(num.get())
    finNum = True

def resta():
    global finNum
    operacion.set("resta")
    numeroViejo.set(num.get())
    finNum = True


def multiplicacion():
    global finNum
    operacion.set("multiplicacion")
    numeroViejo.set(num.get())
    finNum = True


def division():
    global finNum
    operacion.set("division")
    numeroViejo.set(num.get())
    finNum = True

def igual():
    global finNum
    n1 = float(numeroViejo.get())
    n2 = float(num.get())
    op = operacion.get()

    if n1 == "":
        num.set(n2)
    
    elif n2 == "":
        num.set(n2)

    elif op == "suma":
        num.set(n1+n2)
    
    elif op == "resta":
        num.set(n1-n2)
    
    elif op == "multiplicacion":
        num.set(n1*n2)

    elif op == "division":
        if n2 == 0:
            num.set("No se puede dividir por 0")
        else:
            num.set(n1/n2)
    
    finNum = True

pady = 0
padx = 10

mas = Button(der, text = "+", font=("Helvetica", 16), command = suma, width = 3, height=2)
#mas.pack(pady = pady, padx = padx)
mas.grid(row = 0, column = 0)

menos = Button(der, text = "-", font=("Helvetica", 16), command = resta, width = 3, height=2)
#menos.pack(pady = pady, padx = padx)
menos.grid(row = 0, column = 1)

por = Button(der, text = "*", font=("Helvetica", 16), command = multiplicacion, width = 3, height=2)
#por.pack(pady = pady, padx = padx)
por.grid(row = 1, column = 0)

sobre = Button(der, text = "/", font=("Helvetica", 16), command = division, width = 3, height=2)
#sobre.pack(pady = pady, padx = padx)
sobre.grid(row = 1, column = 1)

bot = Frame(root)
bot.pack()

equal = Button(bot, text = "=", font=("Helvetica", 16), width = 20, command = igual)
equal.pack()


root.mainloop()

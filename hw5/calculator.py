from tkinter import *
from sympy import *
window = Tk()
window.title('CALCULATOR')
window.geometry('250x380')
window.resizable(False, False)
window["bg"] = "black"
expression = ''
result = 0
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def f(s):
    global result
    global expression
    E1['state'] = 'normal'
    if expression == '':
        E1.delete(0, END)
    if s == 'C':
        E1.delete(0, END)
        s = ''
    elif s == 'DEL':
        expression = expression[:-1]
        E1.delete(0, END)
        E1.insert(0, expression)
        s = ''
    elif s == '=':
        try:
            result = eval(expression)
            E1.delete(0, END)
            E1.insert(0, float(result))
        except:
            E1.delete(0, END)            
            E1.insert(0, 'SYNTAX ERROR')

    #elif s == '!':
     #   expression = E1.get() + 'factorial'
    
    if s == '=' or s == 'SYNTAX ERROR':
        expression = ''
    else:
        expression = E1.get() + s
        E1.delete(0, END)
        E1.insert(0, expression)
    E1['state'] = 'readonly'

E1 = Entry(window, justify = RIGHT, state = "readonly", font = ("Times New Roman", 15))
Bclear =  Button(window, text = 'C', command = lambda: f('C'))
Bsin =  Button(window, text = 'sin', command = lambda: f('sin'))
Bcos =  Button(window, text = 'cos', command = lambda: f('cos'))
Btan  =  Button(window, text = 'tan', command = lambda: f('tan'))
Basin =  Button(window, text = 'asin', command = lambda: f('asin'))
Bacos =  Button(window, text = 'acos', command = lambda: f('acos'))
Batan  =  Button(window, text = 'atan', command = lambda: f('atan'))

Bbr1 =  Button(window, text = '(', command = lambda: f('('))
Bbr2 =  Button(window, text = ')', command = lambda: f(')'))
Bpi =  Button(window, text = 'pi', command = lambda: f('pi'))
Be  =  Button(window, text = 'E', command = lambda: f('E'))


Bpower =  Button(window, text = '**', command = lambda: f('**'))
Bfact =  Button(window, text = 'factorial', command = lambda: f('factorial'))
Bsqroot  =  Button(window, text = 'sqrt', command = lambda: f('sqrt'))
Blog  =  Button(window, text = 'log', command = lambda: f('log'))
B7  =  Button(window, text = '7', command = lambda: f('7'))
B8  =  Button(window, text = '8', command = lambda: f('8'))
B9  =  Button(window, text = '9', command = lambda: f('9'))
B4  =  Button(window, text = '4',command = lambda: f('4'))
B5  =  Button(window, text = '5', command = lambda: f('5'))
B6  =  Button(window, text = '6', command = lambda: f('6'))
B1  =  Button(window, text = '1', command = lambda: f('1'))
B2  =  Button(window, text = '2', command = lambda: f('2'))
B3  =  Button(window, text = '3', command = lambda: f('3'))
B0  =  Button(window, text = '0', command = lambda: f('0'))
Bdot  =  Button(window, text = '.', command = lambda: f('.'))
Bdel  =  Button(window, text = 'DEL', command = lambda: f('DEL'))
Bmul  =  Button(window, text = '*', command = lambda: f('*'))
Bdiv  =  Button(window, text = '/', command = lambda: f('/'))
Bminus =  Button(window, text = '-', command = lambda: f('-'))
Bplus  =  Button(window, text = '+', command = lambda: f('+'))
Bequal  =  Button(window, text = '=', command = lambda: f('='))
Bcomma  =  Button(window, text = ',', command = lambda: f(','))

E1.place(x = 10, y = 10, width = 230, height = 40)

Bsin.place(x = 10, y = 60, width = 55, height = 28.75)
Bcos.place(x = 70, y = 60, width = 55, height = 28.75)
Btan.place(x = 130, y = 60, width = 55, height = 28.75)
Bclear.place(x = 190, y = 60, width = 55, height = 28.75)

Basin.place(x = 10, y = 93.75, width = 55, height = 28.75)
Bacos.place(x = 70, y = 93.75, width = 55, height = 28.75) 
Batan.place(x = 130, y = 93.75, width = 55, height = 28.75)
Bdel.place(x = 190, y = 93.75, width = 55, height = 28.75)



Bpower.place(x = 10, y = 127.5, width = 55, height = 28.75)
Bfact.place(x = 70, y = 127.5, width = 55, height = 28.75)
Bsqroot.place(x = 130, y = 127.5, width = 55, height = 28.75)
Blog.place(x = 190, y = 127.5, width = 55, height = 28.75)

Bbr1.place(x = 10, y = 161.25, width = 55, height = 28.75)
Bbr2.place(x = 70, y = 161.25, width = 55, height = 28.75) 
Bpi.place(x = 130, y = 161.25, width = 55, height = 28.75)
Be.place(x = 190, y = 161.25, width = 55, height = 28.75)

B7.place(x = 10, y = 195, width = 55, height = 40)
B8.place(x = 70, y = 195, width = 55, height = 40)
B9.place(x = 130, y = 195, width = 55, height = 40)
Bplus.place(x = 190, y = 195, width = 55, height = 40)

B4.place(x = 10, y = 240, width = 55, height = 40) 
B5.place(x = 70, y = 240, width = 55, height = 40)
B6.place(x = 130, y = 240, width = 55, height = 40)
Bminus.place(x = 190, y = 240, width = 55, height = 40)

B1.place(x = 10, y = 285, width = 55, height = 40)
B2.place(x = 70, y = 285, width = 55, height = 40)
B3.place(x = 130, y = 285, width = 55, height = 40)
Bdiv.place(x = 190, y = 285, width = 55, height = 40)

B0.place(x = 10, y = 330, width = 55, height = 40)
Bdot.place(x = 70, y = 330, width = 27.5, height = 40)
Bcomma.place(x = 97.5, y = 330, width = 27.5, height = 40)
Bequal.place(x = 130, y = 330, width = 55, height = 40)
Bmul.place(x = 190, y = 330, width = 55, height = 40)


window.mainloop()
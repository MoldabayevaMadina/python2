import re
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
def closing():
    answer = mb.askyesno(
        title = "Closing", 
        message = "Are you sure you want to leave?")
    if answer:
        for w in windows:
            w.destroy()
def go_back(prev_window, cur_window):
    cur_window.withdraw()
    prev_window.deiconify()
#def asymp(f, a, b):
#    for i in np.arrange(a-0.1, b+0.1, 0.1):
#        if eval(subs(f, i - 0.00001))
def validity(f):
    try:
        eval(subs(f, 7))
    except ZeroDivisionError:
        pass
    except:
        return False
    else:
        return True
def valid_interval(f, a, b):
    try:
        a = float(a)
        b = float(b)
        eval(subs(f, a))
        eval(subs(f, b))
    except:
        return False
    else:
        if a > b:
            return False
        return True
def integral_answer(main_window, Efunc, Ea, Eb):
    f = Efunc.get()
    a = Ea.get()
    b = Eb.get()
    if f == '' or a == '' or b == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    elif not validity(f):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid function')
    elif not valid_interval(f, a, b):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid interval')
    else:
        a = float(a)
        b = float(b)
        answer = calc_integ(f, a, b)
        main_window.withdraw()
        integral_ans_window = Tk()
        integral_ans_window.title('INTEGRAL')
        integral_ans_window.geometry('500x250')
        integral_ans_window.resizable(False, False)
        integral_ans_window["bg"] = "peachpuff"
        integral_ans_window.wm_geometry("+%d+%d" % (370, 100))
        windows.append(integral_ans_window)
        integral_ans_window.protocol("WM_DELETE_WINDOW", closing)
        Label(integral_ans_window, text = 'Calculation of definite integral', font = ("Arial", 14), background = "peachpuff", fg = 'black').place(x = 170, y = 30)
        if isinstance(answer, str):
            Button(integral_ans_window, text = 'Back', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, integral_ans_window)).place(x = 50, y = 200, width = 50, height = 20)
            Label(integral_ans_window, text = f' {answer}', font = ("Arial", 14), background = "peachpuff", fg = 'black').place(x = 30, y = 70)
        else:
            Label(integral_ans_window, text = '∫', font = ("Arial", 30), background = "peachpuff", fg = 'black').place(x = 50, y = 75)
            Label(integral_ans_window, text = f'({f})dx = {answer}', font = ("Arial", 14), background = "peachpuff", fg = 'black').place(x = 63, y = 79)
            Button(integral_ans_window, text = 'Back', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, integral_ans_window)).place(x = 50, y = 200, width = 50, height = 20)
            Button(integral_ans_window, text = 'Show steps', font = ("Arial", 12), background = "white", command = lambda: integral(integral_ans_window, f, a, b, answer)).place(x = 50, y = 150, width = 110, height = 30)
            Label(integral_ans_window, text = f'{a}', font = ("Arial", 8), background = "peachpuff", fg = 'black').place(x = 52, y = 116)
            Label(integral_ans_window, text = f'{b}', font = ("Arial", 8), background = "peachpuff", fg = 'black').place(x = 52, y = 55)

        integral_ans_window.mainloop()
def calc_integ(f, a, b):
    out = domain(f, a, b)[1]
    list1 = []
    list_of_i = []
    i = a
    if len(out) == 0:
        while i <= b:
            list_of_i.append(i)
            i += 0.001
        for j in range(len(list_of_i)):
            if j == 0 or j == len(list_of_i) - 1:
                list1.append(eval(subs(f, list_of_i[j])))
            elif j % 2 == 0:
                list1.append(2 * eval(subs(f, list_of_i[j])))
            else:
                list1.append(4 * eval(subs(f, list_of_i[j])))
        return round(sum(list1) * 0.001 / 3, 7)
    else: 
        return 'It is impossible to calculate integral on this interval'

def integral(integral_ans_window, f, a, b, answer):
    integral_ans_window.withdraw()
    integral_window = Toplevel()
    integral_window.title('INTEGRAL')
    integral_window.geometry('550x400')
    integral_window.resizable(False, False)
    integral_window["bg"] = "peachpuff"
    integral_window.wm_geometry("+%d+%d" % (370, 100))
    im1 = ImageTk.PhotoImage(file = 'im1.png')

    integral_window.protocol("WM_DELETE_WINDOW", closing)
    Label(integral_window, text = 'Calculation of definite integral', font = ("Arial", 14), background = "peachpuff", fg = 'black').place(x = 150, y = 30)
    Button(integral_window, text = 'Back', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, integral_window)).place(x = 50, y = 360, width = 50, height = 20)
    Label(integral_window, text = 'Geometric meaning of integral is the area under the function. Therefore we ', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 10, y = 70)
    Label(integral_window, text = 'will find the approximate value of area under graph using formula', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 10, y = 90)
    Label(integral_window, image = im1).place(x = 25, y = 120)
    Label(integral_window, text = f'Area = (0.001/3) * (f({a}) + 4 * f({a+0.001}) + 2*f({a+0.002}) + ... + f({b})) = {answer}', background = "peachpuff", fg = 'black', font = ("Arial", 11)).place(x = 25, y = 190)
    

    integral_window.mainloop()
    

def subs(s, x0):
    f = ''
    #print(s, '..............')
    for i in s:
        if i == 'x':
            f += f'({str(x0)})'
        else:
            f += i
    #print(f, ';;;;;;;;;')
    return f


def deriv(f):
    if f == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    else:
        df = '('
        for i in f:
            if i == 'x':
                df += '(x + 0.0000000001)'
            else:
                df += i
        df += f' - {f}) / 0.0000000001'
        
        #df = '-f(x+0.00002)+8*f(x+0.00001)-8*f(x-0.00001)+f(x-0.00002)'
        #print(df,'???')
        return df
def deriv2(f):
    if f == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    else:
        df = '('
        for i in f:
            if i == 'x':
                df += '(x + 0.000001)'
            else:
                df += i
        df += f' - 2 * ({f}) + '
        for i in f:
            if i == 'x':
                df += '(x - 0.000001)'
            else:
                df += i
        df += ') / 0.000001**2'
        #df = '-f(x+0.00002)+8*f(x+0.00001)-8*f(x-0.00001)+f(x-0.00002)'
        
        return df
def inc_dec(f, df, points, a, b):
    inc = []
    dec = []
    out = domain(f, a, b)[1]
    if len(points) > 0:
        for i in points:
            if i > a and i < b:
                ##print('rrrrrrrrrrr', eval(subs(df, i - 0.0001)))
                if eval(subs(df, i - 0.0001)) > 0:
                    inc.append([a, i])
                else:
                    dec.append([a, i])
    if len(out) > 0:
        for i in out:
            if i > a and i < b:
                if eval(subs(df, i - 1)) > 0:
                    inc.append([a, i])
                else:
                    dec.append([a, i])
            
    ##print(points, '&&&')
    if eval(subs(df, b)) > 0:
        inc.append([points[-1], b])
    else:
        dec.append([points[-1], b])
    ##print(inc)
    ##print(dec)
    return inc, dec
def domain(f, a, b):
    i = a
    D = []
    out = []
    while i <= b:
        try:
            eval(subs(f, round(i, 4)))
        except:
            out.append(round(i, 4))
        else:
            if 'I' not in str(eval(subs(f, round(i, 4)))) and 'z' not in str(eval(subs(f, round(i, 4)))):
                D.append(round(i, 4))
            else:
                out.append(round(i, 4))
        i+=0.0001
    return D, out
def find_extreme_p(main_window, Efunc, Ea, Eb):
    a = Ea.get()
    b = Eb.get()
    f = Efunc.get()
    if f == '' or a == '' or b == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    elif not validity(f):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid function')
    elif not valid_interval(f, a, b):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid interval')
    else:
        a = float(a)
        b = float(b)
        points = []
        D = domain(f, a, b)[0]
        df = deriv(f)
        asymp = []
        min1 = []
        max1 = []
        infl_p = []
        #print(D)
        for i in D:
            ##print(i, '@8@8@')
            try:
                eval(subs(df, round(i, 4)))
            except ZeroDivisionError:
                points.append(round(i, 2))
            else:
                ##print('---------')
                ##print(round(eval(subs(df, round(i, 4))), 4))
                #print(round(eval(subs(df, round(i, 3))), 9), '^')
                if round(eval(subs(df, round(i, 4))), 4) == 0:
                    ##print('@@@')
                    points.append(round(i, 2))
                    i+=1
            i+=1
            ##print('**********')
            points = set(points)
            points = list(points)
                #print(i, '^^')
        ##print(points, '&&&')
        #inc_dec(f, df, points, a, b)
        df2 = deriv2(f)
        ##print('999999', eval(subs(df2, 1.5708)))
        if len(points) > 0:
            for i in points:
                try:
                    eval(subs(df2, i))
                except ZeroDivisionError:
                    #asymp.append(i)
                    pass
                else:
                    ##print(i)
                    ##print('ooo', round(eval(subs(df2, round(i, 4))), 4))
                    if round(eval(subs(df2, round(i, 4))), 4) > 0:
                        min1.append(i)
                    elif round(eval(subs(df2, round(i, 4))), 4) < 0:
                        max1.append(i)
                    else:
                        infl_p.append(i) 
        concave_d = []
        concave_u = []
        if len(infl_p) > 0:
            for i in infl_p:
                if a < i < b:
                    ##print('i=', i)
                    ##print(round(eval(subs(df2, i-0.1)), 4), 'yyyyyyyyyyyyy')
                    if round(eval(subs(df2, i-0.1)), 4) > 0:
                        concave_u.append([a, i])
                    elif round(eval(subs(df2, i-0.1)), 4) < 0:
                        concave_d.append([a, i])
            if round(eval(subs(df2, b-0.1)), 4) > 0:
                ##print(round(eval(subs(df2, i-0.1)), 4), 'ttttttttt')
                concave_u.append([infl_p[-1], b])
            elif round(eval(subs(df2, b-0.1)), 4) < 0:
                ##print(round(eval(subs(df2, i-0.1)), 4), 'eeeeeeeee')
                concave_d.append([infl_p[-1], b])
        else:
            ##print(round(eval(subs(df2, (a+b)/2)), 3), 'kkkkkkkkk')
            ##print(subs(df2, (a+b)/2), 'jjj')
            if round(eval(subs(df2, (a+b+0.1)/2)), 4) > 0:
                concave_u.append([a, b])
            elif round(eval(subs(df2, (a+b+0.1)/2)), 4) < 0:
                concave_d.append([a, b])
        ##print(min1)
        ##print(max1)
        ##print(infl_p, '+++')
    
        main_window.withdraw()
        exrteme_window = Tk()
        exrteme_window.title('Extreme_points')
        exrteme_window.geometry('720x500')
        exrteme_window.resizable(False, False)
        exrteme_window["bg"] = "peachpuff"
        exrteme_window.wm_geometry("+%d+%d" % (300, 50))
        windows.append(exrteme_window)
        exrteme_window.protocol("WM_DELETE_WINDOW", closing)
        Label(exrteme_window, text = f'Analysis of function f(x) = {f} on interval [{a};{b}]', font = ("Arial", 14), background = "peachpuff", fg = 'black').place(x = 100, y = 30)
        Label(exrteme_window, text = "STEP1. Find values of X where function doesn't exist.", font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 60)
        if len(domain(f, a, b)[1]) != 0:
            Label(exrteme_window, text = f"For f(x) = {f} discontinuity points are: {domain(f, a, b)[1]}", font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 80)
        else:
            Label(exrteme_window, text = f'For f(x) = {f} there are no discontinuity points on the given interval.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 80)
        Label(exrteme_window, text = "STEP2. Find values of X where derivative of function doesn't exist or equals 0. These will ", font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 100)
        if len(points) == 0 and len(domain(f, a, b)[1]) == 0:
            Label(exrteme_window, text = f'be critical points. For f(x) = {f} there are no critical points on the given interval,', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 120)
            Label(exrteme_window, text = f'therefore function f(x) = {f} is monotonic.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 140)
            Label(exrteme_window, text = 'STEP3. Find min and max. Find whether the function is increasing or decreasing.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 160)
            Label(exrteme_window, text = 'Function is monotonic, so minimum and maximum are on the ends of interval.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 180)
            Label(exrteme_window, text = f'For f(x) = {f}, at x = {a} -> y = {round(eval(subs(f, a)), 5)}, at x = {b} -> y = {round(eval(subs(f, b)), 5)}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 200)
            if eval(subs(f, a)) > eval(subs(f, b)):
                Label(exrteme_window, text = f'f({a}) is greater than f({b}) => min is [{b},{round(eval(subs(f, b)), 5)}], max is [{a},{round(eval(subs(f, a)), 5)}]', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 220)
                Label(exrteme_window, text = f'Therefore function is decreasing on the given interval', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 240)

            elif eval(subs(f, a)) < eval(subs(f, b)):
                Label(exrteme_window, text = f'f({b}) is greater than f({a}) => min is [{a},{round(eval(subs(f, a)), 5)}], max is [{b},{round(eval(subs(f, b)), 5)}]', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 220)
                Label(exrteme_window, text = f'Therefore function is increasing on the given interval', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 240)
            
            else:
                Label(exrteme_window, text = f'f({b}) is equal to f({a}) => no min, no max', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 220)
                Label(exrteme_window, text = f'Therefore function is constant on the given interval', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 240)
            
            
            if len(concave_u) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no intervals where function is concave up', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 260)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} intervals where function is concave up: {concave_u}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 260)
            if len(concave_d) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no intervals where function is concave down', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 280)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} intervals where function is concave down: {concave_d}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 280)
            
    #Label(exrteme_window, text = '3rd step. Find whether the function is increasing or decreasing.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 70)
    #Label(exrteme_window, text = 'For this we need to find the sign of first derivative in the interval.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 70)

        elif len(points) != 0 and len(domain(f, a, b)[1]) == 0:
            Label(exrteme_window, text = f'be critical points. For f(x) = {f} critical points: {points}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 120)
            Label(exrteme_window, text = 'STEP3. Find min, max, inflection points. Find whether the function is increasing or decreasing.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 30, y = 140)
            Label(exrteme_window, text = "We need do find sign of second derivative at each critical point. If f''(x0) > 0, then ", font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 160)
            Label(exrteme_window, text = "x0 - min, if f''(x0) < 0, then x0 - max, if f''(x0) = 0, then x0 - inflection point", font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 180)

            if len(min1) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no minimum points', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 200)
            else:
                min2 = []
                for i in min1:
                    min2.append([i, round(eval(subs(f, i)), 5)])
                Label(exrteme_window, text = f'For f(x) = {f} minimum points: {min2}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 200)
            if len(max1) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no maximum points', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 220)
            else:
                max2 = []
                for i in max1:
                    max2.append([i, round(eval(subs(f, i)), 5)])
                Label(exrteme_window, text = f'For f(x) = {f} maximum points: {max2}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 220)
            if len(infl_p) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no inflection points', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 240)
            else:
                infl_p2 = []
                for i in infl_p:
                    infl_p2.append([i, round(eval(subs(f, i)), 5)])
                Label(exrteme_window, text = f'For f(x) = {f} inflection points: {infl_p}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 240)
            ##print(inc_dec(f, df, points, a, b))
            if len(inc_dec(f, df, points, a, b)[0]) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no increasing intervals', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 260)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} increasing intervals: {inc_dec(f, df, points, a, b)[0]}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 260)
            if len(inc_dec(f, df, points, a, b)[1]) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no decreasing intervals', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 280)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} decreasing intervals: {inc_dec(f, df, points, a, b)[1]}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 280)
            
            if len(concave_u) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no intervals where function is concave up', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 300)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} intervals where function is concave up: {concave_u}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 300)
            if len(concave_d) == 0:
                Label(exrteme_window, text = f'For f(x) = {f} there are no intervals where function is concave down', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 320)
            else:
                Label(exrteme_window, text = f'For f(x) = {f} intervals where function is concave down: {concave_d}', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 320)
            
        elif len(domain(f, a, b)[1]) != 0:
            Label(exrteme_window, text = f'be critical points. For f(x) = {f} it is impossiblr to find critical points on the given interval,', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 120)
            
            Label(exrteme_window, text = f'because function is discontinuous.', font = ("Arial", 11), background = "peachpuff", fg = 'black').place(x = 50, y = 140)
        Button(exrteme_window, text = 'Back', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, exrteme_window)).place(x = 50, y = 450, width = 50, height = 20)

        exrteme_window.mainloop()


def graph(Efunc, Ea, Eb):
    a = Ea.get()
    b = Eb.get()
    f = Efunc.get()
    
    
    if f == '' or a == '' or b == '':
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please fill all spaces')
    elif not validity(f):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid function')
    elif not valid_interval(f, a, b):
        mb.showinfo(
            title = 'ERROR', 
            message = 'Please enter valid interval')
    else:
        a = float(a)
        b = float(b)
        D = domain(f, a, b)[0]
        list_y = []
        #list_x = np.arange(a, b + 0.001, 0.001
        for i in D:
            list_y.append(eval(subs(f, i)))
        #fig = plt.figure()
        #ax = fig.add_subplot(1, 1, 1)
        #ax.spines['left'].set_position('center')
        #ax.spines['bottom'].set_position('center')
        #ax.spines['right'].set_color('none')
        #ax.spines['top'].set_color('none')
        ##print(D)
        ##print()
        ##print(list_y)
        plt.grid(True)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.plot(D, list_y)
        plt.title(f'f(x) = {f}')
        plt.show()
def instruction(main_window):
    main_window.withdraw()
    instruction_window = Tk()
    instruction_window.title('MAIN WINDOW')
    instruction_window.geometry('500x400')
    instruction_window.resizable(False, False)
    instruction_window["bg"] = "peachpuff"
    instruction_window.wm_geometry("+%d+%d" % (370, 100))
    windows.append(instruction_window)
    instruction_window.protocol("WM_DELETE_WINDOW", closing)
    Label(instruction_window, text = 'Use this format when entering function', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 20)
    Label(instruction_window, text = 'ln(x) - natural logarithm', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 270)
    Label(instruction_window, text = 'log(x,a) - logarithm, a - base', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 300)
    Label(instruction_window, text = 'cos(x) - cosine', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 60)
    Label(instruction_window, text = 'sin(x) - sine', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 90)
    Label(instruction_window, text = 'tan(x) - tangent', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 120)
    Label(instruction_window, text = '. - for float numbers', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 150)
    Label(instruction_window, text = '** - power', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 240)
    Label(instruction_window, text = 'pi - constant', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 60)
    Label(instruction_window, text = 'E - constant', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 90)
    Label(instruction_window, text = '/ - division', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 120)
    Label(instruction_window, text = '* multiplication', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 150)
    Label(instruction_window, text = '+ sum', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 180)
    Label(instruction_window, text = '- substraction', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 210)
    #Label(instruction_window, text = '. - for float numbers', font = ("Arial", 14), background = "peachpuff").place(x = 50, y = 300)
    Label(instruction_window, text = 'asin(x)', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 180)
    Label(instruction_window, text = 'acos(x)', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 210)
    Label(instruction_window, text = 'atan(x)', font = ("Arial", 14), background = "peachpuff").place(x = 270, y = 240)

    Button(instruction_window, text = 'Back', font = ("Arial", 12), background = "white", command = lambda: go_back(main_window, instruction_window)).place(x = 50, y = 360, width = 50, height = 20)

    instruction_window.mainloop()

main_window = Tk()
main_window.title('MAIN WINDOW')
main_window.geometry('500x400')
main_window.resizable(False, False)
main_window["bg"] = "peachpuff"
main_window.wm_geometry("+%d+%d" % (370, 100))
windows = [main_window]




Label(main_window, text = 'CALCULATOR', font = ("Arial", 20), background = "peachpuff").place(x = 170, y = 20)
Label(main_window, text = 'Enter function:  F(x) = ', font = ("Arial", 14), background = "peachpuff").place(x = 10, y = 170)
Label(main_window, text = 'Enter interval:', font = ("Arial", 14), background = "peachpuff").place(x = 10, y = 210)
Label(main_window, text = ' -', font = ("Arial", 14), background = "peachpuff").place(x = 180, y = 210)

Efunc = Entry(main_window,  background = "lavenderblush")
Efunc.place(x = 200, y = 170, width = 260, height = 30)
Ea = Entry(main_window,  background = "lavenderblush")
Ea.place(x = 140, y = 210, width = 40, height = 30)
Eb = Entry(main_window,  background = "lavenderblush")
Eb.place(x = 200, y = 210, width = 40, height = 30)

#Button(main_window, text = 'Back', font = ("Arial", 10), background = "white", command = lambda: go_back(main_window,window_user_name)).place(x = 20, y = 260, width = 50, height = 20)
Button(main_window, text = 'Function analysis', font = ("Arial", 12), background = "white", command = lambda: find_extreme_p(main_window, Efunc, Ea, Eb)).place(x = 50, y = 260, width = 150, height = 30)
Button(main_window, text = 'Find integral', font = ("Arial", 12), background = "white", command = lambda: integral_answer(main_window, Efunc, Ea, Eb)).place(x = 50, y = 300, width = 150, height = 30)
Button(main_window, text = 'See instruction', font = ("Arial", 12), background = "white", command = lambda: instruction(main_window)).place(x = 300, y = 300, width = 150, height = 30)
Button(main_window, text = 'See the graph', font = ("Arial", 12), background = "white", command = lambda: graph(Efunc, Ea, Eb)).place(x = 300, y = 260, width = 150, height = 30)
Label(main_window, text = 'This program searches for extreme point, intervals where function is  ', font = ("Arial", 11), background = "peachpuff").place(x = 10, y = 70)
Label(main_window, text = 'increasing and decreasing, intevals where function is concave up and', font = ("Arial", 11), background = "peachpuff").place(x = 10, y = 90)
Label(main_window, text = 'concave down, also program calculates the integral and shows the graph.', font = ("Arial", 11), background = "peachpuff").place(x = 10, y = 110)
Label(main_window, text = 'of entererd fuction', font = ("Arial", 11), background = "peachpuff").place(x = 10, y = 130)


main_window.protocol("WM_DELETE_WINDOW", closing)
main_window.mainloop()

import playsound
import math
from tkinter import *

def sound(arg):
    if arg=="start":
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/beam.mp3', block=False)
    elif arg == 1:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/one.mp3', block=False)
    elif arg == 2:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/two.mp3', block=False)
    elif arg == 3:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/three.mp3', block=False)
    elif arg == 4:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/four.mp3', block=False)
    elif arg == 5:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/five.mp3', block=False)
    elif arg == 6:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/six.mp3', block=False)
    elif arg == 7:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/seven.mp3', block=False)
    elif arg == 8:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/eight.mp3', block=False)
    elif arg == 9:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/nine.mp3', block=False)
    elif arg == 0:
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/zero.mp3', block=False)
    elif arg == '/':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/divide.mp3', block=False)
    elif arg == '+':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/plus.mp3', block=False)
    elif arg == '-':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/minus.mp3', block=False)
    elif arg == '*':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/multiple.mp3', block=False)
    elif arg == '=':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/equals.mp3', block=False)
    elif arg == '.':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/point.mp3', block=False)
    elif arg == 'C':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/clear.mp3', block=False)
    elif(arg == 'B'):
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/back.mp3', block=False)
    elif arg == '%':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/percent.mp3', block=False)
    elif arg == "Ans":
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/ans.mp3', block=False)
    elif arg == 'e':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/expo.mp3', block=False)
    elif arg == 'log':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/log.mp3', block=False)
    elif arg == 'antilog':
        playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/antilog.mp3', block=False)
    else:
        print("Sorry something went wrong")

def declare_var():
    global calc, op, ans, trueop, logop, base, isLog, isAntilog, num, screen, antilogop
    calc = Tk()
    op = ""
    ans = ""
    trueop = ""
    logop = ""
    antilogop = ""
    base = math.e
    isLog = False
    isAntilog = False
    num = StringVar()
    calc.configure(background="gray")
    calc.title("Very Sophisticated Simple Calculator")
    screen = Entry(calc, font=('comic sans', 40, 'bold'), textvariable = num, bg="gray", justify='right', state='disabled').grid(columnspan=5)

def onClick(operator):
    global op, trueop
    if len(op)>20:
        op=""
        trueop=""
        num.set("INF")
    else:
        trueop += str(operator)
        op += str(operator)
        num.set(op)

def onClear():
    global op, trueop
    op = ""
    trueop = ""
    num.set(op)

def onEqual():
    global op, trueop, ans, isLog, base, logop, isAntilog, antilogop
    if isLog == True:
        try:
            trueop = str(round(eval(logop + str(math.log(eval(trueop), base))), 4))
            op = trueop
            logop = ""
            isLog = False
            ans = op
            num.set(op)
        except:
            op = ""
            trueop = ""
            logop = ""
            isLog = False
            num.set("Invalid Input")
    elif isAntilog == True:
        try:
            trueop = str(round(eval(antilogop + str(10**eval(trueop))), 4))
            op = trueop
            antilogop = ""
            isAntilog = False
            ans = op
            num.set(op)
        except:
            op = ""
            trueop = ""
            logop = ""
            isLog = False
            num.set("Invalid Input")
    else:
         try:
            trueop = str(round(eval(trueop), 4))
            if len(trueop) > 20 :
                op = ""
                trueop = ""
                num.set("INF")
            else:
                op = trueop
                num.set(op)
                ans = trueop
         except:
            num.set("Invalid Input")

def onAns():
    global op, trueop, ans
    op += ans
    trueop += ans
    num.set(op)

def onPercent():
    global op, trueop
    try:
        num.set(str(eval(trueop)))
        op += "% * "
        num.set(op)
        trueop = str(float(trueop)/100) + "*"
    except:
        op = ""
        trueop = ""
        num.set("Invalid Input")                #Need to check why percent doesn't work with float

def onDecimal():
    global op, trueop
    if(op.count(".") == 0):
        op += "."
        trueop += "."
        num.set(op)

def onBackspace():
    global op, trueop
    op = op[:-1]
    trueop = trueop[:-1]
    num.set(op)

def onLog():
    global op, trueop, logop, isLog
    op += "log"
    num.set(op)
    isLog=True
    if len(trueop) > 0:
        try:
            logop=str(eval(trueop))
            logop += "*"
            trueop = ""
        except:
            try:
                logop=str(eval(trueop[:-1]))
                logop += trueop[-1]
                trueop = ""
            except:
                trueop = ""
                op = ""
                num.set("Invalid Input")
    else:
        logop = ""
        trueop = ""

def setlogbase(arg):
    global base
    if arg == 10:
        base = 10
    elif arg == 'e':
        base = math.e

def onAntilog():
    global op, trueop, antilogop, isAntilog
    op += "antilog"
    num.set(op)
    isAntilog=True
    if len(trueop) > 0:
        try:
            antilogop=str(eval(trueop))
            antilogop += "*"
            trueop = ""
        except:
            try:
                antilogop=str(eval(trueop[:-1]))
                antilogop += trueop[-1]
                trueop = ""
            except:
                trueop = ""
                op = ""
                num.set("Invalid Input")
    else:
        antilogop = ""
        trueop = ""

def onFactorial():
    global op, trueop
    op += "!"
    num.set(op)
    try:
        trueop = str(math.factorial(eval(trueop)))
    except:
        op = ""
        trueop = ""
        num.set("Can't factorial that!")

declare_var()
#First row
btnexpon = Button(calc, font=('comic sans', 20, 'bold'), text="xⁿ", bd=8, command = lambda:[onClick("**"), sound('e')], bg="black", fg="white").grid(row=1, column=0, sticky='news')
btnclear = Button(calc, font=('comic sans', 20, 'bold'), text="C", bd=8, command = lambda:[onClear(), sound('C')], bg="black", fg="orange").grid(row=1, column=1, sticky='news')
btnback = Button(calc, font=('comic sans', 20, 'bold'), text="⌫", bd=8, command = lambda:[onBackspace(), sound('B')], bg="black", fg="red").grid(row=1, column=2, sticky='news')
btnpercent = Button(calc, font=('comic sans', 20, 'bold'), text="%", bd=8, command = lambda:[onPercent(), sound('%')], bg="black", fg="white").grid(row=1, column=3, sticky='news')
btndivide = Button(calc, font=('comic sans', 20, 'bold'), text="÷", bd=8, command = lambda:[onClick("/"), sound('/')], padx=16, bg="black", fg="white").grid(row=1, column=4, sticky='news')
#Second row
btnloge = Button(calc, font=('comic sans', 20, 'bold'), text="Logₑ", bd=8, command = lambda:[onLog(), sound("log"), setlogbase('e')], bg="black", fg="white").grid(row=2, column=0, sticky='news')
btn7 = Button(calc, font=('comic sans', 20, 'bold'), text="7", bd=8, command = lambda:[onClick(7), sound(7)], bg="black", fg="white").grid(row=2, column=1, sticky='news')
btn8 = Button(calc, font=('comic sans', 20, 'bold'), text="8", bd=8, command = lambda:[onClick(8), sound(8)], bg="black", fg="white").grid(row=2, column=2, sticky='news')
btn9 = Button(calc, font=('comic sans', 20, 'bold'), text="9", bd=8, command = lambda:[onClick(9), sound(9)], bg="black", fg="white").grid(row=2, column=3, sticky='news')
btnmultiply = Button(calc, font=('comic sans', 20, 'bold'), text="×", command = lambda:[onClick("*"), sound('*')], bd=8, padx=16, bg="black", fg="white").grid(row=2, column=4, sticky='news')
#Third row
btnlog10 = Button(calc, font=('comic sans', 20, 'bold'), text="Log₁₀", bd=8, command = lambda:[onLog(), sound("log"), setlogbase(10)], bg="black", fg="white").grid(row=3, column=0, sticky='news')
btn4 = Button(calc, font=('comic sans', 20, 'bold'), text="4", bd=8, command = lambda:[onClick(4), sound(4)], bg="black", fg="white").grid(row=3, column=1, sticky='news')
btn5 = Button(calc, font=('comic sans', 20, 'bold'), text="5", bd=8, command = lambda:[onClick(5), sound(5)], bg="black", fg="white").grid(row=3, column=2, sticky='news')
btn6 = Button(calc, font=('comic sans', 20, 'bold'), text="6", bd=8, command = lambda:[onClick(6), sound(6)], bg="black", fg="white").grid(row=3, column=3, sticky='news')
btnminus = Button(calc, font=('comic sans', 20, 'bold'), text="-", bd=8, command = lambda:[onClick("-"), sound('-')], padx=16, bg="black", fg="white").grid(row=3, column=4, sticky='news')
#Fourth row
btnantilog10 = Button(calc, font=('comic sans', 20, 'bold'), text="Antilog₁₀", bd=8, command = lambda:[onAntilog(), sound("antilog")], bg="black", fg="white").grid(row=4, column=0, sticky='news')
btn1 = Button(calc, font=('comic sans', 20, 'bold'), text="1", bd=8, command = lambda:[onClick(1), sound(1)], bg="black", fg="white").grid(row=4, column=1, sticky='news')
btn2 = Button(calc, font=('comic sans', 20, 'bold'), text="2", bd=8, command = lambda:[onClick(2), sound(2)], bg="black", fg="white").grid(row=4, column=2, sticky='news')
btn3 = Button(calc, font=('comic sans', 20, 'bold'), text="3", bd=8, command = lambda:[onClick(3), sound(3)], bg="black", fg="white").grid(row=4, column=3, sticky='news')
btnplus = Button(calc, font=('comic sans', 20, 'bold'), text="+", bd=8, command = lambda:[onClick("+"), sound('+')], padx=16, bg="black", fg="white").grid(row=4, column=4, sticky='news')
#Fifth row
btnfact = Button(calc, font=('comic sans', 20, 'bold'), text="x!", bd=8, command = lambda:[onFactorial(), sound("antilog")], bg="black", fg="white").grid(row=5, column=0, sticky='news')
btnans = Button(calc, font=('comic sans', 20, 'bold'), text="Ans", bd=8, command = lambda:[onAns(), sound("Ans")], bg="black", fg="green").grid(row=5, column=1, sticky='news')
btn0 = Button(calc, font=('comic sans', 20, 'bold'), text="0", bd=8, command = lambda:[onClick(0), sound(0)], bg="black", fg="white").grid(row=5, column=2, sticky='news')
btndecimal = Button(calc, font=('comic sans', 20, 'bold'), text=".", bd=8, command = lambda:[onDecimal(), sound('.')], bg="black", fg="white").grid(row=5, column=3, sticky='news')
btnequal = Button(calc, font=('comic sans', 20, 'bold'), text="=", bd=8, command = lambda:[onEqual(), sound('=')], padx=16, bg="black", fg="white").grid(row=5, column=4, sticky='news')
sound("start")
calc.mainloop()
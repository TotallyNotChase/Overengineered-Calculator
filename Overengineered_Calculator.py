import playsound
import math
import tkinter as tk

class maincalculator(tk.Frame):

    def sound(self, arg):
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
        elif arg == "log":
            playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/log.mp3', block=False)
        elif arg == "antilog":
            playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/antilog.mp3', block=False)
        elif arg == "fact":
            playsound.playsound('C:/Users/Chase/Desktop/Python Projects/Overengineered Calculator/Assets/factorial.mp3', block=False)
        else:
            print("Sorry something went wrong")

    def simplify(self):
        count=0
        a = float(self.op)
        while a > 10:
            a/=10
            count+=1
        self.op = str(round((a*10), 4)) + "*10^" + str(count)

    def onClick(self, operator):
        if len(self.op)>20:
            self.op=""
            self.trueop=""
            self.num.set("INF")
        else:
            self.trueop += str(operator)
            self.op += str(operator)
            self.num.set(self.op)

    def onClear(self):
        self.op = ""
        self.trueop = ""
        self.num.set(self.op)

    def onEqual(self):
        if self.isLog == True:
            try:
                self.trueop = str(round(eval(self.logop + str(math.log(eval(self.trueop), self.base))), 4))
                self.op = self.trueop
                self.logop = ""
                self.isLog = False
                self.ans = self.trueop
                if float(self.trueop) > 100000:
                    self.simplify()
                self.num.set(self.op)
            except:
                self.op = ""
                self.trueop = ""
                self.logop = ""
                self.isLog = False
                self.num.set("Invalid Input")
        elif self.isAntilog == True:
            try:
                self.trueop = str(round(eval(self.antilogop + str(10**eval(self.self.trueop))), 4))
                self.op = self.trueop
                self.antilogop = ""
                self.isAntilog = False
                self.ans = self.trueop
                if float(self.trueop) > 100000:
                    self.simplify()
                self.num.set(self.op)
            except:
                self.op = ""
                self.trueop = ""
                self.logop = ""
                self.isLog = False
                self.num.set("Invalid Input")
        else:
             try:
                self.trueop = str(round(eval(self.trueop), 4))
                if len(self.op) > 20 :
                    self.op = ""
                    self.trueop = ""
                    self.num.set("INF")
                else:
                    self.op = self.trueop
                    if float(self.trueop) > 100000:
                        self.simplify()
                    self.num.set(self.op)
                    self.ans = self.trueop
             except:
                self.num.set("Invalid Input")

    def onAns(self):
        self.op += "Ans"
        self.trueop += self.ans
        self.num.set(self.op)

    def onPercent(self):
        try:
            self.num.set(str(eval(self.trueop)))
            self.op += "% * "
            self.num.set(self.op)
            self.trueop = str(float(self.trueop)/100) + "*"
        except:
            self.op = ""
            self.trueop = ""
            self.num.set("Invalid Input")

    def onDecimal(self):
        if(self.op.count(".") == 0):
            self.op += "."
            self.trueop += "."
            self.num.set(self.op)

    def onBackspace(self):
        self.op = self.op[:-1]
        self.trueop = self.trueop[:-1]
        self.num.set(self.op)

    def onLog(self):
        self.op += "log"
        self.num.set(self.op)
        self.isLog=True
        if len(self.trueop) > 0:
            try:
                self.logop=str(eval(self.trueop))
                self.logop += "*"
                self.trueop = ""
            except:
                try:
                    self.logop=str(eval(self.trueop[:-1]))
                    self.logop += self.trueop[-1]
                    self.trueop = ""
                except:
                    self.trueop = ""
                    self.op = ""
                    self.num.set("Invalid Input")
        else:
            self.logop = ""
            self.trueop = ""

    def setlogbase(self, arg):
        if arg == 10:
            self.base = 10
        elif arg == 'e':
            self.base = math.e

    def onAntilog(self):
        self.op += "antilog"
        self.num.set(self.op)
        self.isAntilog=True
        if len(self.trueop) > 0:
            try:
                self.antilogop=str(eval(self.trueop))
                self.antilogop += "*"
                self.trueop = ""
            except:
                try:
                    self.antilogop=str(eval(self.trueop[:-1]))
                    self.antilogop += self.trueop[-1]
                    self.trueop = ""
                except:
                    self.trueop = ""
                    self.op = ""
                    self.num.set("Invalid Input")
        else:
            self.antilogop = ""
            self.trueop = ""

    def onFactorial(self):
        self.op += "!"
        self.num.set(self.op)
        try:
            self.trueop = str(math.factorial(eval(self.trueop)))
        except:
            self.op = ""
            self.trueop = ""
            self.num.set("Can't factorial that!")

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #Variable definitions
        self.num = tk.StringVar()
        self.screen = tk.Entry(self, font=('comic sans', 40, 'bold'), textvariable = self.num, bg="gray", justify='right', state='disabled').grid(columnspan=5)
        self.parent = parent
        self.op = ""
        self.ans = ""
        self.trueop = ""
        self.logop = ""
        self.antilogop = ""
        self.base = math.e
        self.isLog = False
        self.isAntilog = False
        #First row
        btnexpon = tk.Button(self, font=('comic sans', 20, 'bold'), text="xⁿ", bd=8, command = lambda:[self.onClick("**"), self.sound('e')], bg="black", fg="white").grid(row=1, column=0, sticky='news')
        btnclear = tk.Button(self, font=('comic sans', 20, 'bold'), text="C", bd=8, command = lambda:[self.onClear(), self.sound('C')], bg="black", fg="orange").grid(row=1, column=1, sticky='news')
        btnback = tk.Button(self, font=('comic sans', 20, 'bold'), text="⌫", bd=8, command = lambda:[self.onBackspace(), self.sound('B')], bg="black", fg="red").grid(row=1, column=2, sticky='news')
        btnpercent = tk.Button(self, font=('comic sans', 20, 'bold'), text="%", bd=8, command = lambda:[self.onPercent(), self.sound('%')], bg="black", fg="white").grid(row=1, column=3, sticky='news')
        btndivide = tk.Button(self, font=('comic sans', 20, 'bold'), text="÷", bd=8, command = lambda:[self.onClick("/"), self.sound('/')], padx=16, bg="black", fg="white").grid(row=1, column=4, sticky='news')
        #Second row
        btnloge = tk.Button(self, font=('comic sans', 20, 'bold'), text="Logₑ", bd=8, command = lambda:[self.onLog(), self.sound("log"), self.setlogbase('e')], bg="black", fg="white").grid(row=2, column=0, sticky='news')
        btn7 = tk.Button(self, font=('comic sans', 20, 'bold'), text="7", bd=8, command = lambda:[self.onClick(7), self.sound(7)], bg="black", fg="white").grid(row=2, column=1, sticky='news')
        btn8 = tk.Button(self, font=('comic sans', 20, 'bold'), text="8", bd=8, command = lambda:[self.onClick(8), self.sound(8)], bg="black", fg="white").grid(row=2, column=2, sticky='news')
        btn9 = tk.Button(self, font=('comic sans', 20, 'bold'), text="9", bd=8, command = lambda:[self.onClick(9), self.sound(9)], bg="black", fg="white").grid(row=2, column=3, sticky='news')
        btnmultiply = tk.Button(self, font=('comic sans', 20, 'bold'), text="×", command = lambda:[self.onClick("*"), self.sound('*')], bd=8, padx=16, bg="black", fg="white").grid(row=2, column=4, sticky='news')
        #Third row
        btnlog10 = tk.Button(self, font=('comic sans', 20, 'bold'), text="Log₁₀", bd=8, command = lambda:[self.onLog(), self.sound("log"), self.setlogbase(10)], bg="black", fg="white").grid(row=3, column=0, sticky='news')
        btn4 = tk.Button(self, font=('comic sans', 20, 'bold'), text="4", bd=8, command = lambda:[self.onClick(4), self.sound(4)], bg="black", fg="white").grid(row=3, column=1, sticky='news')
        btn5 = tk.Button(self, font=('comic sans', 20, 'bold'), text="5", bd=8, command = lambda:[self.onClick(5), self.sound(5)], bg="black", fg="white").grid(row=3, column=2, sticky='news')
        btn6 = tk.Button(self, font=('comic sans', 20, 'bold'), text="6", bd=8, command = lambda:[self.onClick(6), self.sound(6)], bg="black", fg="white").grid(row=3, column=3, sticky='news')
        btnminus = tk.Button(self, font=('comic sans', 20, 'bold'), text="-", bd=8, command = lambda:[self.onClick("-"), self.sound('-')], padx=16, bg="black", fg="white").grid(row=3, column=4, sticky='news')
        #Fourth row
        btnantilog10 = tk.Button(self, font=('comic sans', 20, 'bold'), text="Antilog₁₀", bd=8, command = lambda:[self.onAntilog(), self.sound("antilog")], bg="black", fg="white").grid(row=4, column=0, sticky='news')
        btn1 = tk.Button(self, font=('comic sans', 20, 'bold'), text="1", bd=8, command = lambda:[self.onClick(1), self.sound(1)], bg="black", fg="white").grid(row=4, column=1, sticky='news')
        btn2 = tk.Button(self, font=('comic sans', 20, 'bold'), text="2", bd=8, command = lambda:[self.onClick(2), self.sound(2)], bg="black", fg="white").grid(row=4, column=2, sticky='news')
        btn3 = tk.Button(self, font=('comic sans', 20, 'bold'), text="3", bd=8, command = lambda:[self.onClick(3), self.sound(3)], bg="black", fg="white").grid(row=4, column=3, sticky='news')
        btnplus = tk.Button(self, font=('comic sans', 20, 'bold'), text="+", bd=8, command = lambda:[self.onClick("+"), self.sound('+')], padx=16, bg="black", fg="white").grid(row=4, column=4, sticky='news')
        #Fifth row
        btnfact = tk.Button(self, font=('comic sans', 20, 'bold'), text="x!", bd=8, command = lambda:[self.onFactorial(), self.sound("fact")], bg="black", fg="white").grid(row=5, column=0, sticky='news')
        btnans = tk.Button(self, font=('comic sans', 20, 'bold'), text="Ans", bd=8, command = lambda:[self.onAns(), self.sound("Ans")], bg="black", fg="green").grid(row=5, column=1, sticky='news')
        btn0 = tk.Button(self, font=('comic sans', 20, 'bold'), text="0", bd=8, command = lambda:[self.onClick(0), self.sound(0)], bg="black", fg="white").grid(row=5, column=2, sticky='news')
        btndecimal = tk.Button(self, font=('comic sans', 20, 'bold'), text=".", bd=8, command = lambda:[self.onDecimal(), self.sound('.')], bg="black", fg="white").grid(row=5, column=3, sticky='news')
        btnequal = tk.Button(self, font=('comic sans', 20, 'bold'), text="=", bd=8, command = lambda:[self.onEqual(), self.sound('=')], padx=16, bg="black", fg="white").grid(row=5, column=4, sticky='news')

if __name__ == "__main__":
    calc = tk.Tk()
    calc.title("Very Sophisticated Simple Calculator")
    calc.configure(background="gray")
    maincalculator(calc).grid(columnspan=5, rowspan=5)
    maincalculator.sound(calc, "start")
    calc.mainloop()
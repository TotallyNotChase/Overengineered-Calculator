import playsound
import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path

class MainCalculator(tk.Frame):

    def sound(self, arg):
        #For playing sounds on different key presses
        if arg == "start":
            playsound.playsound(base_path + "Sounds\\beam.mp3", block=False)
        elif arg == 1:
            playsound.playsound(base_path + "Sounds\\one.mp3", block=False)
        elif arg == 2:
            playsound.playsound(base_path + "Sounds\\two.mp3", block=False)
        elif arg == 3:
            playsound.playsound(base_path + "Sounds\\three.mp3", block=False)
        elif arg == 4:
            playsound.playsound(base_path + "Sounds\\four.mp3", block=False)
        elif arg == 5:
            playsound.playsound(base_path + "Sounds\\five.mp3", block=False)
        elif arg == 6:
            playsound.playsound(base_path + "Sounds\\six.mp3", block=False)
        elif arg == 7:
            playsound.playsound(base_path + "Sounds\\seven.mp3", block=False)
        elif arg == 8:
            playsound.playsound(base_path + "Sounds\\eight.mp3", block=False)
        elif arg == 9:
            playsound.playsound(base_path + "Sounds\\nine.mp3", block=False)
        elif arg == 0:
            playsound.playsound(base_path + "Sounds\\zero.mp3", block=False)
        elif arg == '/':
            playsound.playsound(base_path + "Sounds\\divide.mp3", block=False)
        elif arg == '+':
            playsound.playsound(base_path + "Sounds\\plus.mp3", block=False)
        elif arg == '-':
            playsound.playsound(base_path + "Sounds\\minus.mp3", block=False)
        elif arg == '*':
            playsound.playsound(base_path + "Sounds\\multiple.mp3", block=False)
        elif arg == '=':
            playsound.playsound(base_path + "Sounds\\equals.mp3", block=False)
        elif arg == '.':
            playsound.playsound(base_path + "Sounds\\point.mp3", block=False)
        elif arg == 'C':
            playsound.playsound(base_path + "Sounds\\clear.mp3", block=False)
        elif(arg == 'B'):
            playsound.playsound(base_path + "Sounds\\back.mp3", block=False)
        elif arg == '%':
            playsound.playsound(base_path + "Sounds\\percent.mp3", block=False)
        elif arg == "Ans":
            playsound.playsound(base_path + "Sounds\\ans.mp3", block=False)
        elif arg == 'e':
            playsound.playsound(base_path + "Sounds\\expo.mp3", block=False)
        elif arg == "log":
            playsound.playsound(base_path + "Sounds\\log.mp3", block=False)
        elif arg == "antilog":
            playsound.playsound(base_path + "Sounds\\antilog.mp3", block=False)
        elif arg == "fact":
            playsound.playsound(base_path + "Sounds\\factorial.mp3", block=False)
        else:
            print("Sorry something went wrong")

    #Methods used for Main Calculator - Start

    def postfixConvert(self, oplist = []):
        stack = [""]
        for i in oplist:
            isDone = False
            if i == '+':
                while (not isDone):
                    if stack[0] == "" or stack[0] == '-' or stack[0] == '(':
                        stack.insert(0, i)
                        isDone = True
                    else:
                        try:
                            print(stack.pop(0))
                        except:
                            print("Stack is empty")
            elif i == '-':
                while (not isDone):
                    if stack[0] == "" or stack[0] == '(':
                        stack.insert(0, i)
                        isDone = True
                    else:
                        try:
                            print(stack.pop(0))
                        except:
                            print("Stack is empty")
            elif i == '*':
                while (not isDone):
                    if stack[0] == "" or stack[0] == '+' or stack[0] == '-' or stack[0] == '/' or stack[0] == '(':
                        stack.insert(0, i)
                        isDone = True
                    else:
                        try:
                            print(stack.pop(0))
                        except:
                            print("Stack is empty")
            elif i == '/':
                while (not isDone):
                    if stack[0] == "" or stack[0] == '+' or stack[0] == '-' or stack[0] == '(':
                        stack.insert(0, i)
                        isDone = True
                    else:
                        print(stack.pop(0))
            elif i == '^':
                stack.insert(0, i)
            elif i == '(':
                stack.insert(0, i)
            elif i == ')':
                while stack[0] != '(':
                    print(stack.pop(0))
            else:
                print(i)
        for i in range (0, len(stack)):
            if stack[i] != '(':
                print(stack[i])

    def simplify(self):
        #For simplifying op into x * 10^y form
        count = 0
        a = float(self.op)
        while a > 10:
            a /= 10
            count += 1
        self.op = str(round((a*10), 4)) + "*10^" + str(count-1)

    def onClick(self, operator):
        #For handling MOST key presses
        if len(self.op) > 20:
            self.op = ""
            self.trueop = ""
            self.num.set("INF")
        else:
            if operator == '**':
                self.op += '^'
            else:
                self.op += str(operator)
            self.trueop += str(operator)
            self.num.set(self.op)

    def onClear(self):
        #For handling 'C' key press
        self.op = ""
        self.trueop = ""
        self.num.set(self.op)

    def onEqual(self):
        #For handling '=' key press
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
               self.postfixConvert(self.op)
               if len(self.op) > 20 :
                   self.op = ""
                   self.trueop = ""
                   self.num.set("INF")
               else:
                   self.op = self.trueop
                   self.isPercent = False
                   if float(self.trueop) > 100000:
                       self.simplify()
                   self.num.set(self.op)
                   self.ans = self.trueop
            except:
               self.num.set("Invalid Input")

    def onAns(self):
        #For handling 'Ans' key press
        self.op += "Ans"
        self.trueop += self.ans
        self.num.set(self.op)

    def onPercent(self):
        #For handling '%' key press
        try:
            self.num.set(str(eval(self.trueop)))
            self.op += "%*"
            self.isPercent = True
            self.num.set(self.op)
            self.trueop = str(float(self.trueop)/100) + "*"
        except:
            self.op = ""
            self.trueop = ""
            self.num.set("Invalid Input")

    def onDecimal(self):
        #For handling '.' key press
        if(self.op.count(".") == 0):
            self.op += "."
            self.trueop += "."
            self.num.set(self.op)

    def onBackspace(self):
        #For handling '⌫' key press
         self.trueop = self.trueop[:-1]
         self.op = self.op[:-1]
         self.num.set(self.op)

    def onLog(self):
        #For handling 'Log₁₀' & 'Logₑ' key press
        self.op += "log"
        self.num.set(self.op)
        self.isLog=True
        if len(self.trueop) > 0:
            try:
                self.logop = str(eval(self.trueop))
                self.logop += "*"
                self.trueop = ""
            except:
                try:
                    self.logop = str(eval(self.trueop[:-1]))
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
        #For setting the log base, called upon pressing either of the 'log' keys
        if arg == 10:
            self.base = 10
        elif arg == 'e':
            self.base = math.e

    def onAntilog(self):\
        #For handling 'Antilog' key press
        self.op += "antilog"
        self.num.set(self.op)
        self.isAntilog = True
        if len(self.trueop) > 0:
            try:
                self.antilogop = str(eval(self.trueop))
                self.antilogop += "*"
                self.trueop = ""
            except:
                try:
                    self.antilogop = str(eval(self.trueop[:-1]))
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
        #For handling 'x!' key press
        self.op += "!"
        self.num.set(self.op)
        try:
            self.trueop = str(math.factorial(eval(self.trueop)))
        except:
            self.op = ""
            self.trueop = ""
            self.num.set("Can't factorial that!")

    #Methods used for Main Calculator - End

    #Methods used for Assigning Macros - Start

    def addbtn(self, event=None):
        #For handling 'Add Macro' key press
        try:
            eval(self.nameentry.get())
            if len(self.nameentry.get()) >= 6 or eval(self.nameentry.get()) >= 100000:
                self.macroinput.set("Can't add a long number!")
            else:
                self.macronumber[self.i] = str(round(eval(self.nameentry.get()), 4))
                self.macrotext[self.i].set(self.nameentry.get())
                self.i+=1
                self.nameentry.delete(0, "end")
        except:
            self.macroinput.set("Invalid expression")

    def clearscreen(self, event):
        #For clearing the screen upon clicking(mouse 1) on it
        self.nameentry.delete(0, "end")
        return None

    #Methods used for Assigning Macros - End

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        #Variable definitions - For Main Calculator

        self.num = tk.StringVar()
        self.op = ""
        self.ans = ""
        self.trueop = ""
        self.logop = ""
        self.antilogop = ""
        self.base = math.e
        self.isLog = False
        self.isAntilog = False
        self.isPercent = False
        self.screen = tk.Entry(self, font = ('comic sans', 40, 'bold'), textvariable = self.num, bg = "gray", justify = 'right', state = 'disabled').grid(columnspan = 5)

        #First row

        btnexpon = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "xⁿ", bd = 8, command = lambda: [self.onClick("**"), self.sound('e')], 
                             bg = "black", fg = "white").grid(row = 1, column = 0, sticky = 'news')

        btnclear = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "C", bd=8, command = lambda: [self.onClear(), self.sound('C')], 
                             bg = "black", fg = "orange").grid(row = 1, column = 1, sticky = 'news')

        btnback = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "⌫", bd = 8, command = lambda: [self.onBackspace(), self.sound('B')], 
                            bg = "black", fg = "red").grid(row = 1, column = 2, sticky = 'news')

        btnpercent = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "%", bd = 8, command = lambda: [self.onPercent(), self.sound('%')], 
                               bg = "black", fg = "white").grid(row = 1, column = 3, sticky = 'news')

        btndivide = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "÷", bd = 8, command = lambda: [self.onClick("/"), self.sound('/')], 
                              bg = "black", fg = "white").grid(row = 1, column = 4, sticky = 'news')
        #Second row

        btnloge = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "Logₑ", bd = 8, command = lambda: [self.onLog(), self.sound("log"), self.setlogbase('e')], 
                            bg = "black", fg = "white").grid(row = 2, column = 0, sticky = 'news')

        btn7 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "7", bd = 8, command = lambda: [self.onClick(7), self.sound(7)], 
                         bg = "black", fg = "white").grid(row = 2, column = 1, sticky = 'news')

        btn8 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "8", bd = 8, command = lambda: [self.onClick(8), self.sound(8)], 
                         bg = "black", fg = "white").grid(row = 2, column = 2, sticky = 'news')

        btn9 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "9", bd = 8, command = lambda: [self.onClick(9), self.sound(9)], 
                         bg = "black", fg = "white").grid(row = 2, column = 3, sticky = 'news')

        btnmultiply = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "×", command = lambda: [self.onClick("*"), self.sound('*')], bd=8, 
                                bg = "black", fg = "white").grid(row = 2, column = 4, sticky = 'news')
        #Third row

        btnlog10 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "Log₁₀", bd = 8, command = lambda: [self.onLog(), self.sound("log"), self.setlogbase(10)],
                             bg = "black", fg = "white").grid(row = 3, column = 0, sticky = 'news')

        btn4 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "4", bd = 8, command = lambda: [self.onClick(4), self.sound(4)], 
                         bg = "black", fg = "white").grid(row = 3, column = 1, sticky = 'news')

        btn5 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "5", bd = 8, command = lambda: [self.onClick(5), self.sound(5)], 
                         bg = "black", fg = "white").grid(row = 3, column = 2, sticky = 'news')

        btn6 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "6", bd = 8, command = lambda: [self.onClick(6), self.sound(6)], 
                         bg = "black", fg = "white").grid(row = 3, column = 3, sticky = 'news')

        btnminus = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "-", bd = 8, command = lambda: [self.onClick("-"), self.sound('-')],  
                             bg = "black", fg = "white").grid(row = 3, column = 4, sticky = 'news')

        #Fourth row

        btnantilog10 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "Antilog₁₀", bd = 8, command = lambda:[self.onAntilog(), self.sound("antilog")], 
                                 bg = "black", fg = "white").grid(row = 4, column = 0, sticky = 'news')


        btn1 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "1", bd = 8, command = lambda: [self.onClick(1), self.sound(1)], 
                         bg = "black", fg = "white").grid(row = 4, column = 1, sticky = 'news')

        btn2 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "2", bd = 8, command = lambda: [self.onClick(2), self.sound(2)], 
                         bg = "black", fg = "white").grid(row = 4, column = 2, sticky = 'news')

        btn3 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "3", bd = 8, command = lambda: [self.onClick(3), self.sound(3)], 
                         bg = "black", fg = "white").grid(row = 4, column = 3, sticky = 'news')

        btnplus = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "+", bd = 8, command = lambda: [self.onClick("+"), self.sound('+')], 
                            bg = "black", fg = "white").grid(row = 4, column = 4, sticky = 'news')
        #Fifth row

        btnfact = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "x!", bd = 8, command = lambda: [self.onFactorial(), self.sound("fact")], 
                            bg = "black", fg = "white").grid(row = 5, column = 0, sticky = 'news')

        btnans = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "Ans", bd = 8, command = lambda: [self.onAns(), self.sound("Ans")], 
                           bg = "black", fg = "green").grid(row = 5, column = 1, sticky = 'news')

        btn0 = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "0", bd = 8, command = lambda: [self.onClick(0), self.sound(0)], 
                         bg = "black", fg = "white").grid(row = 5, column = 2, sticky = 'news')

        btndecimal = tk.Button(self, font = ('comic sans', 20, 'bold'), text = ".", bd = 8, command = lambda: [self.onDecimal(), self.sound('.')], 
                               bg = "black", fg = "white").grid(row = 5, column = 3, sticky = 'news')

        btnequal = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "=", bd = 8, command = lambda: [self.onEqual(), self.sound('=')],  
                             bg = "black", fg = "white").grid(row = 5, column = 4, sticky = 'news')

        #Variable definitions - For Assigning Macros

        self.i = 0
        self.macrotext = [tk.StringVar() for x in range (5)]
        self.macronumber = ["" for x in range (5)]
        self.macroinput = tk.StringVar()

        #Entryscreen setting

        self.nameentry = tk.Entry(self, font = ('comic sans', 27, 'bold'), 
                                  textvariable = self.macroinput, justify = 'right')
        self.nameentry.bind("<Button-1>", self.clearscreen)
        self.nameentry.bind("<Return>", self.addbtn)
        self.nameentry.grid(row = 6, column = 1, columnspan = 4, sticky = 'news')

        #Buttons Defitions

        btnadd = tk.Button(self, font = ('comic sans', 20, 'bold'), text = "Add Macro", bd = 8, command = self.addbtn, bg = "black", fg = "white").grid(row = 6, column = 0)
        self.macrobutton = [tk.Button(self, font = ('comic sans', 20, 'bold'), textvariable = self.macrotext[x], bd=8,
                                    bg = "black", fg = "white")     
                          for x in range (5)]
        [self.macrobutton[x].grid(row = 7, column = x, sticky = 'news') for x in range (5)]
        self.macrobutton[0].configure(command = lambda: self.onClick(self.macronumber[0]))
        self.macrobutton[1].configure(command = lambda: self.onClick(self.macronumber[1]))
        self.macrobutton[2].configure(command = lambda: self.onClick(self.macronumber[2]))
        self.macrobutton[3].configure(command = lambda: self.onClick(self.macronumber[3]))
        self.macrobutton[4].configure(command = lambda: self.onClick(self.macronumber[4]))

class CanvasTab(tk.Frame):

    def showImage(self, image):
        #Puts the image on canvas after garbage collection
        self.fileimage = image
        self.canvas.create_image((0,0), image = image, anchor = tk.NW)

    def fetchKittens(self, seed):
        #Fetches an image based on the random seed
        self.randomkit[0] = seed
        if seed == 1:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens1.png"))
        elif seed == 2:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens2.png"))
        elif seed == 3:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens3.png"))
        elif seed == 4:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens4.png"))
        elif seed == 5:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens5.png"))
        elif seed == 6:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens6.png"))
        elif seed == 7:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens7.png"))
        elif seed == 8:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens8.png"))
        elif seed == 9:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens9.png"))
        elif seed == 10:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\kittens10.png"))

    def fetchPuppies(self, seed):
        #Fetches an image based on the random seed
        self.randompup[0] = seed
        if seed == 1:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies1.png"))
        elif seed == 2:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies2.png"))
        elif seed == 3:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies3.png"))
        elif seed == 4:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies4.png"))
        elif seed == 5:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies5.png"))
        elif seed == 6:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies6.png"))
        elif seed == 7:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies7.png"))
        elif seed == 8:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies8.png"))
        elif seed == 9:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies9.png"))
        elif seed == 10:
            self.showImage(tk.PhotoImage(file = base_path + "Images\\Puppies10.png"))


    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        ttk.Separator(self, orient = tk.VERTICAL).grid(row=0, column = 5, padx = 5, rowspan=4, sticky = 'ns')
        self.randomkit = [0, 0]         #A list to avoid generating the previous random number
        self.randompup = [0, 0]
        btnkittens = tk.Button(self, font = ('comic sans', 15, 'bold'), text = "View kittens", bd = 8, command = lambda: self.fetchKittens(random.choice([i for i in range (1, 10) if i not in self.randomkit])), 
                                bg = "black", fg = "white").grid(row = 0, column = 6, ipady = 40, sticky = 'news')

                            #The Internal padding is so that the buttons have no gap between them

        btnpuppies = tk.Button(self, font = ('comic sans', 15, 'bold'), text = "View puppies", bd = 8, command = lambda: self.fetchPuppies(random.choice([i for i in range (1, 10) if i not in self.randompup])), 
                                bg = "black", fg = "white").grid(row = 2, column = 6, ipady = 40, sticky = 'news')

        self.canvas = tk.Canvas(self, width = 497)
                            #The Canvas has a height of ~280 and width of 497, this the resolution of all the pictures
        self.canvas.grid(row=0, column = 7, rowspan = 4)

if __name__ == "__main__":
    calc = tk.Tk()
    calc.title("Very Sophisticated Simple Calculator")
    calc.configure(background="gray")
    base_path = str(Path(__file__).parent) + "\\assets\\"
    MainCalculator(calc).grid(columnspan=5, rowspan=8)
    MainCalculator.sound(calc, "start")
    CanvasTab(calc).grid(row = 0, column = 6, rowspan = 4, sticky = 'news')
    calc.mainloop()
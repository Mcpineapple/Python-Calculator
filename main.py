from tkinter import *

class pile_pol:

    def __init__(self):
        self.num = []
        self.op = []
    
    def add_num(self, num):
        self.num = [num] + self.num

    def add_op(self,op):
        self.op = [op] + self.op
    
    def calc(self):
        while len(self.num) > 1 and len(self.op) > 0:
            num1 = self.num.pop()
            num2 = self.num.pop()
            oper = self.op.pop()
            if oper == '+':
                self.num = [num1 + num2] + self.num
            elif oper == '-':
                self.num = [num1 - num2] + self.num
            elif oper == '*':
                self.num = [num1 * num2] + self.num
            elif oper == '/':
                if num2 == 0:
                    self.empty()
                    return 'ERROR MATH'
                else:
                    self.num = [num1 // num2] + self.num
        return self.num[-1]
    
    def empty(self):
        self.num = []
        self.op = []

class calculator:
    
    def __init__(self):
        self.pile = pile_pol()

        self.root = Tk() #initialising tkinter interface
        self.root.title("Rudementary Calculator") #window title
        self.frame = Frame(self.root) #creating main (and only) frame that will contain all the widgets
        self.frame.grid() #widgets shall be organised using the grid method - it is very useful when handling multiple buttons like this
        
        self.text = StringVar()  #initialising the text variable. it shall be used as the text of the output. having it is as a StringVar makes it easier to manipulate
        self.text.set("") # output starts empty
        self.result = StringVar()
        self.result.set("")

        self.input = Label(self.frame,textvariable=self.text, borderwidth = 3, relief='ridge', bg = "lightgrey", fg = "black")
        self.input.grid(row = 0, columnspan = 7, sticky="ew")

        self.output = Label(self.frame,textvariable=self.result, borderwidth = 3, relief='ridge',bg = "lightgrey", fg = "black")
        self.output.grid(row = 1, columnspan = 7, sticky="ew")

        #execution button. calculates result of operation and outputs it.
        self.execute = Button(self.frame, text = "EXE", command=self.calculate)
        self.execute.grid(row = 2, column = 1)

        #refreshing button. reinitialises all variables to 0/"" (cache, output)
        self.empty = Button(self.frame, text = "AC", command=self.clear_full)
        self.empty.grid(row=2, column = 2)

        #ouput delete button. deletes the output but not any background data. 
        self.delete = Button(self.frame, text = "DEL", command=self.clear)
        self.delete.grid(row=2, column = 3)

        self.exit = Button(self.frame, text='OFF', command=self.root.destroy)
        self.exit.grid(row=2,column=4)

        """"Following buttons are the number butttons. They add the number to the output."""

        self.one = Button(self.frame, text = "1", command =self.add_one)
        self.one.grid(row = 3, column=1)

        self.two = Button(self.frame, text = "2", command =self.add_two)
        self.two.grid(row = 3, column=2)

        self.three = Button(self.frame, text = "3", command =self.add_three)
        self.three.grid(row = 3, column=3)

        self.four = Button(self.frame, text = "4", command =self.add_four)
        self.four.grid(row = 4, column=1)

        self.five = Button(self.frame, text = "5", command =self.add_five)
        self.five.grid(row = 4, column=2)

        self.six = Button(self.frame, text = "6", command =self.add_six)
        self.six.grid(row = 4, column=3)

        self.seven = Button(self.frame, text = "7", command =self.add_seven)
        self.seven.grid(row = 5, column=1)

        self.eight = Button(self.frame, text = "8", command =self.add_eight)
        self.eight.grid(row = 5, column=2)

        self.nine = Button(self.frame, text = "9", command =self.add_nine)
        self.nine.grid(row = 5, column=3)

        self.zero = Button(self.frame, text = "0", command =self.add_zero)
        self.zero.grid(row = 6, column=1)



        """Operation buttons."""
        self.add = Button(self.frame, text = "+", command=self.add_plus)
        self.add.grid(row = 3, column =5)

        self.sub = Button(self.frame, text = "-", command=self.add_minus)
        self.sub.grid(row = 3, column =6)

        self.mult = Button(self.frame, text="x", command=self.add_mult)
        self.mult.grid(row=4, column=5)

        self.div = Button(self.frame, text="/", command=self.add_div)
        self.div.grid(row=4, column=6)

        self.root.mainloop() #opens the window

    """Functions of the number buttons. Get the current output, add their number at the end, and outputs the result."""
    def add_one(self):
        text = self.text.get()
        text += "1"
        self.text.set(text)


    def add_two(self):
        text = self.text.get()
        text += "2"
        self.text.set(text)

    def add_three(self):
        text = self.text.get()
        text += "3"
        self.text.set(text)

    def add_four(self):
        text = self.text.get()
        text += "4"
        self.text.set(text)

    def add_five(self):
        text = self.text.get()
        text += "5"
        self.text.set(text)
    
    def add_six(self):
        text = self.text.get()
        text += "6"
        self.text.set(text)

    def add_seven(self):
        text = self.text.get()
        text += "7"
        self.text.set(text)

    def add_eight(self):
        text = self.text.get()
        text += "8"
        self.text.set(text)

    def add_nine(self):
        text = self.text.get()
        text += "9"
        self.text.set(text)

    def add_zero(self):
        text = self.text.get()
        text += "0"
        self.text.set(text)

    def add_plus(self):
        """addition fuction"""
        if len(self.text.get()) > 0:
            self.pile.add_num(int(self.text.get()))
        self.pile.add_op('+')
        self.text.set("")
        
    def add_minus(self):
        """substraction function. note : might change the name"""
        if len(self.text.get()) > 0:
            self.pile.add_num(int(self.text.get()))
        self.pile.add_op('-')
        self.text.set("")
        
    
    def add_mult(self):
        """multiplication function"""
        if len(self.text.get()) > 0:
            self.pile.add_num(int(self.text.get()))
        self.pile.add_op('*')
        self.text.set("")

    def add_div(self):
        """division function"""
        if len(self.text.get()) > 0:
            self.pile.add_num(int(self.text.get()))
        self.pile.add_op('/')
        self.text.set("")
        

    def calculate(self):
        self.pile.add_num(int(self.text.get()))
        res = self.pile.calc()
        self.text.set("")
        self.result.set(res)

            
    def clear(self):
        """function to empty output"""
        txt = self.text.get()
        if len(txt) > 1:
            txt = txt[:-1]
            self.text.set(txt)
        else :
            self.text.set("")

    def clear_full(self):
        """function to empty output and pile"""
        self.pile.empty()
        self.text.set("")
        self.result.set("")
        


calc = calculator()

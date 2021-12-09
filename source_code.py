from tkinter import *



class operation_manage:
    def __init__(self):

        self.root = Tk() #initialising tkinter interface
        self.root.title("Rudementary Calculator") #window title
        self.frame = Frame(self.root) #creating main (and only) frame that will contain all the widgets
        self.frame.grid() #widgets shall be organised using the grid method - it is very useful when handling multiple buttons like this
        
        self.text = StringVar()  #initialising the text variable. it shall be used as the text of the output. having it is as a StringVar makes it easier to manipulate
        self.text.set("") # output starts empty

        self.cache = [0, ""] #initialising the cache variable. it is used to stock important information for the mathematical side. first, it saves the number entered, then the operation that shall be executed

        #output widget. using Label because the user should not be able to modify it. contains the text variable (the output). takes up the entire first row
        self.output = Label(self.frame,textvariable=self.text, bg = "lightgrey", fg = "black")
        self.output.grid(row = 0, columnspan = 7, sticky="ew")

        #execution button. calculates result of operation and outputs it.
        self.execute = Button(self.frame, text = "EXE", command=self.calculate)
        self.execute.grid(row = 1, column = 1)

        #refreshing button. reinitialises all variables to 0/"" (cache, output)
        self.empty = Button(self.frame, text = "AC", command=self.clear_full)
        self.empty.grid(row=1, column = 2)

        #ouput delete button. deletes the output but not any background data. 
        self.delete = Button(self.frame, text = "DEL", command=self.clear)
        self.delete.grid(row=1, column = 3)

        """"Following buttons are the number butttons. They add the number to the output."""

        self.one = Button(self.frame, text = "1", command =self.add_one)
        self.one.grid(row = 2, column=1)

        self.two = Button(self.frame, text = "2", command =self.add_two)
        self.two.grid(row = 2, column=2)

        self.three = Button(self.frame, text = "3", command =self.add_three)
        self.three.grid(row = 2, column=3)

        self.four = Button(self.frame, text = "4", command =self.add_four)
        self.four.grid(row = 3, column=1)

        self.five = Button(self.frame, text = "5", command =self.add_five)
        self.five.grid(row = 3, column=2)

        self.six = Button(self.frame, text = "6", command =self.add_six)
        self.six.grid(row = 3, column=3)

        self.seven = Button(self.frame, text = "7", command =self.add_seven)
        self.seven.grid(row = 4, column=1)

        self.eight = Button(self.frame, text = "8", command =self.add_eight)
        self.eight.grid(row = 4, column=2)

        self.nine = Button(self.frame, text = "9", command =self.add_nine)
        self.nine.grid(row = 4, column=3)

        self.zero = Button(self.frame, text = "0", command =self.add_zero)
        self.zero.grid(row = 5, column=1)



        """Operation buttons."""
        self.add = Button(self.frame, text = "+", command=self.add_plus)
        self.add.grid(row = 2, column =5)

        self.sub = Button(self.frame, text = "-", command=self.add_minus)
        self.sub.grid(row = 2, column =6)

        self.mult = Button(self.frame, text="x", command=self.add_mult)
        self.mult.grid(row=3, column=5)

        self.div = Button(self.frame, text="/", command=self.add_div)
        self.div.grid(row=3, column=6)

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

    """The operation functions only activate if no other operation is happening, by checking in the cache if any operation is contained."""
    #Note : this system is so simplistic it gets unintuitive. Adding a manual button would be a temporary solution while waiting for a complete rework of the process.
    def add_plus(self):
        """addition fuction"""
        if self.cache[1] == "":
            self.cache[0] = int(self.text.get()) #stores output value in cache
            self.text.set("") #empties output
            self.cache[1] = "+" #stores current operation in cache, preventing any other, including itself, from taking place.

    def add_minus(self):
        """substraction function. note : might change the name"""
        if self.cache[1] == "":
            self.cache[0] = int(self.text.get())
            self.text.set("")
            self.cache[1] = "-"
    
    def add_mult(self):
        """multiplication function"""
        if self.cache[1] == "":
            self.cache[0] = int(self.text.get())
            self.text.set("")
            self.cache[1] = "*"

    def add_div(self):
        """division function"""
        if self.cache[1] == "":
            self.cache[0] = int(self.text.get())
            self.text.set("")
            self.cache[1] = "/"

    def calculate(self):
        """Main calculation function. Checks if and which operation is taking place, then executes the corresponding code."""
        if self.cache[1] == "+":
            self.cache[0] += int(self.text.get()) #add cache and output.
            self.text.set(self.cache[0]) #output result
            #empty cache
            self.cache[0] = 0
            self.cache[1] = ""
        elif self.cache[1] == "-":
            self.cache[0] -= int(self.text.get()) #subtract output from cache
            self.text.set(self.cache[0]) #output result
            #empty cache
            self.cache[0] = 0
            self.cache[1] = ""
        elif self.cache[1] == "*":
            self.cache[0] = self.cache[0] * int(self.text.get()) #multiply output and cache
            self.text.set(self.cache[0]) #output result
            #empty cache
            self.cache[0] = 0
            self.cache[1] = ""
        elif self.cache[1] == "/":
            if int(self.text.get()) == 0: #verifies if user is trying to divide by 0 (because of course he would)
                self.text.set("ERROR MATH") #ouputs error
            else:
                self.cache[0] = self.cache[0] / int(self.text.get()) #divides cache by output
                self.text.set(self.cache[0]) #output result. 
                #Note : only case of a float. not a problem here since the operations are seperated, but the use of floats would have to be generalized in an improved program
            #empty cache
            self.cache[0] = 0
            self.cache[1] = ""
            
    def clear(self):
        """function to empty output"""
        self.text.set("")

    def clear_full(self):
        """function to empty output and cache"""
        self.cache[0] = 0
        self.cache[1] = ""
        self.text.set("")

    
        
    
if __name__=="__main__":
    calculator = operation_manage() #initialising the class is enough since the __init__ opens a new window. in an improved version, better encapsulation and interactions with the main program could be an interesting addition

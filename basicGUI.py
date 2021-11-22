from tkinter import *
from tkinter import ttk

roots = []

def startupMenu():
    try:
        # Create menuGUI root and frame
        root = Tk()
        roots.append(root)
        frm = ttk.Frame(root, padding=30)
        grid = frm.grid()
        # Create simple label
        helloLabel = ttk.Label(frm, text="Hello there!", justify=CENTER, padding=5).grid(column=2, row=0)

        # Create button options to new windows
        addCalcBtn = ttk.Button(frm, text="Basic Calculator", command=calculatorGUI).grid(column=2, row=1, pady=10)
        addTempBtn = ttk.Button(frm, text="Temperature Converter", command=temperatureGUI).grid(column=2, row=3, pady=10)
        addUnitConverterBtn = ttk.Button(frm, text="Unit Converter", command=unitConverterGUI).grid(column=2, row=5, pady=10)

        # Exit button
        exitBtn = ttk.Button(frm, text="Exit", command= root.destroy).grid(column=4, rows=4)

        # Run GUI
        root.mainloop()
    except:
        menuFailed()

# Math functions
def addition(arg):
    print("adding")
    sol = 0
    for num in arg:
        print(num)
        sol += num
    return sol

# POTENTIALLY ADD LATER
# def subtraction(arg):
#     i = 1
#     sol = arg[0]
#     while(i < len(arg)):
#         sol -= arg[i] 
#         i += 1
# def multiplication(arg):
#     i = 1
#     sol = arg[0]
#     while(i < len(arg)):
#         sol *= arg[i] 
#         i += 1
# def division(arg):
#     i = 1
#     sol = arg[0]
#     while(i < len(arg)):
#         sol /= arg[i] 
#         i += 1

input = []
# Display basic calculator options
def calculatorGUI():
    try:
        inputFlag = False
        calcRoot = Tk()
        frame = ttk.Frame(calcRoot, padding=20)
        calcGrid = frame.grid()

        # Create output label
        solution = ttk.Label(frame, text=0, justify=RIGHT, padding=5).grid(column=2, row=0)
    

        # Create each button - separated by row for easier browsing
        btn0 = ttk.Button(frame, text=0, command= lambda: inputNum(frame, 0)).grid(column=2, row=7)
        equalsBtn = ttk.Button(frame, text="=", command= lambda: inputOp(frame, '=')).grid(column=4, row=7)

        btn1 = ttk.Button(frame, text=1, command= lambda: inputNum(frame, 1)).grid(column=1, row=6)
        btn2 = ttk.Button(frame, text=2, command= lambda: inputNum(frame, 2)).grid(column=2, row=6)
        btn3 = ttk.Button(frame, text=3, command= lambda: inputNum(frame, 3)).grid(column=3, row=6)

        btn4 = ttk.Button(frame, text=4, command= lambda: inputNum(frame, 4)).grid(column=1, row=5)
        btn5 = ttk.Button(frame, text=5, command= lambda: inputNum(frame, 5)).grid(column=2, row=5)
        btn6 = ttk.Button(frame, text=6, command= lambda: inputNum(frame, 6)).grid(column=3, row=5)
        addBtn = ttk.Button(frame, text='+', command= lambda: inputOp(frame, '+')).grid(column=4, row=5)
        
        btn7 = ttk.Button(frame, text=7, command= lambda: inputNum(frame, 7)).grid(column=1, row=4)
        btn8 = ttk.Button(frame, text=8, command= lambda: inputNum(frame, 8)).grid(column=2, row=4)
        btn9 = ttk.Button(frame, text=9, command= lambda: inputNum(frame, 9)).grid(column=3, row=4)
    except:
        loadingFailed()


# Functions to display the input of the user
def inputNum(frame, x = ''):
    try:
        input1 = x
        solution = ttk.Label(frame, text=input1, justify=RIGHT, padding=5).grid(column=2, row=0)
        input.append(input1)
    except:
        inputFailed()

def inputOp(frame, sym):
    try:
        if(sym == '='):
            solution = ttk.Label(frame, text=sym, justify=RIGHT, padding=5).grid(column=2, row=0)
            print(input)
            sol = addition(input)
            solution = ttk.Label(frame, text=sol, justify=RIGHT, padding=5).grid(column=2, row=0)
            showCalcuation(frame, sol)
            input.clear()
        else:
            inputSym = sym
            if(inputSym == '+'):
                solution = ttk.Label(frame, text=sym, justify=RIGHT, padding=5).grid(column=2, row=0)
            elif(inputSym == '-'):
                print()
            elif(inputSym == '*'):
                print()
            elif(inputSym == '/'):
                print()
            
    except:
        inputFailed()

def showCalcuation(frame, ans):
    answer = ttk.Label(frame, text=ans, justify=CENTER, padding=5).grid(column=2, row=8)

def temperatureGUI():
    tRoot = Tk()
    tFrame = ttk.Frame(tRoot, padding=20)
    tGrid = tFrame.grid()

    frontLabel = ttk.Label(tFrame, text="Temperature Converter", justify=CENTER, padding=5).grid(column=1, row=0)
    fromLabel = ttk.Label(tFrame, text="From:", justify=LEFT, padding=5).grid(column=0, row=1)
    toLabel = ttk.Label(tFrame, text="To:", justify=RIGHT, padding=5).grid(column=2, row=1)

    # Create options
    option_menu = ttk.OptionMenu()

def unitConverterGUI():
    OPTIONS = ["Foot", "Inch", "Mile", "Yard", "Kilometer", "Meter", "Centimeter", "Millimeter", "Micrometer", "Nanometer"]
    ucRoot = Tk()
    ucFrame = ttk.Frame(ucRoot, padding=20)
    ucGrid = ucFrame.grid()

    variable = StringVar(ucRoot)
    variable.set(OPTIONS[0])    # default value

    topLabel = ttk.Label(ucFrame, text="Unit Converter", justify=CENTER, padding=5).grid(column=1, row=0)
    fromLabel = ttk.Label(ucFrame, text="From:", justify=LEFT, padding=5).grid(column=0, row=1)
    toLabel = ttk.Label(ucFrame, text="To:", justify=RIGHT, padding=5).grid(column=2, row=1)
    
    # Dropdown menu creation
    opMenu = OptionMenu(ucRoot, variable, OPTIONS[0], *OPTIONS, optionChanged)

    # Output label
    unit_output = ttk.Label(ucFrame, text="testing", foreground='red').grid(column=1, row=3)

    print("Unit Converter")

def optionChanged():
    print("Unit change")

def loadingFailed():
    fRoot = Tk()
    roots.append(fRoot)
    fFrame = ttk.Frame(fRoot, padding=20)
    fGrid = fFrame.grid()
    fLabel = ttk.Label(fFrame, text="Loading process interupted.", justify=CENTER, padding=3).grid(column=1, row=1)
    fBtn = ttk.Button(fFrame, text="Close", command=fRoot.destroy).grid(column=2, row=2)

def menuFailed():
    mRoot = Tk()
    mFrame = ttk.Frame(mRoot, padding=20)
    mGrid = mFrame.grid()
    mLabel = ttk.Label(mFrame, text="Menu failed to load.", justify=CENTER, padding=3).grid(column=1, row=1)
    mBtn = ttk.Button(mFrame, text="Close", command=mRoot.destroy).grid(column=2, row=2)

def inputFailed():
    iRoot = Tk()
    roots.append(iRoot)
    iFrame = ttk.Frame(iRoot, padding=20)
    iGrid = iFrame.grid()
    iLabel = ttk.Label(iFrame, text="Input failed.", justify=CENTER, padding=3).grid(column=1, row=1)
    iBtn = ttk.Button(iFrame, text="Close", command=iRoot.destroy).grid(column=2, row=2)

startupMenu()


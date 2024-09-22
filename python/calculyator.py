# # from tkinter import *
# # from tkinter import ttk
# # root = Tk()
# # root.title("Calculyator")
# # frm = ttk.Frame(root, padding=10)
# # frm.grid()
# # ttk.Label(frm, text="Calculyator").grid(column=0, row=0)
# # ttk.Button(frm, text="chiqish", command=root.destroy).grid(column=1, row=0)
# # root.mainloop() 


# # vidio degi tkinter

# import tkinter
# from tkinter import *
# import math


# root=Tk()
# root.title("Calculator")
# root.geometry("570x600+100+200")
# root.resizable(False,False)
# root.configure(bg="#17161b")

# equation = ""

# def show(value):
#     global equation
#     equation+=value
#     label_result.config(text=equation)

# def clear():
#     global equation
#     equation = ""
#     label_result.config(text=equation)



# def calculate():
#     global equation
#     result = ""
#     if equation != "":
#         try:
#             result = eval(equation)
#         except:
#             result = "error"
#             equation = ""
#     label_result.config(text=result)



# def sinus(angle):
#     return math.sin(angle)

# def kosinus(angle):
#     return math.cos(angle)

# # def calculate_sqrt():
# #         num = 0
# #         sqrt = math.sqrt(num)
# #         result_label.config(text="Квадратный корень из числа " + str(num) + " это " + str(sqrt))



# # num = 0
# # sqrt = math.sqrt(num)
# # print("Квадратный корень из числа " + str(num) + " это " + str(sqrt))




# label_result= Label(root, width=25,height=2,text="",font=("arial",30))
# label_result.pack() 

# Button(root,text="C",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda:  clear()).place(x=10,y=100)
# Button(root,text="/",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("/")).place(x=150,y=100)
# Button(root,text="%",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("%")).place(x=290,y=100)
# Button(root,text="*",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("*")).place(x=430,y=100)

# Button(root,text="7",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("7")).place(x=10,y=200)
# Button(root,text="8",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("8")).place(x=150,y=200)
# Button(root,text="9",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("9")).place(x=290,y=200)
# Button(root,text="-",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("-")).place(x=430,y=200)


# Button(root,text="4",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("4")).place(x=10,y=300)
# Button(root,text="5",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("5")).place(x=150,y=300)
# Button(root,text="6",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("6")).place(x=290,y=300)
# Button(root,text="+",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("+")).place(x=430,y=300)
# Button(root,text="**",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("**")).place(x=430,y=400)
# Button(root, text='Sin', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: sinus(sinus)).place(x=570, y=300)
# Button(root, text='Cos', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: kosinus(kosinus  )).place(x=570, y=400)


# Button(root,text="1",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("1")).place(x=10,y=400)
# Button(root,text="2",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("2")).place(x=150,y=400)
# Button(root,text="3",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("3")).place(x=290,y=400)
# Button(root,text="0",width=11, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show("0")).place(x=10,y=500)

# Button(root,text=".",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36", command=lambda: show(".")).place(x=290,y=500)
# Button(root,text="=",width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#fe9037", command=lambda: calculate() ).place(x=430,y=500)


# root.mainloop()













# # clas siz calculate HATO LIY BILAN BU

# from tkinter import*
# import math
# import textwrap

# cal = Tk()
# cal.title("Calculator")
# operator= ""
# text_Input = StringVar()

# textDisplay = Entry(cal, font=('fixedsys', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
#                     bg='Orange', justify='right').grid(columnspan=4)


# def btnClick(number):
#     global operator
#     operator = operator + str(number)
#     text_Input.set(operator)

# def btnClear():
#     global opderator
#     operator=''
#     text_Input.set('')

# def btnEquals():
#     global operator
#     result = str(eval(operator))
#     text_Input.set(result)
#     operator=''

# class Calc():
#     def __init__(self):
#         self.total=0
#         self.total=""
#         self.input_value = True
#         self.check_sum = False
#         self.op = ""
#         self.result = False

#     def display(self, value):
#         txtDisplay.delete(0, END)
#         txtDisplay.insert(0, value)

#     def btnsin(self):
#         self.result = False
#         self.current = math.sin(float(txtDisplay.get()))
#         self.display(self.current)

#     def btncos(self):
#         self.result = False
#         self.current = math.cos(float(txtDisplay.get()))
#         self.display(self.current)

#     def btntan(self):
#         self.result = False
#         self.current = math.tan(float(txtDisplay.get()))
#         self.display(self.current)



# added_value = Calc()

# #SIN, COS AND TAN BUTTONS
# btnsin=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='Sin', bg='Blue', command=added_value.btnsin).grid(row=1, column=0)

# btncos=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='Cos', bg='Blue', command=added_value.btncos).grid(row=1, column=1)

# btntan=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='Tan', bg='Blue', command=added_value.btntan).grid(row=1, column=2)

# #Buttons

# btn7=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='7', bg='Blue', command=lambda:btnClick(7)).grid(row=2, column=0)

# btn8=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='8', bg='Blue', command=lambda:btnClick(8)).grid(row=2, column=1)

# btn9=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='9', bg='Blue', command=lambda:btnClick(9)).grid(row=2, column=2)

# btnAdd=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='+', bg='Blue', command=lambda:btnClick('+')).grid(row=2, column=3)

# #MoreButtons

# btn4=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='4', bg='Blue', command=lambda:btnClick(4)).grid(row=3, column=0)

# btn5=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='5', bg='Blue', command=lambda:btnClick(5)).grid(row=3, column=1)

# btn6=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='6', bg='Blue', command=lambda:btnClick(6)).grid(row=3, column=2)

# btnSub=Button(cal, padx=16, pady=16, bd=8, fg='white', font=('fixedsys', 20, 'bold'),
#             text='-', bg='Blue', command=lambda:btnClick('-')).grid(row=3, column=3)

# #MoreButtons2

# btn1=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='1', bg='Yellow', command=lambda:btnClick(1)).grid(row=4, column=0)

# btn2=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='2', bg='Yellow', command=lambda:btnClick(2)).grid(row=4, column=1)

# btn3=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='3', bg='Yellow', command=lambda:btnClick(3)).grid(row=4, column=2)

# btnTimes=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='x', bg='Yellow', command=lambda:btnClick('*')).grid(row=4, column=3)

# #MoreButtons3

# btn0=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='0', bg='Yellow', command=lambda:btnClick(0)).grid(row=5, column=0)

# btnClear=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='C', bg='Yellow', command=btnClear).grid(row=5, column=1)

# btnEquals=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='=', bg='Yellow', command=btnEquals).grid(row=5, column=2)

# btnDivide=Button(cal, padx=16, pady=16, bd=8, fg='black', font=('fixedsys', 20, 'bold'),
#             text='/', bg='Yellow', command=lambda:btnClick('/')).grid(row=5, column=3)


# #End Main Loop
# cal.mainloop()



# class calculate
from tkinter import *
import math

# Create main calculator window
cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

# Display entry
txtDisplay = Entry(cal, font=('Arial', 24, 'bold'), textvariable=text_Input, bd=10, insertwidth=4,
                    bg='#2e2e2e', fg='white', justify='right')
txtDisplay.grid(columnspan=4, pady=10)

# Button click function
def btnClick(number):
    global operator
    operator += str(number)
    text_Input.set(operator)

# Clear button
def btnClear():
    global operator
    operator = ''
    text_Input.set('')

# Equals button
def btnEquals():
    global operator
    try:
        result = str(eval(operator))
        text_Input.set(result)
    except Exception:
        text_Input.set("Error")
    operator = ''

# Calculator operations class
class Calc:
    def __init__(self):
        self.current = 0
        self.result = False

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def btnsin(self):
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)

    def btncos(self):
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)

    def btntan(self):
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def btnctg(self):
        self.current = 1 / math.tan(float(txtDisplay.get()))
        self.display(self.current)

# Create calculator instance
added_value = Calc()

# Function to create buttons
def create_button(text, row, column, command, bg_color='#444', fg_color='white'):
    return Button(cal, padx=20, pady=20, bd=0, text=text, bg=bg_color, fg=fg_color,
                  font=('Arial', 18, 'bold'), activebackground='#666', activeforeground='white',
                  relief=GROOVE, command=command).grid(row=row, column=column, sticky='nsew')

# Set grid weights for better button sizing
for i in range(6):
    cal.grid_rowconfigure(i, weight=1)
    cal.grid_columnconfigure(i, weight=1)

# Trigonometric buttons
create_button('Sin', 1, 0, added_value.btnsin)
create_button('Cos', 1, 1, added_value.btncos)
create_button('Tan', 1, 2, added_value.btntan)
create_button('Ctg', 1, 3, added_value.btnctg)

# Basic buttons
create_button('7', 2, 0, lambda: btnClick(7))
create_button('8', 2, 1, lambda: btnClick(8))
create_button('9', 2, 2, lambda: btnClick(9))
create_button('+', 2, 3, lambda: btnClick('+'))

create_button('4', 3, 0, lambda: btnClick(4))
create_button('5', 3, 1, lambda: btnClick(5))
create_button('6', 3, 2, lambda: btnClick(6))
create_button('-', 3, 3, lambda: btnClick('-'))

create_button('1', 4, 0, lambda: btnClick(1), bg_color='#ffb74d')
create_button('2', 4, 1, lambda: btnClick(2), bg_color='#ffb74d')
create_button('3', 4, 2, lambda: btnClick(3), bg_color='#ffb74d')
create_button('*', 4, 3, lambda: btnClick('*'))

create_button('0', 5, 0, lambda: btnClick(0), bg_color='#ffb74d')
create_button('C', 5, 1, btnClear, bg_color='red')
create_button('=', 5, 2, btnEquals, bg_color='green')
create_button('/', 5, 3, lambda: btnClick('/'))

# Run the main loop
cal.mainloop()
    



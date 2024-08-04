import tkinter

font = ('OpenSymbol', 10, 'bold')

#window
windows = tkinter.Tk()
windows.title("BMI Calculator")
windows.geometry("300x300+600+240")

#mainlabel
mainlabel = tkinter.Label(text="BMI Calculator", font=font)
mainlabel.pack()

#height
label1 = tkinter.Label(text="Your Height: \n (cm as an integer)", font=font,padx=5, pady=5)
label1.pack()
text1 = tkinter.Entry()
text1.pack()
text1.focus()

#weight
label2 = tkinter.Label(text="Your Weight: \n (kg as an integer)", font=font, padx=5, pady=5)
label2.pack()
text2 = tkinter.Entry()
text2.pack()

def bmi_calculation():
    heightm = float(text1.get())/100
    weightkg = float(text2.get())
    bmi_result = weightkg/heightm**2
    if bmi_result < 18.5:
        finallabel.config(text="Your BMI status is UNDERWEIGHT")
    elif bmi_result >= 18.5 and bmi_result < 25:
        finallabel.config(text="Your BMI status is NORMAL")
    elif bmi_result >= 25 and bmi_result < 40:
        finallabel.config(text="Your BMI status is OVERWEIGHT")
    elif bmi_result >= 40:
        finallabel.config(text="Your BMI status is OBESE")
    else:
        finallabel.config(text="Enter the right values")


def bmi_calculator():
    if text1.get() == "" or text2.get() == "":
        finallabel.config(text="Please fill the blanks!")

    elif (text1.get()).isdigit() and (text2.get()).isdigit() == True:
        bmi_calculation()

    else:
        finallabel.config(text="Please enter a digit!")

button1 = tkinter.Button(text="Calculate", font=font, command=bmi_calculator)
button1.pack(padx=5, pady=5)

finallabel = tkinter.Label(font=font)
finallabel.pack()

windows.mainloop()
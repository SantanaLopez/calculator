from tkinter import *
import tkinter as tk



result = 0.0

def add():
    global result 

    first=entry.get()


    #Get result
    try:
        result_1 = float(first)
        label_3.config(text=f"Current Number you are adding with: {result_1}")
        result += result_1
        label_4.config(text=result)
        return result
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("Invalid input! Please enter a valid number.")
        label_3.config(text="Invalid input!")


def sub():

    global result
    #Get the first Number
    first=entry.get()



    #Get result
    try:
        result_1 = float(first)
        label_3.config(text=f"Current Number you are subtracting with: {result_1}")
        result -= result_1
        label_4.config(text=result)
        return result
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("Invalid input! Please enter a valid number.")
        label_3.config(text="Invalid input!")

def multiply():
    global result
    #Get the first Number
    first=entry.get()
    label.config(text=first)



    #Get result
    try:
        result_1 = float(first)
        label_3.config(text=f"Current Number you are multiplying with: {result_1}")
        result *= result_1
        label_4.config(text=result)
        return result
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("Invalid input! Please enter a valid number.")
        label_3.config(text="Invalid input!")

def divide():
    global result
    #Get the first Number
    first=entry.get()



    #Get result
    try:
        result_1 = float(first)
        label_3.config(text=f"Current Number you dividing with: {result_1}")
        result /= result_1
        label_4.config(text=result)
        return result
    except ValueError:
        # Handles the case where the input is not a valid integer
        print("Invalid input! Please enter a valid number.")
        label_3.config(text="Invalid input!")

def clear():
    global result
    result = 0.0
    label_3.config(text="")
    label_4.config(text=result)
    return result

#main application
root = tk.Tk()
root.title("Calculator")
root.geometry("800x600")



#creating widget
entry = tk.Entry(root, width=20)
entry.pack(pady=20)

#create button to display numbers
button = tk.Button(root, text="+",
                   command=add)
button.pack(pady=10)

button = tk.Button(root, text="-",
                   command=sub)
button.pack(pady=10)

button = tk.Button(root, text="*",
                   command=multiply)
button.pack(pady=10)

button = tk.Button(root, text="/",
                   command=divide)
button.pack(pady=10)

button = tk.Button(root, text="CLR",
                   command=clear)
button.pack(pady=10)

# Create a Label widget to display the text
label = tk.Label(root, text="Result:")
label.pack(pady=10)

# Create a Label widget to display the text
label_2 = tk.Label(root, text="")
label_2.pack(pady=10)

label_3 = tk.Label(root, text="")
label_3.pack(pady=10)

label_4 = tk.Label(root, text="")
label_4.pack(pady=10)

root.mainloop()



#ALL YOUR FUNCTIONALITY SHOULD BE AT THE TOP

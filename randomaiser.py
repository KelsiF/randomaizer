import tkinter as tk
import random
from tkinter import ttk
from tkinter.font import Font

#functions
def random1():
	num1 = entryInt.get()
	num2 = entryInt2.get()
	result = random.randint(num1, num2)
	output_string.set(result)

def yesorno():
	result = False
	num = random.randint(0, 1)
	if num == 0:
		result = False
	if num == 1:
		result = True
	output_boolean.set(result)

#window
window = tk.Tk()
window.title("Randomaizer")
window.geometry('800x650')

#titles
title_label = ttk.Label(master = window, text = "Randomaizer", font = 'Nunito 24 bold').grid(row = 0, column = 1, columnspan = 2)
number_label1 = ttk.Label(master = window, text = "range of numbers", font = "Nunito 22").grid(row = 1, column = 1)
number_label2 = ttk.Label(master = window, text = "first num", font = "Nunito 18 italic").grid(row = 2, column = 0)
number2_label = ttk.Label(master = window, text = "second num", font = "Nunito 18 italic").grid(row = 2, column = 2)
title_label_yesorno = ttk.Label(master = window, text = "Yes or No", font = "Nunito 22").grid(row  = 7, column = 1)


#input
input_frame = ttk.Frame(master = window).grid(row = 3, column = 0) #text = "range of numbers (write only the largest number
entryInt = tk.IntVar()
entryInt2 = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt).grid(row = 4, column = 0)
entry2 = ttk.Entry(master = input_frame, textvariable = entryInt2).grid(row = 4, column = 2)
button = ttk.Button(master = input_frame, text = "randomaize", command = random1).grid(row = 5, column = 1)
button_yesorno = ttk.Button(master = input_frame, text = "start", command = yesorno).grid(row = 8, column = 1)


#output
output_string = tk.StringVar()
output_boolean = tk.BooleanVar()
output_label = ttk.Label(master = window, text = "result", font = "Nunito 24", textvariable = output_string).grid(row = 6, column = 1)
output_yesorno = ttk.Label(master = window, text = "result", font = "Nunito 24", textvariable = output_boolean).grid(row = 9, column = 1)

#run
window.mainloop()	
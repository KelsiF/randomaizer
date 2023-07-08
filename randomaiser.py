import tkinter as tk
import random
from tkinter import ttk

#functions
def random1():
	num1 = 1
	num2 = entryInt.get()
	result = random.randint(num1, num2)
	output_string.set(result)

#window
window = tk.Tk()
window.title("Randomaizer")
window.geometry('800x650')

#titles
title_label = ttk.Label(master = window, text = "Randomaizer", font = 'Calibri 24 bold').grid(row = 0, column = 1, columnspan = 2)
number_label1 = ttk.Label(master = window, text = "range of numbers", font = "Calibri 22").grid(row = 1, column = 0)
number_label2 = ttk.Label(master = window, text = "(write only the largest number)", font = "Calibri 18 italic").grid(row = 2, column = 0)


#input
input_frame = ttk.Frame(master = window).grid(row = 3, column = 0) #text = "range of numbers (write only the largest number
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt).grid(row = 4, column = 0)
button = ttk.Button(master = input_frame, text = "randomaize", command = random1).grid(row = 5, column = 0)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "result", font = "Calibri 24", textvariable = output_string).grid(row = 6, column = 0)	

#run
window.mainloop()
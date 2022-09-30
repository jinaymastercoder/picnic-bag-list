# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 11:05:55 2022

@author: Nirav
"""
from tkinter import *

root=Tk()
root.title("sales project")

root.geometry("400x400")
root.configure(background = 'aqua')


month = ("January", "February", "March", "April", "May", "June", "July", "August", "September" ,
"October", "November", "December")

profits = (20000, 45000,78008,97080, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000) 

label_month = Label(root)
label_month["text"] = " month :" + str(month)
print(profits)

max_profit = max(profits) 
max_profit_index = profits.index(max_profit) 
print(max_profit_index)
max_profit_month = month[max_profit_index] 
print("The maximum profit of " + str(max_profit)+ " was recorded in the month of "
+ str(max_profit_month))

min_profit = min(profits) 
min_profit_index = profits.index(min_profit) 
print(min_profit_index)
min_profit_month = month[min_profit_index] 
print("The minimum profit of " + str(min_profit)+ " was recorded in the month of "
+ str(min_profit_month))

root.mainloop()
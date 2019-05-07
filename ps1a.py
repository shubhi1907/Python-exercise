# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary you plan on saving monthly: "))
total_cost = float(input("Enter the price of your dream house: "))
count = 1
current_savings = 0
monthly_salary = annual_salary / 12
ps = monthly_salary*portion_saved/100
portion_down_payment = 0.25*total_cost
s = current_savings + ps
print("The portion of the down payment due for the dream house is ", portion_down_payment)

while s<portion_down_payment:
    count += 1 
    s *= (0.04/12 + 1) 
    s += ps 
   
    
print("Number of Months till you can pay that due by saving monthly = ", count)

 
 
# -*- coding: utf-8 -*-
"""


@author: shubhi
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary you plan to save: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
count = 1
current_savings = 0
monthly_salary = annual_salary / 12
ps = monthly_salary*portion_saved/100
portion_down_payment = 0.25*total_cost
s = current_savings + ps
#print("ms", monthly_salary)
#print("ps", ps)
#print("down", portion_down_payment)
#print("s", s)

while s<portion_down_payment:
    #print(monthly_return)
    count += 1 
    #print("count", count)
    #print("ps before if ", ps)
    if count%6 == 1:
        annual_salary *= (1 + semi_annual_raise)
        ms = annual_salary / 12
        nps = ms*portion_saved/100
        #s *= (0.04/12 + 1)
        #s += nps
        ps = nps
        #break
#        s *= (0.04/12 + 1)
#        s += ps
#    else:
    #print("ps after if ", ps)
    s *= (0.04/12 + 1)
    s += ps
    #print("current_savings", current_savings)
    #print("saved", s)
    
print("Number of months: ", count)

 
 
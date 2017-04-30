# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:11:48 2017

@author: Oksana Borovyk
"""

year_salary = float (input ("Input your year salary - "))
total_coast = float (input ("Input total coast your dream house - "))
k = float (input ("Input parth of salary in %  - "))
count_month = 0
month_salary = year_salary / 12
saving = month_salary * k / 100
parth_down_payment = total_coast * 0.25
current_saving = 0

while current_saving <= parth_down_payment:
    current_saving = current_saving * 0.04 / 12  + saving  + current_saving
    count_month = count_month + 1
    
print (count_month)



year_salary = float (input ("Input your year salary - "))
total_coast = float (input ("Input total coast your dream house - "))
semmi_annual = float (input ("Enter the semi­annual raise, as a decimal: - "))
k = float (input ("Enter the percent of your salary to save, in %  - "))
count_month = 0
month_salary = year_salary / 12
saving = month_salary * k / 100
parth_down_payment = total_coast * 0.25
current_saving = 0

while current_saving <= parth_down_payment:
    current_saving = current_saving * 0.04 / 12  + saving  + current_saving
    count_month = count_month + 1
    if count_month % 6 == 0:
        month_salary = month_salary * (1 + semmi_annual)
        saving = month_salary * k / 100


print (count_month)





annual_salary = float(input("enter your annual salary: "))
percent_saved = float(input("enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("enter the cost of your dream home: "))
percent_down_payment = 0.12
amount_saved = 0.0
r = 0.06

down_payment = total_cost * percent_down_payment
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * percent_saved
months = 0
while(amount_saved < down_payment):
	amount_saved += monthly_saved + (amount_saved * r / 12)
	months += 1
print("Number of months: ", months)
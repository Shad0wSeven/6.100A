## 6.100A Pset 1: Part b
## Name: Ayush Nayak
## Time Spent: 3 minutes
## Collaborators: None

##################################################################################
## Get user input for annual_salary, percent_saved and total_cost_of_home below ##
##################################################################################

annual_salary = float(input("enter your annual salary: "))
percent_saved = float(input("enter the percent of your salary to save, as a decimal: "))
total_cost_of_home = float(input("enter the cost of your dream home: "))
semi_annual_raise = float(input("enter the semi-annual raise, as a decimal: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

percent_down_payment = 0.12
amount_saved = 0.0
r = 0.06


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


down_payment = total_cost_of_home * percent_down_payment
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * percent_saved
months = 0
while(amount_saved < down_payment):
	amount_saved += monthly_saved + (amount_saved * r / 12)
	months += 1
	if(months % 6 == 0):
		monthly_salary += monthly_salary * semi_annual_raise
		monthly_saved = monthly_salary * percent_saved
print("Number of months: ", months)
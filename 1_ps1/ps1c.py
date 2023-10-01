## 6.100A Pset 1: Part c
## Name:Ayush Nayak
## Time Spent: 10 minutes
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("enter your initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_home = 800000
down_payment = cost_of_home * 0.12

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

r = 0.5

def amount_saved(r):
	return initial_deposit * (1 + r / 12) ** 36

if initial_deposit > down_payment:
	print("0.0")

low = 0.0
high = 1.0
steps = 1


if(amount_saved(high) < down_payment):
	print("Best savings rate: None")
	print("Steps in bisection search: 0")
	exit()

while(abs(amount_saved(r) - down_payment) > 100):
	if(amount_saved(r) < down_payment):
		low = r
	else:
		high = r
	r = (low + high) / 2
	steps += 1

print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
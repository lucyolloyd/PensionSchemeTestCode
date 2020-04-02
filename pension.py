import math

def invSplit(t,r1,r2,p1,p2,y):
    p1=p1/100
    p2=p2/100
    return t*(1-r1)*(1-r2)/(p1*r1*(1-r1**y)*(1-r2)+p2*r2*(1-r2**y)*(1-r1))

#Fixed variables/assumptions
state_pen_pa = 8767.2 #state pension per year
ret_age = 66 #Offical retirement age
fundReturn=1.06
bondReturn=1.02

#Life expectancy
le60_69f = 74.56 #female born between 1960 and 1969
le70_79f = 75.81 #female born between 1970 and 1979
le80_89f = 77.67 #female born between 1980 and 1989
le90_98f = 79.29 #female born between 1990 and 1998
le60_69m = 68.42 #male born between 1960 and 1969
le70_79m = 69.62 #male born between 1970 and 1979
le80_89m = 71.84 #male born between 1980 and 1989
le90_98m = 73.96 #male born between 1990 and 1998


#User dependent variables
salary = float(input("Yearly salary: £"))
gen = str(input("Gender: "))
gen_low = gen.lower()
                
dob = float(input("Year of Birth: "))
if 1960 <= dob <= 1969 and gen_low == 'female':
    life_exp = le60_69f
elif 1970 <= dob <= 1979 and gen_low == 'female':
    life_exp = le70_79f
elif 1980 <= dob <= 1989 and gen_low == 'female':
    life_exp = le80_89f
elif 1990 <= dob <= 1998 and gen_low == 'female':
    life_exp = le90_98f
elif 1960 <= dob <= 1969 and gen_low == 'male' :
    life_exp = le60_69m
elif 1970 <= dob <= 1979 and gen_low == 'male' :
    life_exp = le70_79m
elif 1980 <= dob <= 1989 and gen_low == 'male' :
    life_exp = le80_89m
elif 1990 <= dob <= 1998 and gen_low == 'male':
    life_exp = le90_98m    
else:
    print("You are too young to start a pension.")

    
pen_pa = 20000 #average cost of a comfortable year in retirement

total_contrib = ((life_exp - ret_age)*pen_pa)-((life_exp - ret_age)*state_pen_pa) #total amount required by employee and employer combined

percFund = float(input("Percentage invested in funds: "))
percBond = 100-percFund
print("Percentage invested in bonds: ",percBond)
contrib_pa = invSplit(total_contrib,fundReturn,bondReturn,percFund,percBond,ret_age-(2020-dob)) #calls the invSplit function
    

print("Age: ", (2020-dob))
print("Yearly salary: £", salary)

print("Yearly total amount needed to cover the cost of retirement: £",contrib_pa)

employer_contrib = round(0.05 * salary,2) 
print("Employer will contribute 5%.")
print("Employer contributes £", employer_contrib)
employee_min = round(0.03 * salary, 2)
print("Employee must contribute a minimum 3% to meet legal requirement.")
print("Minimum yearly contribution for employee: £", employee_min)

if (employee_min + employer_contrib) >= contrib_pa: #checks whether combined employer and employee amount is enough
    print("This is enough to cover the cost of retirement.")
else:
    employee_min = contrib_pa - employer_contrib
    perc = employee_min/salary
    perc = perc * 100
    perc = math.ceil(perc) #rounds percentage UP to the nearest integer
    print("This is not enough to cover the cost of retirement.")
    print("You need to increase the employee contribuion to ",perc,"%")

    


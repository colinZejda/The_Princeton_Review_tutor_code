print("Newspaper Salary Calculator")

# prompt user for values 
papers_per_day = int(input("Enter number of papers delivered on the route per day: " ))
times_per_week = int(input("Now enter number of days the paper is delivered per week: "))
tips_per_week  = int(input("Lastly enter amount of tips received per week: "))

# define constants 
cost_per_paper = 2.45        # assign float value of 2.45 into my_const variable
my_commission = 0.08         # raw numbers, no %, no $

# perform calculations (things to print)
num_papers_per_week = papers_per_day * times_per_week
weekly_salary       = num_papers_per_week * cost_per_paper * my_commission
weekly_total        = weekly_salary + tips_per_week 

# print variables from lines 13-15
print("Number of papers delivered this week:", num_papers_per_week)
print("Your weekly salary is: $", weekly_salary)
print("Your total income for the week: $", weekly_total)

"""
Grading:

10% - Design – outline proper sequence of steps, calculations (if necessary). Identify values of any known constants (e.g. commission rate). Identify what the user inputs will be and what the output will be.

Design:

Steps: First, get input from user. Next, define constants. Then, perform calculations for output values. Lastly, show results.

Calculations: 

num_papers_per_week = papers_per_day * times_per_week

weekly_salary = num_papers_per_week * cost_per_paper * my_commission

weekly_total = weekly_salary + tips_per_week 



Known constants: cost per paper is $2.45,  and my commission is 8%

User inputs: prompt user to input 3 things: number of papers delivered each day, how many days per week and how much money gained in tips.

Output: print results of calculations: papers delivered per week, weekly salary and total income per week



10% - Completeness of your Test plan (at least three test cases). Include screenshots for each test case.

10% - Documentation - Header and in-line comments. Include documentation for the values you chose as the known constants (hourly rate, commission rate) in your comments as well. Documentation of major steps (from Design outline). 

70% - Program prompts and executes correctly on all test cases. Satisfies all requirements, compiles, effectiveness and neatness, descriptive variables, def main
"""
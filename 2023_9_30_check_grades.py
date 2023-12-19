def main():
    
    grade = input("Enter your numeric grade: ")      # input grade
    
    # if regular int, or negative int
    if grade.isdigit() or (grade[0] == '-' and grade[1:].isdigit()):      
        numeric_grade = int(grade)                   # directly convert found int to int
        
        # process nested if-else statements
        if numeric_grade >= 90 and numeric_grade <= 100:
            print("Your grade is: A ")
        elif numeric_grade >= 80 and numeric_grade <= 89:
            print("Your grade is: B ")
        elif numeric_grade >= 70 and numeric_grade <= 79:
            print("Your grade is: C ")
        elif numeric_grade >= 60 and numeric_grade <= 69:
            print("Your grade is: D ")
        elif numeric_grade >= 0 and numeric_grade <= 59:
            print("Your grade is: F ")
        
        # detects int out of bounds
        if numeric_grade < 0 or numeric_grade > 100: 
        	print("invalid value")
    
    # line 6 got all integers, this else is for non-integers
    else:
        print("You must enter a number.")
         
    
           
if __name__ == "__main__": 	
	main()
#You are a manager of a  Wally's Training Gym and you encourage your trainers to enroll new members.  
#Input is the trainer's last name and the number of new enrollees.  
#Output is the number of trainers who have enrolled members in each of three categories:  
#0-5 new members, 6-10 new members, and 11 to 15 new members. 
#Write an application that allows the user to enter 15 Trainer's names and the number of new members they have enrolled into an array.   
#Output is to display the number of trainers who are in each category.  
#Use good programming techniques that you have learned throughout the course.  
#Use appropriate variable names, use an array to store the names and number of new enrollees, and use prompts for the input and labels with the display. 

def main():

	# counts
    zeroToFive=0
    sixToTen=0
    elevenToFifteen=0
    
    # arrays to store:
    trainerLastNames = []   # last names of the 15 trainers.
    newEnrolleesList = []       # number of new enrollees that each of the trainers recruit.    
	
    # prompting loop
    for x in range(15): # cycles 15 times to create a parallel array.
        trainerLastName = input("please enter the last name of the trainer: ")
        newEnrollees = int(input("please enter the amount of new enrollees that the trainer has recruited: "))
        # add to lists
        trainerLastNames.append(trainerLastName)  # adds the trainers last name to the array.
        newEnrolleesList.append(newEnrollees)         # adds the new enrollees to the array.
    
   	# iterate over newEnrollees list, categorize trainers
    for enrollees in newEnrolleesList: #cycle through 0-4 new enrollees for each trainer.
    	if enrollees >= 0 and enrollees <= 5:
            zeroToFive += 1
    if enrollees >=6 and enrollees <=10:
            sixToTen += 1
    if enrollees >=11 and enrollees <=15:
            elevenToFifteen += 1
    
    # print outputs
    print("category of new enrollees 0-5: ", zeroToFive)
    print("category of new enrollees 6-10: ", sixToTen)
    print("category of new enrollees 11-15: ", elevenToFifteen)
        
# run the program
main()
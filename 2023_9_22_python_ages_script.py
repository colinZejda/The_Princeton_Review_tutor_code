#import random for our generator
import random as random

# custom value-returning func
def reverse_sort_tutor_version(age_list):
    return age_list.sort(reverse=True)

# custom value returning function
def reverse_sort(x):
    x.sort()      # sort our list in the ascending order
    x.reverse()   # reverse the list
    return x      # return the corrected list
  
def main():
  
  	# use list comp to create age list
    age_list = [random.randint(1, 100) for x in range(100)]
    age_list = reverse_sort(age_list)

    #start a counter for our sum of the random age
    age_sum = 0

    # print ages (5x20 grid), accumulate age sum
    # note: 5x20 is rowxcol, so 5 rows, 20 col
    for i in range(len(age_list)):
        age_sum += x[i]                         # add to sum
        print(f'{age_list[i]:3}', end = ' ')   # print single age, then a space
        if (i + 1) % 20 == 0:                  # every 20 ages, start printing on newline
            print()

    #display the sum of all the ages
    print('Sum of all ages:', age_sum)
    
    #determine and print the oldest age
    print('Oldest age:', max(age_list))

    #determine and print the youngest age
    print('Youngest age:', min(age_list))

    #calculate the average age from the 100 random ages
    avg_age = age_sum / 100
    
    #display the average age
    print(f'Average age: {avg_age:.2f}')
            
    # better way to sum minors and seniors
    minors = sum(1 for age in age_list if age < 18)
    seniors = sum(1 for age in age_list if age > 65)
	college_students = [age in age_list if age >= 18 and age <= 21]
                  
    #display the number of minors in the list
    print('Number of minors:', minors)

    #display the number of seniors in the list
    print('Number of seniors:', seniors)

    #display the list of college aged adults
    print('The college-aged adults:', college_students)

if __name__ == '__main__':
	main()
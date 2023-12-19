import random

def main():
	# create a list called randoms
    randoms = list()

    # add 12 random nums between 50 and 100 to list
    for index in range(12):
        randoms.append(random.randint(50, 100))

    print('Here is the list of random integers...')
    for num in randoms:
        print(num, end= ' ')
    print()           # for formatting
    
    print('The 4th element in the list is', randoms[3])
    print('The element at index 9 is', randoms[8])
    print('The smallest element in the list is', min(randoms))

    # call change_list, pass randoms list in as argument
    new_list = change_list(randoms)
    print('change_list returned this sorted list... ')
    
    # display sorted changed list
    for num in new_list:
        print(num, end=' ')
    print()

def change_list(num_list):
    changedrandoms = num_list[3:9]
    print('The size of the list is now', len(changedrandoms))
    changedrandoms.sort()
    return changedrandoms

if __name__ == "__main__":
	main()

def main():
    print("This program calculates the volume of a box.")          # this line good
    
    # LENGTH
    print("What's the length of the box?")
    length = input('Please enter a whole number: ')
    while not length.isdigit() or int(length) <= 0:
        length = input("Enter a whole number greater than 0: ")
    length = int(length)
    
    # WIDTH
    print("Whats the width of the box? ")
    width = input('Please enter a whole number: ')
    while not width.isdigit() or int(width) <=0:
        width = input("Enter a whole number greater than 0: ")
    width = int(width)
    
    # HEIGHT
    print("Whats the height of the box? ")
    height = input('Enter height: ')
    while not height.isdigit() or int(width) <= 0:
        height = input("Enter a whole number greater than 0: ")
    height = int(height)
        
    calculate_volume(length, width, height)

def calculate_volume(length, width, height):         # pass variables from main() to this func
    '''This DOESN'T work as is – the
    calculate_volume function can't access variables
    from the main function. They are LOCAL to main.'''
    volume = length * width * height
    print('The volume of the box is: ', volume)

    
main() # will be revised in lab
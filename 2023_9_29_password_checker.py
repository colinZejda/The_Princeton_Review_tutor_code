#Password validation by Gary Plummer CMS105 9/29
#Minimum 8 characters.
#No spaces
#The alphabet must be between [a-z]
#At least one alphabet should be of Upper Case [A-Z]
#At least 1 number
#At least 1 character.

def main():

	Welcome()                                  # Explain expectations to users
	pw = input("\nEnter your password :  ")    # Prompt user for password

	#Validate password criteria
	caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lcase = "abcdefghijklmnopqrstuvwxyz"
	specialchar="_ or @ or $ or # or ^ or % or ^ * or +_ or ( or ) or - or _ or ="
	digits="0123456789"

	Valid()
	Space()

def Welcome():
    print("Requirements of a secure password require:")
    print("No spaces, 1 alpha, 1 numeric, one character, one upper, and one lower case key")

    #No null spaces
def Space():
    if " " in pw is true:
    	print("Space character not permitted in passwords")

    return space
    break
    
def Valid(pw):
	capsCount = sum(1 for c in pw if c.isupper())
    lcaseCount = sum(1 for c in pw if c.islower())
    
    
    if (len(pw) >= 8):
    	for char in pw:                # for loop
    		# rest of i-statements checking if char is lowercase, upper, special, or num
            # indentation INSIDE for loop tells us this code is inside the loop
    		

    	if (caps>=1 and lcase>=1 and specialchar>=1 and digits>=1 and caps+lcase+specialchar+digits>=len(pw)):
    		print("Valid Password")

   		else:
        	print("Invalid Password")

    

    print("Good work, your password is valid", valid)

#--- Execute --------------------------------------------------------
if __name__ == '__main__':
	main()
#Password validation by Gary Plummer CMS105 9/29
#Minimum 8 characters.
#No spaces
#The alphabet must be between [a-z]
#At least one alphabet should be of Upper Case [A-Z]
#At least 1 number
#At least 1 character.

def main():
	Welcome()                                  # Explain expectations to users
	pw = input("\nEnter your password :  ")    # Prompt user for password

	Valid()
	Space()

    
def Welcome():
    print("Requirements of a secure password require:")
    print("No spaces, 1 alpha, 1 numeric, one character, one upper, and one lower case key")

# No spaces allowed in password
def Space():
    if " " in pw:
    	print("Space character not permitted in passwords")

    
def Valid(pw):
	# upper and lower case 
	capsCount = sum(1 for c in pw if c.isupper())
    lcaseCount = sum(1 for c in pw if c.islower())

    # now for special characters and numbers
	digitCount = sum(1 for d in pw if d.isdigit())
    specialCount = sum(1 for c in pw if c in "_@#$%^*+()-_=")
    
    
    if (len(pw) >= 8):
    	if capsCount >= 1 and lcaseCount >= 1 and specialCount >= 1 and digitCount >=1:   # NEED ONE OF EACH
            print("Valid Password")
        else:
        	print("Invalid Password")
	else:
    	print("Password needs to be at least 8 characters long.")
        
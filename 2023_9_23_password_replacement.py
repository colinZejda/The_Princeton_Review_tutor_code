old_password = input("Enter a simple password: ")
new_password = ""

replacements = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}

for char in old_password:
    if char in replacements:
    	new_password += replacements[char]
	else:
		new_password += char
    
new_password += "q*s"
print(new_password)


# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    name_parts = personsName.split()
    intials_p = [name[0].upper() for name in name_parts]
    intials_str = '. '.join(intials_p) + '.'
    return intials_str  

try:
    personsName = input('Enter the user first, middle, and last name')
except EOFError:
    personsName = "John William Smith"


initials = initials_generator(personsName)

print(initials)
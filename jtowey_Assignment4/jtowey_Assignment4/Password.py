'''user enters a password...
is it strong enough?
    - 8 or more characters long 
    -at least 1 uppercase
    -at least 3 numbers 
    -should contain the word 'cat' once at least
    -1 question mark 
    -no spaces 
if it is not strong enough tell the user exactly what is missing and try again until valid'''


def strongPassword(p):                          #create a function with par. p
    int_counter = 0             #set variable for digit count later on
    global strength             #make strength a global variable so it works all the way through
    strength = 0                #set the variable strength
    if len(p) >= 7:             #length!!
        strength += 1           #if it is true add to strength 
    else:
        print("Must be 8 characters long")      #if it does not meet req. tell them why 

    if p.islower():
        print("Must have a uppercase letter")   #if it does not meet req. tell them why 
    else:
        strength += 1               #if it is true add to strength 

    index = 0               #set index to 0 for int count
    while index <= len(p) - 1:              
        if p[index].isdigit():
            int_counter += 1        #add to int for every digit in password
        index += 1
    if int_counter >= 3:            #if there are at least digits all good
        strength += 1                   #if it is true add to strength 
    else:
        print("You must have at least 3 digits")        #if it does not meet req. tell them why 

    if "cat" in p:
        strength += 1                   #if it is true add to strength 
    else:
        print("You need 'cat' inside your password'")       #if it does not meet req. tell them why 

    if "?" in p:
        strength += 1                   #if it is true add to strength 
    else:
        print("You need a question mark")       #if it does not meet req. tell them why 

    if " " in p:
        print("You can't have any spaces")      #if it does not meet req. tell them why 
    else:
        strength += 1                   #if it is true add to strength 


password = input("Enter your password:")            #just get password from user
result = strongPassword(password)

if strength == 6:                   #if all req. were met then there should be 6 added to strength so that will print 
    print("Success!")
else:
    print("Try again")
    password = input("Enter your password:")            #just get password from user
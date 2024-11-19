import random
num = random.randint(0 , 100)

def guess(number):            #func --> asks user for number and returns it
    return number

def comparator(a , b):          #func --> determines values greater or less than
    if a > b:                       
        return 0                #returns a value that is later assigned to inform user higher or lower
    elif a < b:
        return 1                #returns a value that is later assigned to inform user higher or lower
    else:
        return -1               #returns a value to tell user if they got it correct or not 

def remark(val):                # func --> returns to tell user higher or lower 
    if val == 0:
        print("You guessed higher!")                             #inform user to go higher or lower 
        numberUser = int(input("Enter a number:"))              #if it is not correct the first time it will keep going with this
        print(guess(numberUser))
        print(remark(comparator(guess(numberUser), num)))
    elif val == 1:
        print("You guessed lower")                              #inform user to go higher or lower 
        numberUser = int(input("Enter a number:"))              #if it is not correct the first time it will keep going with this
        print(guess(numberUser))
        print(remark(comparator(guess(numberUser), num)))
    else:
        print("You got it!")                                       #if user gets it it tells them and ends game


#to sart the program it starts outside function
numberUser = int(input("Enter a number:"))                     #asks for a number    
print(guess(numberUser))                                    #reprints that number
print(remark(comparator(guess(numberUser), num)))           #runs it through both functions to se set value and respond to user



import random                              #select random word from list

def printInstructions():                   #print the instructions to the user
    print("Enter a five-letter word:")

def getRandomWord():                       #select a random word from the list of words.txt
    with open("words.txt") as f:           #open file and do stuff within it 
        words = f.read().splitlines()      #line by line words 
        return random.choice(words)         #random function to call on it 

def readInput(): 
    with open("words.txt") as f:            #open file and do stuff within it 
        words = f.read().splitlines()       #line by line words 
        if word in words:
            return True
        else:                               #input if valid word in words.txt
            return False    

answer = getRandomWord()                    #set the answer to a random word 
guess = 0                                   #sets it at 0 so after everyone you can add to it. initialize 

while guess in range(6):                    #up to the guess number 
    printInstructions()                     #ask main question while range is still low
    userGuess = input().lower()             #make lower case so we can read
    if readInput(userGuess) == True:        #if the input user gives is the random read input 
        for i in range(0,5):
            if userGuess[i] == answer[i]:       #all the same         
                print(colored(userGuess[i], 'green'), end='')       #will color a letter if it is correct
            elif userGuess[i] in answer:        #in answer
                print(colored(userGuess[i], 'yellow'), end='')      #will color a letter if it is misplaces 
            else:                               #not at all
                print(colored(userGuess[i], 'grey'), end='')      #will color a letter if it is wrong

            i += 1                                      #letter to correctness 
        
        guess += 1                          #adds to guesses used 
    
        if userGuess == answer: 
            print("You guessed the word in", (guess + 1), "guesses!")       #tells user if they got it and how often
            exit()                                                          #stops it 

    else:
        guess -= 1
        print("Invalid guess. Try again!")        
print("Game over... no guesses")                    #what the real answer was and why they lost
print("The worlde was", answer)
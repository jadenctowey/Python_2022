'''map my work:
- user input seconds in a day 
- create a 24 hour clock 
- output three numbers hour minute second'''

#prompt for number between 1 - 86400 input
seconds = int(input("Enter a number between 1-86400:"))

#calculate a 24 hour clock 
hours = (seconds // 3600)
minutes = (seconds % 3600 // 60)
seconds2 = (seconds % 60)          #seconds2 so it is dif from seconds

#print the results
print("There are", hours, "hours,", minutes, "minutes, and", seconds2, "seconds.")


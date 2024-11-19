'''map my work:
- float input the sales tax and the price
- calculate the final price '''

#get the price 
price = float(input("What is price of the item:"))

#if statement so it only runs when the numbers are positive
if price >= 0:
    salesTax = float(input("What is the sales tax rate:"))       #if the price is positve then ask for the sales tax
    if salesTax >= 0:
        results = ((salesTax * .01 * price) + price)            #calculate the new price if both parts are positve
        print("The total price is:", results)                   #print the results of the calc
    else:                                                       #if there is a negative sales tax tell them
        print("There was an error! No negative numbers!") 
else:                                                           #if there is a negative price tell them
    print("There was an error! No negative numbers!")

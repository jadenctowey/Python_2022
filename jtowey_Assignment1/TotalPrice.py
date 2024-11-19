'''map my work:
- float input the sales tax and the price
- calculate the final price '''

#get the price and sales tax
price = float(input("What is price of the item:"))
salesTax = float(input("What is the sales tax rate:"))

#calculate the new price 
results = ((salesTax * .01 * price) + price)

#print the results of the calc
print("The total price is:", results)
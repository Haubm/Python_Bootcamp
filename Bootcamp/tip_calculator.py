#1. Create a greeting for the program
print("Welcome to the tip calculator!")
#2. Ask for total bill
bill = float(input("What was the total bill? $"))
#3. Ask for tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#4. Ask for number of people shared the bill
people = int(input("How many people to split the bill? "))
#5. Calculate the total bill with tip
bill_with_tip = ((tip / 100) * bill) + bill
#6. Notice the total bill eith tip
print("Your total bill with tip is: %.2f" % bill_with_tip)

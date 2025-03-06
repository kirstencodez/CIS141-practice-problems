#1. Construct a truth table for the expression:  (A AND B) OR (NOT B) where A and B each can be True or False. 
#Your truth table should be commented out (as it's not valid Python code!)
#A      B       A AND B     NOT B       (A AND B) OR (NOT B)
#True   True    True        False       True
#True   False   False       True        True
#False  True    False       False       False
#False  False   False       True        True


#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
#If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
sensor_threshold = int(input("On a scale of 1-10, what is the daylight level?"))
if sensor_threshold >= 8:
    print("Headlights OFF")
else:
    print("Headlights ON")


#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. 
#Print True if the user’s balance is below $100; print False, otherwise.
bank_balance = int(input("Let's see if your savings are less than $100. What is your bank account balance? "))
if bank_balance < 100:
    print("True")
else:
    print("False")




#4. A theater wants to enforce age restrictions for movie tickets.
#Ask the user for their age, and tell them whether they can see G (appropriate for under 13),
#PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
age = int(input("What is your age? "))
if age >= 18:
    print("You can see G, PG-13, and R rated movies.")
elif age >= 13:
    print("You can watch G and PG-13 rated movies.")
else:
    print("You can see G rated movies.")



#5. A store charges $5 for shipping on any order under $50. 
#If the order amount is $50 or more, shipping is free. 
#Ask the user for the order total and print the total cost, including shipping.
print("There is a $5 charge for orders under $50. For orders over $50, shipping is free!")
order_total = int(input("What is your order total? "))
if order_total >= 50:
    print("Congratulations! You are eligible for free shipping.")
else:
    total_cost = order_total + 5
    print("A $5 shipping fee has been added to your total.")
    print("Your total is", total_cost)

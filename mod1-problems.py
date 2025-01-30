# 1. Create a program that prints the following output to the screen:
# "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony.
# Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")



# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication,
#and division of the first number by the second number.
import math
print("Hello!")
x = int(input("Please give x a value!"))

y = int(input("Awesome! Now please give y a value and watch magic happen!"))

print(x+y)
print(x-y)
print(x*y)
print(x/y)



# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula.
#(https://en.wikipedia.org/wiki/Heron%27s_formula)
print("This program will solve equations involving Heron's formula!")
s = int(input("Please give 's' a value."))
a = int(input("Please give 'a' a value."))
b = int(input("Please give 'b' a value."))
c = int(input("Please give 'c' a value."))

import math
val1 = (((s)-(a))*((s)-(b))*((s)-(c)))
val2 = (((s)*(val1)))
answer = (math.sqrt(val2))
print(answer)


# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation
#(https://en.wikipedia.org/wiki/Standard_deviation).
print("This program will create different statistics based off five numbers you give!")
num1 = int(input("Please give us the first number."))
num2 = int(input("Please give us the second number."))
num3 = int(input("Please give us the third number."))
num4 = int(input("Please give us the fourth number."))
num5 = int(input("Please give us the fifth number."))
print(num1, num2, num3, num4, num5)

import math

minimum = (min(num1, num2, num3, num4, num5))
maximum = (max(num1, num2, num3, num4, num5))

range = ((maximum) - (minimum))
total = ((num1)+(num2)+(num3)+(num4)+(num5))
average = ((total)/5)

dev1 = ((((num1)-5)**2)+(((num2)-5)**2)+(((num3)-5)**2)+(((num4)-5)**2)+(((num5)-5)**2))
deviation = (math.sqrt(dev1))

print("The total is", total)
print("The average is", average)
print("The minimum is", minimum)
print("the maximum is", maximum)
print("the range is", range)

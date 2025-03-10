#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Please give a positive integer! "))
count = 0
while count < n: #need to start from 0 to given number, how do i do that?
    print(count+1)
    count += 1
print("The final sum is", n)


#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.
my_string = "Coding Rules"
for char in my_string:
    print(char)

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
for i in range(2, 21):
    if i % 2 == 0:
        print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5.
#Format your output so that each row corresponds to multiplying by a specific number. 
#ex.
#   1   2   3   4   5
#   2   4   6   8   10
#   3   6   9   12  15
#   4   8   12  16  20
#   5   10  15  20  25

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


#5. Write a program that continuously asks the user to input a number. 
#If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.
#EX.
#ENTER A NUMBER (0 TO STOP): 4
#YOU ENTERED 4
#ENTER A NUMBER (0 TO STOP): 7
#YOU ENTERED 7
#ENTER A NUMBER (0 TO STOP): 0
#EXITING


while True:
    number = int(input("Please enter a number! (0 to STOP) "))
    if number == 0:
        print("Exiting")
        break
    print("You entered", number)

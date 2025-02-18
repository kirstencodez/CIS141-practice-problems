## 1. Prompt the user for a word.
#Then, prompt the user for how many times they'd like that word repeated.
#Use the skills you learned in this module to print the word the correct number of times.

word = (input("Give us a word!"))
repeat = int(input("How many times would you like it repeated?"))
print(word*repeat)

#2. Prompt the user for their name and their age.
Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old.
Next year, you will be <age2> years old."

#name = input("What's your name?")
age = int(input("How old are you?"))
age2 = age + 1
greeting = "Hello " + name + "!" + " You are " + str(age) + " years old." + " Next year, you will be " + str(age2) + " years old."
print(greeting)


#3. Prompt the user for a sentence and a word to try to find in that sentence.
#Have the program print out whether the word was found in the sentence. (i.e. True or False)
sentence = input("Please type in a sentence.")
word = input("What word do you want to find in that sentence?")
is_word_found = word in sentence
print(is_word_found)

#4. Prompt the user for: a word, a first index, and a last index.
#Slice the word at the indexes provided by the user and print to the screen.
word = input("Please give us a word!")
first_index = int(input("Now please give us a first index."))
last_index = int(input("Lastly, please give us a last index."))
word_slice = word[first_index:last_index]
print("The sliced word is:" , word_slice)


#5. Print 3 words with a | character (called a pipe) in between them.
#Use the appropriate keyword argument in print() to do so.
word_1 = input("We are going to ask you for three words. Please give the first word.")
word_2 = input("Please give a second word.")
word_3 = input("Please give us the last word.")
words = (word_1, word_2, word_3)

together = "|".join(words)
print(together)

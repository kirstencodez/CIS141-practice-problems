"""
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
"""

# file = open("gardening_tips.txt", "r")
# contents = file.read()
# print(contents)


"""
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
"""
"""
with open("hiking_log.txt", "a") as file:
    while True: 
        hike_name = str(input("Where did you hike? Press 0 to EXIT. "))
        if hike_name == "0":
            break
        distance = str(input("How many miles was your hike? Press 0 to EXIT. "))
        if distance == "0":
           break   
        file.write(hike_name + "\t" + distance + "miles\n")
print("\nHere is your hike log:")
with open("hiking_log.txt", "r") as file:
    print(file.read())
    


"""
"""
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
"""
"""
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()
    
word_counts = {}    
words_input = input("Give 5 words you would like to count the frequency of: ")
words = words_input.lower().split()

while len(words) != 5:
    print("Please enter EXACTLY 5 words!")
    words_input = input("Give 5 words you would like to count the frequency of: ")
    words = words_input.lower().split()


words = words_input.lower().split()
for word in words:
    count = lyrics.split().count(word)
    word_counts[word] = count
    
    
print("\nWord Frequency Dictionary:")
for word, count in word_counts.items():
        print(f"{word}: {count}")

"""
"""
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.

"""
"""

with open("poll.txt", "r") as file:
    contents = file.read()
    yea_count = 0
    nay_count = 0
    words = contents.split()

for word in words:
    word = word.lower()
    if word == "yea":
        yea_count += 1
    elif word == "nay":
        nay_count += 1
print("There are ", yea_count, "votes for yea and ", nay_count, "votes for nay.")
"""

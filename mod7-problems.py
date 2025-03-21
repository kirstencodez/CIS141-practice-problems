'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
    

'''
#user_input = input("Please type out a string! ")
#vowel = ["a", "e", "i", "o", "u"]

#def count_vowels(input_string):
#    vowels = 0
#    for char in input_string:
#        if char.lower() in vowel:
#            vowels += 1
#    return f"There are {vowels} vowel(s)"
#result = count_vowels(user_input)
#print(result)

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
    Test: tacocat (True), grape (False), Madam (True)
    Input: string (s)
    Output: boolean
    Function body: lowercase s, flip s and save to new variable (flipped s), and then compare s flipped & flipped s
    
'''
#def is_palindrome(s):
#    lower_s = s.lower()
#    flipped_s = lower_s[::-1]
#    return lower_s == flipped_s

#print(is_palindrome("madam"))
#print(is_palindrome("grape"))
#print(is_palindrome("tacocat"))
    
#is_palindrome("Madam")

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
#def type_advantage(attacker, defender):
#    if attacker == "Water" and defender == "Fire":
#        return "Super Effective"
#    elif attacker == "Fire" and defender == "Water":
#        return "Not Very Effective"
#    elif attacker == "Electric" and defender == "Grass":
#        return "Neutral"
#print(type_advantage("Water", "Fire"))  
#print(type_advantage("Fire", "Water"))  
#print(type_advantage("Electric", "Grass")) 
    
'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
#age = int(input("How old are you? "))
#vehicle_input = input("If boarding with vehicle, type True. If not boarding with vehicle, type False. ")
#vehicle = vehicle_input.lower() == "true"

#def ferry_fare(age, vehicle):
#    if age >= 19 and vehicle:
#        return "$20"
#    elif age >= 19 and not vehicle:
#        return "$10"
#    if age >= 65 and vehicle:
#        return "$20"
#    elif age >= 65 and not vehicle:
#        return "$10"
#    elif age <= 18:
#        return "Free"

#print(ferry_fare(age, vehicle))


'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''

#experience = int(input("What is your total number of points? "))

#def level_up(experience):
#    if experience <= 99:
#        return "Great Job! You are on Level 1"
#    elif experience <= 199:
#        return "Congratulations, you are on Level 2!"
#    elif experience >= 200:
#        return "Amazing! You have reached Level 3!"
    
#print(level_up(experience))

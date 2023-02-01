# Random
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# String
# https://www.askpython.com/python/string/convert-string-to-list-in-python
# bez upotrebe funkcije choice()

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)

velicinaPolja = len(names)-1 # vazno je oduzeti s jedan jer [0 ... n-1]
randBroj = random.randint(0, velicinaPolja)

ime = names[randBroj]

print(f"{ime} is going to buy the meal today!")

# --------------------------------------------------------
# Funkcija choice()
# osobaPlaca = random.choice(names)
# print(osobaPlaca + " is going to buy the meal today!")
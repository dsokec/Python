# bez upotrebe funkcije choice()

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)

velicinaPolja = len(names)
randBroj = random.randint(0, velicinaPolja)

ime = names[randBroj]

print(f"{ime} is going to buy the meal today!")
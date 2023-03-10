################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Local scope

# def drinkPotion():
#   potionStrength = 20
#   print(potionStrength)

# drinkPotion()

# Error
# print(potionStrength)

# # Global scope

# playerHealth = 20
# def game():
#   def drinkPotion():
#     potionStrength = 5
#     print(playerHealth)

#   drinkPotion()

# # Error
# # drinkPotion()
# print(playerHealth)
# # Error
# # print(potionStrength)

# game()

# There is no block scope

# gameLevel = 3

# def createEnemy():
#   enemies = ["zombie", "dinosaur", "skeleton"]

#   if gameLevel < 5:
#     newEnemy = enemies[1]
  
#   print(newEnemy)

# createEnemy()

# # Modify global variable

# enemies = 1

# def increaseEnemies():
#   # ovo nije u redu jer utjece direktno na glob varijablu
#   # global enemies
#   # enemies += 2

#   # Ovaj način je puno ispravniji
#   print(f"Enemies inside the function {enemies}")
#   return enemies + 1

# numOfEnemies = increaseEnemies()
# print(f"Enemies outside of function {numOfEnemies}")

# Global constants
# These are always UPPERCASE

PI = 3.14
URL = "https://www.google.com"
FACEBOOK = "https://www.facebook.com/dino.sokec"

def calc():
  PI
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

# Global scope

playerHealth = 20
def game():
  def drinkPotion():
    potionStrength = 5
    print(playerHealth)

  drinkPotion()

# Error
# drinkPotion()
print(playerHealth)
# Error
# print(potionStrength)

game()
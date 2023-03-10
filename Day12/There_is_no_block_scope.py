# There is no block scope

gameLevel = 3

def createEnemy():
  enemies = ["zombie", "dinosaur", "skeleton"]

  if gameLevel < 5:
    newEnemy = enemies[1]
  
  print(newEnemy)

createEnemy()
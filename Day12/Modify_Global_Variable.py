# Modify global variable

enemies = 1

def increaseEnemies():
  # ovo nije u redu jer utjece direktno na glob varijablu
  # global enemies
  # enemies += 2

  # Ovaj način je puno ispravniji
  print(f"Enemies inside the function {enemies}")
  return enemies + 1

numOfEnemies = increaseEnemies()
print(f"Enemies outside of function {numOfEnemies}")
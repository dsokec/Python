# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random
# napravi se nova datoteka
# import myModule

randomInteger = random.randint(1, 10)

print(randomInteger)

# randomFloat = random.uniform(1,5)
randomFloat = random.random() * 5
print(randomFloat)

# potrebno je ako samo koristiš .random()
# randomFloat * 5

# Love Calculator
loveScore = random.randint(1, 100)
print(f"Your love score is {loveScore}")


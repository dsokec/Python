from art import logo, vs
from game_data import data
import random

# 3. Format the account data into printable format

def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  
  return f"{account_name}, a {account_descr}, from {account_country}"

# 1. Display art
print(logo)

# 2. Generate a random account name from the list
account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
  account_b = random.choice(data)

# 3. Format the account data into printable format
print(f"Compare A: {format_data(account_a)}")
print(vs)
print(f"Compare B: {format_data(account_b)}")
  
# 4. Ask user for a guess

# 5. Check if user is correct
## 5.1. Get follower count of each account
## 5.2. Use if statement to check if user is correct

# 6. Give user feedbac on their guess

# 7. Score keeping.abs

# 8. Make the game repeatable.

# 9. Making account at position B become the next account at position A

# 10. Clear the screen between rounds.



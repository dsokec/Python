from art import logo, vs
from game_data import data
import random
from replit import clear

# 3. Format the account data into printable format

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  
  return f"{account_name}, a {account_descr}, from {account_country}"

## 5.2. Use if statement to check if user is correct
def check_answer(guess, a_followers, b_followers):
  """Take the user guess and followers counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# 1. Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# 8. Make the game repeatable.
while game_should_continue:
  # 2. Generate a random account name from the list
  # 9. Making account at position B become the next account at position A
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  # 3. Format the account data into printable format
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
    
  # 4. Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # 5. Check if user is correct
  ## 5.1. Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # 10. Clear the screen between rounds.
  clear()
  print(logo)
  
  # 6. Give user feedback on their guess
  # 7. Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
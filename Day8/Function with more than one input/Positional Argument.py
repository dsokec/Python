# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Functions with more than one input
def greetWith(name, location):
  # Hello -name-
  # What is it like in -location-
  print(f"Hello {name}.")
  print(f"What is it like in {location} ?")

greetWith("John", "Đurđevac")

# pazi na poredak argumenata
# Positional Argument
greetWith("Đurđevac", "John")
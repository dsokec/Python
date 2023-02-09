def formatName(firstName, lastName):
  # Docstrings - čitanje teksta prelazi se iz reda u red
  # Pogledaj si art.py - ASCII art i navodnike
  """Take a first and last name and format it 
  to return the title case version of the name. """
  
  if firstName == "" or lastName == "":
    return "You didn't provide valid inputs."
  firstName = firstName.title()
  lastName = lastName.title()
  # print(firstName + " " + lastName)
  # print(f"{firstName} {lastName}")
  return f"{firstName} {lastName}"

outputString = formatName(input("What is your first name? "), input("What is your last name? "))
print(outputString)

# ctrl + shift + / - za komentare
# fdsafdfa
# dfafdsaf
# dfdfsadf
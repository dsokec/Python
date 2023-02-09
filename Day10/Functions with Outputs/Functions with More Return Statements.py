def formatName(firstName, lastName):
  if firstName == "" or lastName == "":
    return "You didn't provide valid inputs."
  firstName = firstName.title()
  lastName = lastName.title()
  # print(firstName + " " + lastName)
  # print(f"{firstName} {lastName}")
  return f"{firstName} {lastName}"

outputString = formatName(input("What is your first name? "), input("What is your last name? "))
print(outputString)
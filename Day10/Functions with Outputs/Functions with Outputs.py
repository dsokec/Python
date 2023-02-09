def formatName(firstName, lastName):
  firstName = firstName.title()
  lastName = lastName.title()
  # print(firstName + " " + lastName)
  # print(f"{firstName} {lastName}")
  return f"{firstName} {lastName}"

outputString = formatName(firstName = "diNO", lastName = "sOKEc")
print(outputString)
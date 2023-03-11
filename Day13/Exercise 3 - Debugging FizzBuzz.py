# Error - ispisuje dvije grane bez ikakve potrebe
# for number in range(1, 101):
  # if number % 3 == 0 or number % 5 == 0: # treba ici and, a ne or
    # print("FizzBuzz")
  # if number % 3 == 0: # ispisuje Fizz pa potom broj 3
    # print("Fizz")
  # if number % 5 == 0:
    # print("Buzz")
  # else:
    # print(number)


for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
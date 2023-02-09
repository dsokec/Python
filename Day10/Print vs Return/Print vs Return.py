# Calculator
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# -----------
# Dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What is the first number?: "))

for symbol in operations:
  print(symbol)
operationSymbol = input("Pick an operation from the line above: ")

num2 = int(input("What is the second number?: "))

# A hold function
# https://pythontutor.com/visualize.html#mode=edit
calculationFunction = operations[operationSymbol]
Firstanswer = calculationFunction(num1, num2)

print(f"{num1} {operationSymbol} {num2} = {Firstanswer}")

operationSymbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculationFunction = operations[operationSymbol]
secondAnswer = calculationFunction(calculationFunction(num1, num2), num3)

print(f"{Firstanswer} {operationSymbol} {num3} = {secondAnswer}")

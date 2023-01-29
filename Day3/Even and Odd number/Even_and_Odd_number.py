# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

provjera = number % 2
evenNumber = f"This number {number} is an even number"
oddNumber = "This number {number} is an odd number"

if(provjera == 0):
    print(evenNumber)
else:
    print(oddNumber)

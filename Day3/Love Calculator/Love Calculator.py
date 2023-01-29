# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combinedString = name1 + name2
lowerCaseString = combinedString.lower()

t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")

true = t + r + u + e

l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")

love = l + o + v + e

trueLove = int(str(true) + str(love))
# intScore = int(trueLove)

score = f"Your score is {trueLove}"
cokeMenta = ", you go together like coke and mentos."
together = ", you are alright together."
otherwise = f"Your score is {trueLove}."

if trueLove < 10 or trueLove > 90:
    print(score + cokeMenta)
elif trueLove >= 40 and trueLove <= 50:
    print(score + together)
else:
    print(otherwise)
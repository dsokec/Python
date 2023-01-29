# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

# Size S
if(size == "S" or size == "s"):
    bill += 15

# Size M
elif(size == "M" or size == "m"):
    bill += 20

# Size L
else:
    bill += 25

if(add_pepperoni == "y" or add_pepperoni == "Y"):
    if(size == "S" or size == "s"):
        bill += 2
    else:
        bill += 3

if(extra_cheese == "y" or extra_cheese == "Y"):
    bill += 1


# Final bill
finalBill = f"Your final bill is ${bill}"

print(finalBill)
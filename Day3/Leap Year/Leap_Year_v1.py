# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leapYear = "Leap year."
notLeapYear = "Not leap year."

saCetiri = year % 4
saSto = year % 100
saCetiriSto = year % 400

if(saCetiri == 0):
    if(saSto == 0):
        if(saCetiriSto == 0):
            print(leapYear)
        else:
            print(notLeapYear)
    else:
        print(leapYear)
else:
    print(notLeapYear)
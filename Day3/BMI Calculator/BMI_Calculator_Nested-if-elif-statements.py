# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_float = weight / (height ** 2)

bmi = int(round(bmi_float, 0))

message = f"Your BMI is {bmi},"

underweight = " you are underweight."
normal = " you have a normal weight."
overweight = " you are slightly overweight."
obese = " you are obese."
clinicallyObese = " you are clinically obese."

if(bmi < 18.5):
    print(message + underweight)
elif(bmi > 18.5 and bmi < 25):
    print(message + normal)
elif(bmi > 25 and bmi < 30):
    print(message + overweight)
elif(bmi > 30 and bmi < 35):
    print(message + obese)
else:
    print(message + clinicallyObese)
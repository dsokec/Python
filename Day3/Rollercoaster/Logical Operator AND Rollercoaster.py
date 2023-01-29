print("Welcome to the rollercoaster!")
height = int(input("\nWhat is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("\nWhat is your age? "))
    if age < 12:
      # bill = 5
      bill += 5
      print("Child tickets are $5.")
    elif age <= 18:
      # bill = 7
      bill += 7
      print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
      # bill = 0 ili bez toga retka
      bill += 0
      print("Tickets are $0")
    else:
      # bill = 12
      bill += 12
      print("Adult tickets are $12.")
    

    wantPhoto = input("\nDo you want a photo taken? Y or N. ")
    if (wantPhoto == "Y") or (wantPhoto == "y"):
      # ovdje treba +=
      bill += 3
    
    # Nema potrebe za else statement
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

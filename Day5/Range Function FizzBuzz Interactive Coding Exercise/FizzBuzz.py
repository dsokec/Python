#Write your code below this row 👇

for number in range (1, 101):
    # Ovo mora ici na vrh petlje for
    # Vrlo zahtjevan if statement se mora prvo izvrsiti
    if number % 3 == 0 and number % 5 == 0:
        # Divisible by 3 and 5
        print("FizzBuzz")

    elif number % 3 == 0:
        # Divisible by 3
        print("Fizz")

    elif number % 5 == 0:
        # Divisible by 5
        print("Buzz")

    else:
        print(number)
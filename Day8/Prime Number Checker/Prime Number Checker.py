#Write your code below this line 👇

# je li broj prost ?
def prime_checker(number):
    isPrime = True
    # raspon je od 2 do number-1
    for x in range(2, number):
        if number % x == 0:
            isPrime = False
    if isPrime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

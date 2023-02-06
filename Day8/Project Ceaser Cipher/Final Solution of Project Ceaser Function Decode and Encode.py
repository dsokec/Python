alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# Funkcija Ceaser
def ceaser(startText, shiftAmount, cipherDirection):
  endText = ""
  # Mora ići van u protivnom
  # shiftAmount će biti negativan, pozitivan, negativan, pozitivan, ...
  if cipherDirection == "decode":
      shiftAmount *= -1
    
  for char in startText:
    # provjera je li znak zapravo u abecedi
    if char in alphabet:
      position = alphabet.index(char)
      newPosition = (position + shiftAmount) % 26
      endText += alphabet[newPosition]
    # ako nije znak u abecedi tada se ispisuje tekst koji se upisao na početku
    else:
      endText += char
  print(f"The {cipherDirection}d text is {endText}")
# --------------------------------------------------

from replit import clear
from art import logo

shouldContinue = True
while shouldContinue:
  clear()
  print(logo)

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() 
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # shift = shift % 26
  # tada se briše 26 u retku 'newPosition = (position + shiftAmount) % 26'
  
  # Calling the ceaser function
  ceaser(startText = text, shiftAmount = shift, cipherDirection = direction)

  result = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if result == "no":
    shouldContinue = False
    print("\nGoodbye !")
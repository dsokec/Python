alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt the message
def encrypt(plainText, shiftAmount):
  cipherText = ""
  for letter in plainText:
    position = alphabet.index(letter)
    # newPosition = (position + shiftAmount)%len(alphabet)
    newPosition = (position + shiftAmount)%26
    newLetter = alphabet[newPosition]
    cipherText += newLetter
  print(f"The encoded text is {cipherText}")
  
# Decrypt the message
def decrypt(plainText, shiftAmount):
  cipherText = ""
  for letter in plainText:
    position = alphabet.index(letter)
    newPosition = (position - shiftAmount)%26
    newLetter = alphabet[newPosition]
    cipherText += newLetter
  print(f"Decrypted message is {cipherText}")

if direction == "encode":
    encrypt(plainText = text, shiftAmount = shift)
elif direction == "decode":
    decrypt(plainText = text, shiftAmount = shift)
# nije potrebna else grana
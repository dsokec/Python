# https://getemoji.com/

# 🚨 Don't change the code below 👇
# Emoji
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# e.g '23'
horizontal = int(position[0]) # 2
vertical = int(position[1]) # 3

selectedRow = map[vertical-1]
selectedRow[horizontal-1] = "X"

# jednostavniji pristup
#map[vertical-1][horizontal-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


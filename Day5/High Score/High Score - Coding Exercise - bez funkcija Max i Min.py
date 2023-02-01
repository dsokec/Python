# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# bez upotrebe funkcija Max i Min



# druga opcija je:
# minScore = 0

# minScore = student_scores[0]

# ovo je najbolja solucija:
# maxScore = 0
maxScore = student_scores[0]
for score in student_scores:
    if maxScore < score:
        maxScore = score
    # Grana za Minimum Score
    # if minScore > score:
        # minScore = score

print(f"The highest score in the class is: {maxScore}")

# Min Score
# print(f"The lowest score in the class is: {minScore}")




# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

totalHeights = sum(student_heights)
numberOfStudents = len(student_heights)
# averageHeight = round((totalHeights / numberOfStudents),0)
averageHeight = round(totalHeights / numberOfStudents)

print(averageHeight)



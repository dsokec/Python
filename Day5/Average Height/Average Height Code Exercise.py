# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

brojacStudenata = 0
for brojStudenata in student_heights:
    brojacStudenata += 1

sumaVisina = 0
for visinaStudenta in student_heights:
    sumaVisina += visinaStudenta

averageHeightFloat = sumaVisina / brojacStudenata

averageHeightInt = int(round(averageHeightFloat, 0))

print(averageHeightInt)



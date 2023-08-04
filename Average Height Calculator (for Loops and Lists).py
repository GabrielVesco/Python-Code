# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#replicating the sum and len function
cumulative_height = 0
counter = 0
for height in student_heights:
    cumulative_height += height
    counter += 1


#now we have the height totals and number of students
average_height = round(cumulative_height / counter)
print(average_height)
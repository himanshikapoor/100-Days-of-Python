# Program to print sum of even no.s from 1-100
#Write your code below this row 👇
sum = 0
for number in range(1, 101):
  if number % 2 == 0:
    sum += number

print(sum)
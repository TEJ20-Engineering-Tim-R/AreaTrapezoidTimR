# Created by: Tim R
# Date: 01/04/2021
# this program will ask for the values of side A, side B and the height and will then calculate the area. It will then display the value of the area to the user.

print("Today we will calculate the area of a trapezoid.")
sideA = int(input("Enter the value of side A: "))
sideB = int(input("Enter the value of side B: "))
height = int(input("Enter the value of the height: "))
area = ((sideA + sideB) / 2) * height
print("The area of a trapezoid with a side A of ", sideA, "cm, a side B of ", sideB, "cm and a height of ", height, "cm is ", area, "cm squared.")

 #Exercises - Day 3

 #1. Declare your age as integer variable
#2. Declare your height as a float variable
#3. Declare a variable that store a complex number

age = 20
height = 164.8
z = 5+6j



#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = int (input('enter base: '))
height = int (input('enter height: '))

area = 0.5*base*height

print ('the area= ' , area) 




#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = int (input('enter side a of tringle: '))
side_b = int (input('enter side b of tringle: '))
side_c = int (input('enter side c of tringle: '))

perimeter = side_a + side_b + side_c

print ('perimeter is: ' , perimeter)




#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int (input('enter length: '))
width = int (input('enter width: '))

area = length * width 
perimeter = 2 * (length + width)

print ('area of tringle is : ' , area)
print ('perimeter of tringle is : ' , perimeter)





#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = int (input('enter radius of circle: '))

area = 3.14*(radius**2)
circumference = 2*3.14*radius

print ('area of circle= ' , area)
print ('circumference of circle= ' , circumference)




#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope1 = 2
y_intercept = -2
x_intercept = -y_intercept/slope1




#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10).

X1, y1 = 2, 2
x2, y2 = 6; 10

slope2 = (y2-y1)/(x2-x1)
distance = (((x2-x1)**2) + ((y2-y1)**2))**0.5



#10. Compare the slopes in tasks 8 and 9.

print("slopes are equal", slope1==slope2)



#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = -3
y = (x**2)+6*x+9


print ("x =", x)
print ("y =", y)



#12.Find the length of 'python' and 'dragon' and make a falsy comparison statement.

python = len('python')
dragon = len('dragon')

python != dragon



#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'.

print ('on' in 'python' and 'on' in 'dragon')


#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print ('jargon' in 'I hope this course is not full of jargon')


#15. There is no 'on' in both dragon and python.

print ('on' not in 'python' and 'on' not in 'dragon')


#16. Find the length of the text python and convert the value to float and convert it to string.

length = len ('python')

float (length)
str (length)


#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

even_number = 6

print (even_number % 2 == 0)


#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

division = 7//3
convert = int (2.7) 

print (division == convert)


#19. Check if type of '10' is equal to type of 10

firsttype = type ('10')
seconedtype = type (10)

print (firsttype == seconedtype)



#20. Check if int('9.8') is equal to 10

first = int ('9.8')
seconed = 10

print (first == seconed )


#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int (input('enter hours: '))
rate = int (input('enter rate: '))

pay = hours*rate
print ('pay of the person= ' , pay)



#22. Write a script that prompts the user to enter number of years.Calculate the number of seconds a person can live. Assume a person can live hundred years.

years = int (input('enter number of years: '))

seconds = years*365*24*60*60
print ('Number of seconds: ', seconds)



#23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print (1, 1, 1,  1,   1)
print (2, 1, 2,  4,   8)
print (3, 1, 3,  9,  27)
print (4, 1, 4, 16,  64)
print (5, 1, 5, 25, 125)

















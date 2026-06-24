"""
-level 1-

Q1: 
1.Declare a first name variable and assign a value to it
2.Declare a last name variable and assign a value to it
3.Declare a full name variable and assign a value to it
4.Declare a country variable and assign a value to it
5.Declare a city variable and assign a value to it
6.Declare an age variable and assign a value to it
7.Declare a year variable and assign a value to it
8.Declare a variable is_married and assign a value to it
9.Declare a variable is_true and assign a value to it
10.Declare a variable is_light_on and assign a value to it
11.Declare multiple variable on one line

"""

first_name = 'waad'
last_name = 'daraghmeh'
full_name = 'waad daraghmeh'
country = 'palestine'
city = 'tubas'
age = 20
year = 2006
is_marrid = False
is_true = True
is_light_on = True
x, y, z = 4, 6, 8



"""
-level 2-

Q2: 
1.Check the data type of all your variables using type() built-in function
2.Using the len() built-in function, find the length of your first name
3.Compare the length of your first name and your last name
4.Declare 5 as num_one and 4 as num_two
5.Add num_one and num_two and assign the value to a variable total
6.Subtract num_two from num_one and assign the value to a variable diff
7.Multiply num_two and num_one and assign the value to a variable product
8.Divide num_one by num_two and assign the value to a variable division
9.Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
10.Calculate num_one to the power of num_two and assign the value to a variable exp
11.Find floor division of num_one by num_two and assign the value to a variable floor_division
12.The radius of a circle is 30 meters.
   i.Calculate the area of a circle and assign the value to a variable name of area_of_circle
   ii.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
   iii.Take radius as user input and calculate the area.
13.Use the built-in input function to get first name, last name, country and age 
from a user and store the value to their corresponding variable names
14.Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

type (first_name)
type (last_name)
type (full_name)
type (country)
type (city)
type (age)
type (year)
type (is_marrid)
type (is_light_on)
type (x, y, z)


len (first_name)
len (first_name) > len (last_name)


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two 
product = num_one * num_two
division = num_one / num_two 
remainder = num_two % num_one 
exp = num_one ** num_two
floor_division = num_one // num_two


R = 30
area_of_circle = 3.14 * (R ** 2)
circum_of_circle = 2 * 3.14 * R
R = int (input("Enter radius: "))
print ("area: " 3.14 * (R ** 2))



first_name = input ("Enter your first name:  ")
last_name = input ("Enter your last name:  ")
country = input ("Enter your country:  ") 
age = input ("Enter your age:  ")
print (first_name, last_name, country, age)


help('keywords')

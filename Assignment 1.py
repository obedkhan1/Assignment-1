#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of
service and print the net bonus amount.


# In[ ]:


salary = float(input("Enter your salary: "))

years_of_service = int(input("Enter your years of service: "))


if years_of_service > 5:
    bonus_amount = 0.05 * salary
    print("Congratulations! You are eligible for a bonus of 5%.")
    print("Net bonus amount: Rs", bonus_amount)
else:
    print("Sorry, you are not eligible for a bonus at this time.")


# In[ ]:


Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not
eligible


# In[ ]:


age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")


# In[ ]:





# In[ ]:


Write a program to check whether a number entered by user is even or odd.


# In[ ]:


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# In[ ]:





# In[ ]:


Write a program to check whether a number is divisible by 7 or not. Show Answer


# In[ ]:


number = int(input("Enter a number: "))

if number % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")


# In[ ]:





# In[ ]:


Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".


# In[ ]:


number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Hello")
else:
    print("Bye")


# In[ ]:





# In[ ]:


Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is
Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750


# In[ ]:


This program calculates the electricity bill based on the following criteria:

- Up to 100 units, there's no charge.
- For the next 200 units (101 to 300), the charge is Rs 5 per unit.
- Beyond 300 units, the charge is Rs 10 per unit.

We take input from the user for the number of units consumed, then calculate the total bill amount according to 
these criteria, and finally print out the total bill amount.


# In[ ]:


units = int(input("Enter the number of units: "))

total_bill = 0

if units <= 100:
    total_bill = 0
elif units <= 300:
    total_bill = (units - 100) * 5
elif units > 300:
    total_bill = (200 * 5) + ((units - 300) * 10)

print("Total bill amount is Rs.", total_bill)


# In[ ]:





# In[ ]:


Write a program to display the last digit of a number.


# In[ ]:


number = int(input("Enter a number: "))
last_digit = number % 10
print("The last digit of the number is:", last_digit)


# In[ ]:





# In[ ]:


Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.


# In[ ]:


number = int(input("Enter a number: "))
last_digit = number % 10

if last_digit % 3 == 0:
    print("The last digit of the number is divisible by 3.")
else:
    print("The last digit of the number is not divisible by 3.")


# In[ ]:





# In[ ]:


Take values of length and breadth of a rectangle from user and print if it is square or rectangle.


# In[ ]:


length = float(input("3: "))
breadth = float(input("2: "))

if length == breadth:
    print("It is a square.")
else:
    print("It is a rectangle.")


# In[ ]:





# In[ ]:


Take two int values from user and print greatest among them.


# In[ ]:


num1 = int(input("30: "))
num2 = int(input("50: "))

if num1 > num2:
    print("The greatest number is:", num1)
elif num2 > num1:
    print("The greatest number is:", num2)
else:
    print("Both numbers are equal.")


# In[ ]:





# In[ ]:


A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100.
Judge and print total cost for user.


# In[ ]:


quantity = int(input("Enter the quantity of items purchased: "))

unit_cost = 100
total_cost = quantity * unit_cost

if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount

print("Total cost for the user:", total_cost)


# In[ ]:





# In[ ]:


A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.


# In[ ]:


marks = float(input("Enter your marks: "))

if marks < 25:
    grade = "F"
elif marks >= 25 and marks < 45:
    grade = "E"
elif marks >= 45 and marks < 50:
    grade = "D"
elif marks >= 50 and marks < 60:
    grade = "C"
elif marks >= 60 and marks < 80:
    grade = "B"
else:
    grade = "A"

print("Your grade is:", grade)


# In[ ]:





# In[ ]:


Take input of age of 3 people by user and determine oldest and youngest among them.


# In[ ]:


ages = []

for i in range(3):
    age = int(input(f"Enter age of person {i+1}: "))
    ages.append(age)

oldest_age = max(ages)
youngest_age = min(ages)

print(f"The oldest person is {oldest_age} years old.")
print(f"The youngest person is {youngest_age} years old.")


# In[ ]:





# In[ ]:


A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.


# In[ ]:


classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

if attendance_percentage >= 75:
    print("Percentage of classes attended:", attendance_percentage)
    print("The student is allowed to sit in the exam.")
else:
    print("Percentage of classes attended:", attendance_percentage)
    print("The student is not allowed to sit in the exam due to low attendance.")


# In[ ]:





# In[ ]:


Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and
print accordingly.


# In[ ]:


classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

medical_cause = input("Do you have a medical cause? (Y/N): ")

if attendance_percentage >= 75 or medical_cause.upper() == 'Y':
    print("Percentage of classes attended:", attendance_percentage)
    print("The student is allowed to sit in the exam.")
else:
    print("Percentage of classes attended:", attendance_percentage)
    print("The student is not allowed to sit in the exam due to low attendance.")


# In[ ]:





# In[ ]:


Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.


# In[ ]:


- We take input from the user for the year.
- We then use conditional statements to check if the given year is a leap year.
According to the conditions provided:
- If the year is divisible by 4 but not divisible by 100, or if the year is divisible by 400, then it is a leap year.
- Otherwise, it is not a leap year.
- Finally, the program prints whether the given year is a leap year or not.


# In[ ]:


year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.") 


# In[ ]:





# In[ ]:


Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR


# In[ ]:


- We prompt the user to enter their age, gender, and marital status.
- Based on the provided rules, we check the place of service:
  - If the gender is female, the place of service is urban areas.
  - If the gender is male and the age is between 20 to 40, the place of service is anywhere.
  - If the gender is male and the age is between 40 to 60, the place of service is urban areas.
  - If any other input of age is provided, it prints "ERROR".
- Finally, the program prints the place of service accordingly.


# In[ ]:


age = int(input("Enter age: "))
gender = input("Enter gender (M or F): ")
marital_status = input("Enter marital status (Y or N): ")

if gender.upper() == 'F':
    print("Place of service: Urban areas")
elif gender.upper() == 'M':
    if 20 <= age <= 40:
        print("Place of service: Anywhere")
    elif 40 <= age <= 60:
        print("Place of service: Urban areas")
    else:
        print("ERROR")
else:
    print("ERROR")


# In[ ]:





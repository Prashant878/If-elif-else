#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question:create a python program that asks thye user for a month (1-12) and then print the corresponding season("spring","summer", fall","winter")? )
month = int(input("Enter a month (1-12): "))

# Determine the season
if month in [3, 4, 5]:
    season = "spring"
elif month in [6, 7, 8]:
    season = "summer"
elif month in [9, 10, 11]:
    season = "fall"
else:
    season = "winter"

# Print the corresponding season
print(f"The season for month {month} is {season}.")


# In[3]:


#question:write a python program that determines weather a given year is a leap year or not. 
year=int(input("Write the year:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")


# In[6]:


# question: write a python program that asks the user for their age and gender. Based on their age and gender print "you are a young man" or "you are a old woman".
age=int(input("what is your age:"))
gender=input("what is your gender(Male/Female):")
if age<=30 and gender=="male":
    print("You are a young man")
elif age>30 and gender=="male":
    print("You are a old man")
elif age<=30 and gender=="female":
    print("you are a young female")
elif age>30 and gender=="female":
    print("you are a old female")
else:
    print("Age entered is invalid")


# In[11]:


#create a python program that takes an integer as input and checks if it's positive, negative, or zero, print an  appropriate message.
num=int(input("please enter a number here"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


# In[7]:


#question 
#Age classification 
user_1=int(input("What is your age:"))

if user_1<=12:
    print("Child")
elif (user_1>=13) and (user_1<=19):
    print("Teenager")
else:
    print("Adult")


# In[8]:


#question 3
score=int(input("Please enter your score:"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("c")
elif score>=60:
    print("D")
else:
    print:("F")


# In[10]:


#create a pythone program takes a temprature in celsius and converts it to Farenheit. Display the result with an appropriate message. 
temprature= float(input("please enter the tempratrature in celsius:"))
fahrenheit=(temprature *1.8)+32
print("temprature celsius to fahrenheit conversion in fahrenheit is:", fahrenheit)


# In[13]:


#write a python program that calculates the shipping cost based on the weight of a package. Use the following rules:
#weight<=2 pounds:$5.00-2 pounds<weight<=10 pounds:$10.00
#weight>10 pounds:$15.00
package_1=float(input("Please enter the package weight in pounds:"))
weight=package_1 
if weight<=2:
    print("the shiiping cost will be $5")
elif weight>10:
    print("the shippng cose will be $15")
else:
    print("the shipping cose will be $10")


# In[14]:


#create a python program that asks the users for three numbers and then prints in ascending order.
numb_1=int(input("Please enter a number:"))
numb_2=int(input("please enter a number:"))
numb_3=int(input("please enter a number:"))
sortedNumbers=sorted([numb_1,numb_2,numb_3])
print("Numbers in asceneding orders are:",sortedNumbers)


# In[15]:


#create a python programs that asks the user for a number and then determines if it's even or odd. 
number=int(input("please enter a number:"))
if number%2==0:
    print("the entered number is even number")
else:
    print("the entered number is odd number")


# In[17]:


#create a python program that checks if a given year is a "centuary year" (ends in 00) if it's acentuary year checks if it's a leap year.
year=int(input("please enter the year:"))
if year%100==0:
    if year%400==0:
        print("it is a leap centuary year")
    else:
        print("It is not a leap centuary year")
else:
    print("not a centuary year")


# In[ ]:





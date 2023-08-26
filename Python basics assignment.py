#!/usr/bin/env python
# coding: utf-8

# Topic: Python Basics Variable
# 
# 1. Declare two variables, `x` and `y`, and assign them integer values. Swap the
# values of these variables without using any temporary variable.
# 

# In[3]:


x = 5
y = 10
x,y = y,x


# In[8]:


x,y


# 2. Create a program that calculates the area of a rectangle. Take the length and
# width as inputs from the user and store them in variables. Calculate and
# display the area.

# In[21]:


length = float(input("Area of lenght"))
width = float(input("Area of width"))
area = length * width
print("Area of rectangle:",area)
  


# 3. Write a Python program that converts temperatures from Celsius to
# Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
# convert it to Fahrenheit, and display the result.

# In[26]:


F = (float(input("celsius")) * 9/5) +32
print("celsius: ",F)


# TOPIC: String Based Questions
#     
# 1. Write a Python program that takes a string as input and prints the length of
# the string.

# In[36]:


input_str = input("enter the string")
string_length = len(input_str)
print("The length of the string is: ",  string_length)


# 2. Create a program that takes a sentence from the user and counts the number
# of vowels (a, e, i, o, u) in the string.

# In[40]:


text = input("text: ")
count = 0
for char in text:
    if(char in "aAeEiIoOuU"):
        count += 1
print("count:", count)


# 3. Given a string, reverse the order of characters using string slicing and print
# the reversed string.

# In[45]:


input_string = input("enter the string: ")
reversed_string = input_string[::-1]
print("Reversed string: ", reversed_string)


# 4. Write a program that takes a string as input and checks if it is a palindrome
# (reads the same forwards and backwards).

# In[48]:


input_string = input("Enter the string: ")
cleaned_string = input_string.replace(" ","").lower()
reversed_string  = cleaned_string[::-1]
is_palidrome = cleaned_string == reversed_string
print("The entered string is a palidrome" if is_palidrome else "The enteres string is not a palindrome")


# 5. Create a program that takes a string as input and removes all the spaces from
# it. Print the modified string without spaces.

# In[49]:


input_string = input("Enter the string :")
space_removal = input_string.replace(" ","")
print("After removal of spaces ", space_removal)


# In[ ]:





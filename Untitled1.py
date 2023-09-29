#!/usr/bin/env python
# coding: utf-8

# # Question1
# 
# The data types are:

# In[ ]:


a.Integer
b.Float ,                    it has zero after dot(5.0),so it is decimal
c.Boolean ,                  5 is greater that 1 ,so it is true
d.string
f.mathematical expression
g.string,                     output is 55
h.string ,                    output is 52
i.mathematical expressio      result:2.5
j.algebric expression,        remainder:1
k.set
l.Boolean,                     result:False
m.float                        3.1415....    


# # Question 2
# 
#  Python expression

# In[12]:


string='Supercalifragilisticexpialidocious'
print("string-length : ",len(string))




# In[13]:


string='Supercalifragilisticexpialidocious'
substring='ice'
x=substring in string
print(x)


# In[44]:


list=['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus','Bababadalgharaghtakamminarronnkonn']
print (max(list,key=len))


# In[52]:


composers=['Berlioz', 'Borodin', 'Brian',
'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composers.sort()
firstcomposer=composers[0]
lastcomposer=composers[-1]
print(f"first composer:{firstcomposer}")
print(f"last composer:{lastcomposer}")


# # Question3
# 
# TriangleArea
# 

# In[182]:


a=float(input('Enter the length of first side:'))
b=float(input('Enter the length of second side:'))
c=float(input('Enter the length of third side:'))
s=(a+b+c)/2
import math
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))


# # question4
# Seprate odd and even integers in seprate arrays

# In[262]:


x= int(input("Input the number of elements to be stored in the array: "))
even_numbers = []
odd_numbers = []
print("Input",x, "elements in the array:")
for i in range(x):
    element = int(input(f"element - {i} : "))
    if element % 2 == 0:
        even_numbers.append(element)
    else:
        odd_numbers.append(element)
        
print("the Even Numbers are:")
print(" ".join(map(str, even_numbers)))

print("the Odd Numbers are:")
print(" ".join(map(str, odd_numbers)))
   


# # Question5
# 
# Return true or false

# In[294]:


def inside(x,y,x1,y1,x2,y2) :
return x1<=x<=x2 and y1<=y<=y2
print("inside(1,1,0,0,2,3):" ,inside(1,1,0,0,2,3))
print("inside(-1,-1,0,0,2,3):",inside(-1,-1,0,0,2,3))
   
   


# # Question6
# 
# Turn a word into pig-Latin

# In[246]:


def pig(word):
    word = word.lower()

    if word[0] in 'uieoa':
       
        return word + 'way'
    else:
        
        consonants = []
        i = 0
        while i < len(word) and word[i] not in 'aeiou':
            consonants.append(word[i])
            i += 1
        return word[i:] + ''.join(consonants) + 'ay'

print(pig('happy')) 
print(pig('Enter'))


# # Question7
# 
# Bloodtype
# 

# In[293]:


def bldcount(bloodtype1):
    bldcount('/user/donyabonyadian/bloodtype1.txt')
   
    blood_type_counts = {'A': 0, 'B': 0, 'AB': 0, 'O': 0, 'OO': 0}

   
    with open(bloodtype1, 'r') as file:
        
        for line in file:
           
            line = line.strip()
            
            
            if line in blood_type_counts:
               
                blood_type_counts[line] += 1
    
    
    for blood_type, count in blood_type_counts.items():
        if count == 1:
            print(f"There is one patient of blood type {blood_type}.")
        elif count > 1:
            print(f"There are {count} patients of blood type {blood_type}.")
        else:
            print(f"There are no patients of blood type {blood_type}.")




# In[ ]:





# # Question8
# 
# curconv function
# 

# In[ ]:





# # Question9
# 
# Type of Errors are:
# 

# In[ ]:


1.Type Error //we can not add an integer and string together.
2.Index Error //index is out of range
3.value Error// this function only get positive value
4.Name Error
5.File not found Error//IO Error


# # Question10
# Cryptanalysis

# In[259]:


def frequencies(text):
   
    letters = 'abcdefghijklmnopqrstuvwxyz'

    frequency_list = [0] * 26

    text = text.lower()


    for char in text:
        if char in letters:
        
            index = letters.index(char)
            frequency_list[index] += 1

    return frequency_list

print(frequencies('The quick red fox got bored and went home.'))
print(frequencies('apple'))



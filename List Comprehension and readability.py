
#############################List Comprehensions and Readability################################################
characr = "A"
# Build a list of Unicode codepoints from a string 
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
     codes.append(ord(symbol))
print(codes )

ord("A")

CollectionOfStrings = 'Sandhya'
EmptyBox = []
for Letter in CollectionOfStrings:
     EmptyBox.append(ord(Letter))

EmptyBox

# Alternative way to perform the above Unicode
symbols = '$¢£¥€'
codes = [ord(symbol) for symbol in symbols] 
codes 

# Expression Generator 

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols) 

symbols = 'SHARVINEE'
codes = list(ord(symbol) for symbol in symbols)
codes 

import array
K = array.array('I', (1,0,0,0,00,1))
K
print(K)
import array as a
symbols = '$¢£¥€¤'
k = a.array('I', (ord(symbol) for symbol in symbols)) 
#An unsigned variable type of int can hold zero and positive numbers,
# and a signed int holds negative, zero and positive numbers.
k

"""In 32-bit integers, an unsigned integer has a range of 
0 to 232-1 = 0 to 4,294,967,295 or about 4 billion. 
The signed version goes from -231-1 to 231, which is 
–2,147,483,648 to 2,147,483,647 or about -2 billion to +2 billion.
 The range is the same, but it is shifted on the number line. """

s= a.array('I', [36, 162, 163, 165, 8364, 164])


# Ellipsis 
data = list(range(10))
data
del data[5:7]
data
del(data[5:7])
data
data[2:]
import numpy as np # pip install numpy
arrayy = np.random.rand(2,2)
print(arrayy[0,...])

# List of List
mix_list = [1.13, 2, 5, "beginnersbook", 100, "hi"]
print(mix_list)

nest_list = [mix_list, 1.13, 2, 5]
print(nest_list)

# Augumented assignment operators += and *=
# id of lists 
l = [1,2,3]
id(l)
# ID of list will not change just append the values to the same ID
l *= 2 # Eql to L*2
l
id(l)

# id of Tuples 
t = (1,2,3)
id(t)
# ID of the tuple will change instaed of appending the values to the same ID 
t *= 2
id(t)

# += operator 

t=(1,2,[30,40])
t
t[2] += [50, 60]
t
P = (22,33,(44,88),55,66)
P
P[2]=[99,11]
P[2] += (99,11)
P
L =[22,33,44,55,66]
L[2]=99
L


# Built-in Sort Functions
animals = ['dog','pig', 'cat', 'sheep', 'goat']
# Assending order with alphaabet 
sorted(animals)
# Desending order with alphabet 
sorted(animals, reverse = True)

#  Desending order with respect to length of the character
sorted(animals, key = len, reverse = True)
# Assending order with respect to length of the character 
sorted(animals, key = len)

# Built in Function for sort
animals.sort()
sorted(animals,key=len)

name = 'Deeksha' 
len(name)
len('dog')

# Handling Missing Keys # imputation technique 

# initializing Dictionary 
d = { 'a' : 1 , 'b' : 2 } 
  
# trying to output value of absent key  
print ("The value associated with 'c' is : ") 
print (d['c']) 
print (d['b'])

# We need to handle these kind of errors  
# importing "collections" for defaultdict 
import collections as cl
  
# declaring defaultdict 
# sets default value 'Key Not found' to absent keys 
defd = cl.defaultdict(lambda : 'Value Not available') 
  
# initializing values  
defd['a'] = 1
  
# initializing values  
defd['b'] = 2
defd['c'] 
  
# printing value  
print ("The value of 'a' is : ",end="") 
print (defd['a']) 
  
# printing value associated with 'c' 
print ("The value of 'c' is : ",end="") 
print (defd['c']) 

# Sets and Frozen Sets
# A normal Set
normal_set = set(["a","a","d","d","d", "b","c"]) 
normal_set
normal_set.add("d") 

"""Note: Collective data types like set, dictionary are not ordered. 
  Any iterable, added to set will not preserve order 
  Sets have one important job that is to tell if an element is included in the set 
  and to tell it as fast as possible. Keeping the insertion order isn't on set
  to-do list"""
  
print("Normal Set") 
print(normal_set) 
  
# A frozen set 
frozen_set = frozenset(["e", "f", "g"]) 

  
print("Frozen Set") 
print(frozen_set) 

# adding a member to set in frozen set and should throw an error
frozen_set.add("h")

# Set Operations 

# Let us create sets 
set1 = set() # Null Set
set2 = set() # Null Set

# Adding elements to set1 
for i in range(1, 10): 
    set1.add(i) 

set1

for i in range(3, 10): 
    set2.add(i) 
set2

# Union of set1 and set2 
# Uninon shows all the values in set1 ans set2
set3 = set1 | set2 
#set1.union(set2) 
print("Union of Set1 & Set2: Set3 = ", set3) 
  
# Intersection of set1 and set2 
# Intersection shows common values in set1 and set2 
set4 = set1 & set2
set1.intersection(set2) 
print("Intersection of Set1 & Set2: Set4 = ", set4)     
set3 - set4
# Lets us check is there any relationship between set3 and set4
# Checking relation between set3 and set4 
if set3 > set4: # set3.issuperset(set4) 
    print("Set3 is superset of Set4") 
elif set3 < set4: # set3.issubset(set4) 
    print("Set3 is subset of Set4") 
else : # set3 == set4 
    print("Set3 is same as Set4") 
  
# displaying relation between set4 and set3 
if set4 < set3: # set4.issubset(set3) 
    print("\n")
    print("Set4 is subset of Set3") 
    print("\n") 
  
# difference between set3 and set4 
set5 = set3 - set4 
print("\n") 
print("Elements in Set3 and not in Set4: Set5 = ", set5) 

  
set4 = {1,2,3}
set5={4,5,6}
set4.isdisjoint(set5)
# checkv if set4 and set5 are disjoint sets 
if set4.isdisjoint(set5): 
    print("\nSet4 and Set5 have nothing in common\n") 
  
# Removing all the values of set5 
set5.clear() 
set5  
print("After applying clear on sets Set5: ") 
print("Set5 = ", set5) 

# Higher-Order Functions
# Defining the square of x
def square(x):
    return x * x

square(16)

# Defining the Cube of n
def sum_cubes(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k*k*k, k + 1
        return total

sum_cubes(2)

# Defining the lambda function 

s = lambda x: x * x
s
s(12)


# Functional Programming Packages
val = [1, 2, 3, 4, 5, 6]
list(map(lambda x: x * 2, val)) # function, iterables
help(map)

from functools import reduce 
reduce(lambda x, y: x * y, val)

help(reduce)
# Filter

def grea(x):
    return x>100

list(filter(grea,[111,222,3444532,4,343,2,2,3,32,32,42,4,2384848]))

# Identify, Equality & References
data = [10,20,30]
my_data = [10,20,30]
data=my_data

if  data is my_data: 
    print("Yes") 
else: 
    print("No")
    
# create another reference x3 to same list. 
df = data 

if  data is df: 
    print("Yes") 
else: 
    print("No")
    
# Let us try to use comparitive operative 
if  data == df: 
    print("Yes") 
else: 
    print("No") 

 # Alternative way to run above code
data = [10,20,30]   
df = list(data)

if  data == df: 
    print("Yes") 
else: 
    print("No") 
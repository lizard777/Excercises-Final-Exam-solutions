import pandas as pd
import numpy as np
import math



#Question 1: Write a Python script to sort (ascending and descending) a dictionary by value 
thisdict = {
    1:2,
    3:4,
    4:3,
    2:1,
    0:0
}
print(thisdict.items())

#ascending
sorted_dict = dict(sorted(thisdict.items(), key = lambda x:x[1]))
print(sorted_dict)

#descending
sorted_dict_d = dict(sorted(thisdict.items(), key = lambda x: x[1], reverse = True))
print(sorted_dict_d)



#Question 2: Write a python script to add a key to a dictionary 
sample_dictionary = {
    0:10,
    1:20
}
expected_dictionary = {
    0:10,
    1:20,
    2:30
}

for k,v in expected_dictionary.items():
    if k in sample_dictionary:
        expected_dictionary[k] = sample_dictionary[k]+ expected_dictionary[k]



#Question 3: Write a Python script to concatenate the following dictionaries to creaet a new one 
#expected result: {1:10,2:20,3:30,4:40,5:50,6:60}
dict1 = {
    1:10,
    2:20
}
dict2 = {
    3:30,
    4:40
}
dict3 = {
    5:50,
    6:60
}
dict4 = {}
for d in (dict1, dict2, dict3):
    pass


#Q4. Write a python script to check wheter a given key already exists in a dictionary
new_d = {1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60}

def in_func(x):
    if x in new_d:
        print(True)
    else:
        print(False)

in_func(3)

#Q5 Write a python program to iterate over dictionaries using for loops
new_d = {1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60}

for k,v in new_d.items():
    print('{}-{}'.format(k,v))

#Q6. Write a python script to generate and print a dictionary that contains a number 
#(between 1 and n) in the form (x,x*x)

def create_dict(n):
    if (n <=0):
        return 'bad_value'
    else:
        new_dict = {}
        for x in range(n):
            new_dict[x+1] = (x+1)*(x+1)
        return new_dict

print(create_dict(5))

#Q7. Write a python script to generate and  print a dictionary where the keys are numbers 
#between 1 and 15 ( both included) and the values are the squares of the keys

new_dict = {}
for x in range(1,16):
    new_dict[x] = x*x
print(new_dict)

#Q8 Write a python script to merge two python dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

for k,v in d2.items():
    d1[k] = d2[k]
print(d1)

#Q9 Write a python program to iterate over dictionaries using for loops 
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for k, v in d.items():
     print(k, 'corresponds to ', d[k])

#Q10 Write a python program to sum all the values in a dictionary
my_dict = {'data1':100,'data2':-54,'data3':247}

print(sum(my_dict.values()))

#Q11 Write a python program to multipy all the values in a dictionary with one variable
my_dict = {'data1':100,'data2':-54,'data3':247}
variable = 1
for x in my_dict:
    variable = variable * my_dict[x]
print(variable)

#Q12 Write a python program to remove a key from a dictionary 
my_dict = {'data1':100,'data2':-54,'data3':247}
del my_dict['data1']
print(my_dict)
#Q13 Write a python program to map two lists into a dictionary
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
keys_values = [tup for tup in zip(keys,values)]#zip creates tuples
print(keys_values)
keys_values_dict = dict(keys_values) 
print(keys_values_dict)
#Q14 Write a python program to sort a given dictionary by key
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
for key in sorted(color_dict):
    print(key, color_dict[key])

#Q15 Write a python program to get the maximum and minimum values of a dictionary
my_dict = {'data1':100,'data2':-54,'data3':247}

#max value
print(max(my_dict.values()))
#min value
print(min(my_dict.values()))


#Q17 Write a python program to remove duplicates from the dictionary
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
   'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
print(student_data)

result = {}
for k,v in student_data.items():
    if v not in result.values():
        result[k] = v

print(result)


#Q18 Write a python program to check if a dictionary is empty or not
dict = {}
if not bool(dict):
    print('dict is empty')

#Q19 Write a python program to combine two dictionaries by adding values for common keys
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for k,v in d1.items():
    if k in d2:
        d1[k] = v + d2[k]
    else:
        d1[k] = v
print(d1)

#Q20 Write a python program to print all distinct values in a dictionary


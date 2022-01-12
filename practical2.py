                 ###             DICTIONARY           ###

# Write a Python script to check whether a given key already exists in a dictionary.
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")
dict = {'a': 10, 'b': 20, 'c': 30}
key = 't'
checkKey(dict, key)
key = 'a'
checkKey(dict, key)

# Write a Python script to merge two Python dictionaries.
def Merge(dict1, dict2):
    return (dict2.update(dict1))
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print(Merge(dict1, dict2))
print(dict2)

#Write a Python program to sum all the items in a dictionary.
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

#Write a Python script to add a key to a dictionary.
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

###         TUPLE           ###

#Write a Python program to create a tuple with different data types.
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#Write a Python program to create a tuple with numbers and print one item.
tuplex = 5, 10, 15, 20, 25
print(tuplex)
tuplex = 5,
print(tuplex)

#Write a Python program to add an item in a tuple.
a_tuple = ("element1", "element2")
print(a_tuple)
new_element = ("element3",)
a_tuple = a_tuple + new_element
print(a_tuple)

#Write a Python program to convert a tuple to a string.
def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)

#Write a Python program to find the length of a tuple.
tuplex = ('w3resource',)
print(len(tuplex))

###         SET           ###

#Write a Python program to add member(s) in a set and clear a set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)
color_set.clear()

#Write a Python program to remove an item from a set if it is present in the set.
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)
print(num_set)
print("\nRemove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
num_set.discard(15)
print(num_set)

#Write a Python program to create an intersection, Union, difference of sets.
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)

#Write a Python program to find maximum and the minimum value in a set.
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#most common from list
def most_frequent(List):
    return max(set(List), key = List.count)
List = [2, 1, 2, 2, 1, 3]
a=most_frequent(List)
print(a,List.count(a))
#most common from tuple
def most_frequent(List):
    return max(set(List), key = List.count)
List = list((2, 1, 2, 2, 1, 3,))#converted tuple to list
a=most_frequent(List)
print(a,List.count(a))
#most common from dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11,5:11}
List = list(dict.values())
a=most_frequent(List)
print(a,List.count(a))
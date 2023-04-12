# # Lists: Sequence of multiple values which are seperated with comma(,) and declared inside [ ]...

# a = [32,67.5,'ramesh',64,'suresh',75]

# # print(type(a))

# b = [43,'vekatesh',65,[12,13,14],85,'hyderabad']

# print(b)

# # Nested List: Declaring the list inside other list..

# # Accessing the elements inside the string.. - indexing..

# # Indexing starts from 0 and wil go on depending on the lenght of the value..

# print(a[4])

# print(a[1:5])

# print(a[1:6:2])

# print(a[-1])

# print(a[-1:-5:-1])

# # nested indexing: Performing indexing on other indexing output..


# # print(b[3][1])

# # print(b[5][3])

# # Basic operation : 
#     # Concatenation(+): Adding the 2 list elements and making it as single list..
#     # Repetition(*): Repeating the elements inside the list multiple no.of times..

# # print([1,2,3]+["ramesh","suresh"])

# # print([1,2,3]*3)

# # List are mutubale -- Which means we can make the chnages in the list element after the declaration..

b = [43,'vekatesh',65,[12,13,14],85,'hyderabad']

# print(b)
# b[2] = 'vizag'

# print(b)

# del b[4]

# print(b)

# b[3] = 12,13,14

# print(b)

# List methods:

# print(dir(list))

# append,extend,insert -- adding the elements.
# remove,pop,clear -- removal methods
# index,count - accessing methods
# reverse,sort,copy, - order changing methods.

# append -- Its for adding sinlge element into the list at last index..

# b.append(54)
# print(b)

# # b.append([21,22,23])
# # print(b)

# # extend -- Its for adding multiple elements into the list at single go at the last index..

# b.extend([21,22,23])

# print(b)

# b.extend('ramesh')

# print(b)

# # b.extend(43)

# # during extend we have to use only sequence datatypes as values.(string,list,tuple)..

# # insert -- Adding a sinle element into the list at specific index value..

# b.insert(3,'amaravathi')

# print(b)

# # remove() -- Its for removing thhe element from the list..

# b.remove('amaravathi')

# print(b)

# pop() -- its also for removing the element from the list based on the index specified..

b.pop(4)
# print(b)

# clear() -- its for removing all the elements and make it as empty list.

# b.clear()

# print(b)

# index - to return the index value of the element isnide the list..

# print(b.index('a'))


# count() -- how many times a element is repeated isnide the list.

# print(b.count('a'))


# reverse -- It will reverse the elements inside the list..

# b.reverse()
# print(b)

# sort() -- Its for ordering the values inside the list either ascending or descending order.
    # while using sort, all the values inside the list should be of same datatype.

# a=[66,43,96,42,54,32,674,648,43,64]

# print(a)
# # a.sort()
# a.sort(reverse=True)
# print(a)


# a=['ramesh','Rajesh','Amar','akbar','Antony','vijay','balaji']

# a.sort()

# print(a)


# copy() -- 

a=[23,24,25,26]

# b=a 
# b=a.copy()

# print(id(b))
# print(id(a))
# a.append(27)

# print(id(a))
# print(id(b))

# print(a)
# print(b)


a=[43,65,84,16,42,76,25,61]
# new_list = []
# for ele in a:
#     if ele%2 == 0:
#         new_list.append(ele+5) 
#     else:
#         new_list.append(ele+3)
# print(new_list)


# List Comprehensions


# new_list = []
# for ele in a:
#     new_list.append(ele+5)
# print(new_list)
# 1st Syntax:
    # [expression for ele in sequence]

# print([ele+5 for ele in a])



# new_list = []
# for ele in a:
#     if ele%2 == 0:
#         new_list.append(ele+5)
# print(new_list)
# 2nd Syntax:
    # [expression for ele in sequence if condition]

# print([ele+5 for ele in a if ele%2==0])



# new_list = []
# for ele in a:
#     if ele%2 == 0:
#         new_list.append(ele+5)
#     else:
#         new_list.append(ele+3)
# print(new_list)
# 3rd Syntax:
    # [expression if condition else expression for ele in sequence ]

# print([ele+5 if ele%2==0 else ele+3 for ele in a])

# b = [43,'venkatesh',65,[12,13,14],85,'hyderabad']

# # b[3:4] = [12,13,14]

# index_val = b.index([12,13,14])

# b[index_val:index_val+1] = [12,13,14]

# print(b)


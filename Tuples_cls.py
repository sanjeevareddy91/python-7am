# # Tuples - Sequence of elements seperated with comma(,) declared inside ( )..

# a=(12,13,14,'python',[1,3,4])

# # print(a)

# # print(type(a))

# # b=12,13,14,'python',[1,3,4]

# # print(b)
# # print(type(b))

# # c=(12,) # single value tuple..

# # print(c)

# # print(type(c))

# # indexing -- Accessing the elements isnide the tuple..

# # print(a[1])
# # print(a[-1])

# # print(a[1:4])

# # print(a[-1:-4:-1])

# # Tuples are immutable : Elements inside the tuple cannot be chnaged once declared..

# # a[1] = 43

# # print(a[3])

# # Basic Operations
#     # Concatenation(+): Adding the 2 tuple elements and making it as single tuple..
#     # Repetition(*): Repeating the element isnide the tuple specified no.of time..


# a=(1,2,3)
# b=(4,5,6)
# print(id(a))
# print(id(b))

# c=a+b 
# print(id(c))
# print(c)


# print((1,2,3)*3)

# # Tuple methods:
#     # index() -- it will return the index of an element isnide the tuple..
#     # count() -- It will return the no.of times the element is repeated inside the tuple..



# a=(12,65,64,87,43,75,43,12,54,65,43)

# # print(a.index(43))

# # print(a.count(43))

# # print(dir(tuple))
# print(id(a))
# b=list(a)
# print(id(b))
# print(b)
# b.append(32)
# a=tuple(b)

# print(id(a))
# print(a)

# a = eval(input("Enter tuple:"))

# print(a)

# print(type(a))


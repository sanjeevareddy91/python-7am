# sets : Sequence of multiple values seperated with comma(,) which are declared inside { }.
    # Sets are going to contain only unique elements..
    # Elements inside the set has to be immutable only....
    # Sets are unordered datatype..


a={2,76,'python',(21,15,12),76,'python'}

# print(a)

# a={2,76,'python',(21,15,12),76,'python',[1,2],{1:1},{1,2}} -- Error as sets doesnot allow mutuable elements..

# set methods:
    # add,update,remove,discard,pop,
    
# Set Operations:
    # union,intersection,difference,symmetric_difference,intersection_update,sifference_update,symmetric_difference_update..
    # issuperset,issubset,isdisjoint..
# print(dir(set))

a={1,5,'python',14}

# add - for adding single element into the set..
a.add(54)

#update - for adding multiple elements into the set..

a.update('django')

a.update(['django','devops','fullstack'],{21,13,14,15})

# print(a)

# remove - for removing the element from the set..

a.remove(21)
# print(a)

# discard - for removing the element from the set..

# print(a.discard(55))
# print(a)

a.remove(21)

# pop() - it will remove the first element from the set..

# a.pop() 

# print(a)

# clear() -- will remove all the elements and make it as empty set..

# a.clear()

# print(a)

# union() -- Adding 2 set element into single set by removing duplicates..

a={1,2,65,14}

b={43,12,14,1}

# print(a.union(b))
# print(a|b)

# intersection() -- common elements between both the sets..

# print(a.intersection(b))
# print(a&b)

# difference:

# 13-14

print(a.difference(b)) # {1,2,65,14} - {43,12,14,1} = {2,65}
print(a-b)

print(b-a)  # {43,12,14,1} - {1,2,65,14} = {43,12}

# symmetric_difference()

a={1,2,65,14}

b={43,12,14,1}


# print(a.symmetric_difference(b))
# print(b^a)

# print(a)
# print(b)

# a = a.intersection(b)

# intersection_update
# difference_update
# symmetric_difference_update

# print(a)
# a.intersection_update(b)

# print(a)

# a.difference_update(b)

# print(a)

# a.symmetric_difference_update(b)

# print(a)

# issuperset() - 
# issubset() - 

a={1,6,85,23}

b={23,6}

print(a.issuperset(b))

print(a.issubset(b))

# isdisjoint()

# a={1,4,2,5}
# b={6,7,8,9}

# print(a.isdisjoint(b))







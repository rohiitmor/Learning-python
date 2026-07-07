friends = ["apple" , "orange" , 5 , 3.45 , "mango" ]
# this is a append method of a list +++++++++++++++++++++++++++++++++++++++++

print(friends[2])

friends.append("harry")
print(friends)

#sort method of list +++++++++++++++++++++++++++++++++++

l1 = [1, 4, 45, 57, 11]
l1.sort()
print(l1)

#reverse methos ++++++++++++++++++++++++++++
l1 = [1, 34, 51, 15, 25]
l1.reverse()
print(l1)

#insert method +++++++++++++++++++++++++++++++++++++++
l1 = [2, 5, 3, 6, 7, 9]
l1.insert(0, 33333)
print(l1)


#pop method ++++++++++++++++++++++++++++++++++++++++++++++
l1 = [1, 2, 3, 5, 6, 7]
print(l1.pop(2))
print(l1)


#remove method ++++++++++++++++++++++++++
l1 = [1, 2, 4, 6, 8, 9]
l1.remove(2)
print(l1)
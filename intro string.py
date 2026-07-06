name = "rohit"

print(len(name))


# start from the index 0 and end at index 4
name = "himanshu"

nameshort = name[0:4]
print(nameshort)

name = "parth"
character = name[3]
print(character)


#negative string slicing
name = "himanshu"
nameshort = name[-5:-1]
print(nameshort)

#we convert the negative index to positive index 
name = "himanshu"
nameshort = name[-5:-1] #negative
print(nameshort)

nameshort = name[1:5] #positive
print(nameshort)


name = "himanshu"
nameshort = name[:4] # its same as name[0:4]
print(nameshort)

nameshort = name[4:] # its same as name[4:len(name)]
print(nameshort)

#slicing with skip value
name = "abcdefghijkl"
nameshort = name[2:9]
print(nameshort)

nameshort = name[2:9:2] #skip value is 2
print(nameshort)


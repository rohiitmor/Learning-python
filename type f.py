a = "31.2"

t = type(a)
print(t) # <class 'str'>

b = 31.2
u = type(b)
print(u) # <class 'float'>

c = 31
v = type(c)
print(v) # <class 'int'>

d = True
w = type(d)
print(w) # <class 'bool'>


# in this example, we are converting a string to a float
e = "40.5"
f = float(e)
x = type(f)

print(x) # <class 'str'>


# write a python program to find an average of number entered by user
a = input( 56 )
b = input( 34 )
c = input( 78) 
d = a + b + c
print(d)

# write a python program to calculate the average square of a number entered by user
a = input( 4 )
b = input( 7 )
c = input( 12 )

average_square = (a**2 + b**2 + c**2) / 3
print("The average square is:", average_square)

# Empty tuple
my_tuple = ()
print(my_tuple)

#tuple having intergers
my_tuple = (1, 2, 3)
print(my_tuple)

#tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#accesing tuple elements using indices
my_tuple = ("p", "e", "r", "m", "i", "t")
print(my_tuple[0])
print(my_tuple[5])

#nested tuple
n_tuple = ("mouse",  [8, 4, 6], (1, 2, 3))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

#slicing
print("sliced :", my_tuple[1:4])

#Iterating trough tupple
for letter in ("my_tupple"):
 print("Hello", letter)

      

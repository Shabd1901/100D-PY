#Type Error, Type Checking and Type Conversion

#len(12345)   --->Error

print(type("HELLO"))   #  --> TYPE CHECKING which returns the type of the object (in this case, a string)
print(type(12345))   #  --> TYPE CHECKING which returns the type of the object (in this case, a integer)
print(type(12.0345))   #  --> TYPE CHECKING which returns the type of the object (in this case, a float(decimal))
print(type(True))   #  --> TYPE CHECKING which returns the type of the object (in this case, a boolean value)

#TYPE CONVERSION
print(int("12345"))   #  --> TYPE CONVERSION which converts a string to an integer
print(int(123) + int("456"))   #  --> TYPE CONVERSION which converts a string to an integer and adds it to another integer

#print(int("abcde"))   #  --> Error, cannot convert a non-numeric string to an integer

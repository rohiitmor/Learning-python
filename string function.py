name = "rohit"
print(len(name)) #len function is used to find the length of the string


# string endswith function is used to check whether the string ends with a specific character or not
print(name.endswith("it")) # its return True because the string ends with "it"

print(name.endswith("ro")) # its return False because the string does not ends with "ro"


#startswith function is used to check whether the string starts with a specific character or not

print(name.startswith("ro")) # its return True because the string starts with "ro"

print(name.startswith("hi")) # its return False because the string does not starts with "hi"


# string capitalize function is used to convert the first character of the string to uppercase and all other characters to lowercase
name = "rohit"
name = name.capitalize()

print(name) # its return "Rohit" because the first character of the string is converted to uppercase and all other characters are converted to lowercase


# string count function is used to count the number of occurrences of a specific character in the string
name = "rohit"

print(name.count("h")) # its return 1 because the character "h" occurs 1 time in the string


#upper function is used to convert all characters of the string to uppercase
name = "rohit"
name = name.upper()
print(name) # its return "ROHIT" because all characters of the string are converted to uppercase


#lower function is used to convert all characters of the string to lowercase
name = "rohit"
name = name.lower()
print(name) # its return "rohit" because all characters of the string are converted to lowercase


#strip function is used to remove the leading and trailing whitespaces from the string
name = "   rohit   "
name = name.strip()
print(name) # its return "rohit" because the leading and trailing whitespaces are removed from the string

#replace function is used to replace a specific character in the string with another character
name = "rohit"
name = name.replace("h", "k")
print(name) # its return "rokit" because the character "h" is replaced with "k" in the string


#split function is used to split the string into a list of substrings based on a specific character
name = "rohit"
name = name.split("h")

print(name) # its return ['ro', 'it'] because the string is split into a list of substrings based on the character "h"


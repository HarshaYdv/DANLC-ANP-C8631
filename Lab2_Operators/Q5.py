# Wap to check a character and print whether it is an alphabet, number or Special character.
# Number (0-9) : 48 to 57
# Alphabet (A-Z and a-z) : 65 to 90 and 97 to 122
# Special Characters : 33 to 47, 58 to 64, 91 to 96 and 123 to 126

print("* Input must be a Single Character *")
char = input("Enter a character : ")

result = ord(char)

if 48 <= result <= 57:
    print("This is a Number.")
elif 65 <= result <= 90:
    print("This is an Uppercase Alphabet.")
elif 97 <= result <= 122:
    print("This is a Lowercase Alphabet.")
elif 33 <= result <= 47 or 58 <= result <= 64 or 91 <= result <= 96 or 123 <= result <= 126:
    print("This is a Special Character.")
else:
    print("Invalid Character!")


# Direct Method:
"""
print("* Input must be a Single Character *")
char = input("Enter a character : ")

if ord(char) >= 48 and ord(char) <= 57:
    print("This is a Number.")
elif ord(char) >= 65 and ord(char) <= 90:
    print("This is an Uppercase Alphabet.")
elif ord(char) >= 97 and ord(char) <= 122:
    print("This is a Lowercase Alphabet.")
elif ord(char) >= 33 and ord(char) <= 47 or ord(char) >= 58 and ord(char) <= 64 or ord(char) >= 91 and ord(char) <= 96 or ord(char) >= 123 and ord(char) <= 126:
    print("This is a Special Character.")
else:
    print("Invalid Character!")
"""

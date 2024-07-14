# Wap to check whether a character is  in lower case or upper case.
# A-Z   :     65 to 90
# a-z   :     97 to 122

chr = input("Enter a character : ")

if 65 <= ord(chr) <= 90:
    print("The character is in UPPERCASE.")
elif 97 <= ord(chr) <= 122:
    print("The character is in LOWERCASE.")
else:
    print("Invalid Character")

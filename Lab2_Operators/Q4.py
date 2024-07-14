# Wap to check whether a character is alphabet or not.

ch = input("Enter a character : ")
print("Character :", ch)

if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122):
    print("It is an Alphabet.")
else:
    print("It is NOT an Alphabet.")

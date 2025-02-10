# Challenge 1 : 
# 1. Ask the user for a number and a length.
# 2. Create a program that prints a list of multiples of the 
# number until the list length reaches length.

# Solution 1: 
# num, length = map(int, input("Enter tow numbers please (separated by a space): ").split())
# liste=[]
# for i in range(1, length+1):
#     liste.append(num*i)
# print(f"list of first {length} multiples of {num}: {liste}")

# Challenge 2 :
#Write a program that asks a string to the user, 
# and display a new string with any duplicate consecutive letters removed.

# Solution 2:
word = input("Enter a string: ")
new_word= word[0]
for i in range(1, len(word)):
    if word[i] != word[i-1]:
        new_word += word[i]
print(f"String wothout consecutive duplicates: {new_word}")


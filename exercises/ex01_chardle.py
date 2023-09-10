"""Chardle 9/10/23"""

__author__ = "730655689"


word:str=input("Enter a 5-character word: ")
if(len(word)!=5):
    print("Error: Word must contain 5 characters")
    exit()
letter:str=input("Enter a single character: ")
if(len(letter)!=1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for "+ letter + " in "+ word)




count:int=0
if(letter==word[0]):
    print(letter+" found at index 1")
    count+=1
if(letter==word[1]):
    print(letter+" found at index 2")
    count+=1
if(letter==word[2]):
    print(letter+" found at index 3")
    count+=1
if(letter==word[3]):
    print(letter+" found at index 4")
    count+=1
if(letter==word[4]):
    print(letter+" found at index 5")
    count+=1
if(count==0):
    print("No instances of "+letter+" found in "+word)
else:
    print(str(count)+" instances of "+letter+" found in "+word)
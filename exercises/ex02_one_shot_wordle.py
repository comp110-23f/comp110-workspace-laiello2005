"""One Shot Wordle!"""

__author__ = "730655689"

#emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoj: str=""

#secret
sec:str = "python"

#loops to check if the guess is the right length and makes you re-submit a guess until it is the right length
check:int = 0
guess: str = input("What is your 6-letter guess?")
if (len(guess) == 6):
    check = 1

while (check == 0):
    guess = input("That was not 6 letters! Try again:")
    if (len(guess) == 6):
        check = 1


#"ind" is used to index through the guess
ind: int = 0
while (ind < len(sec)):
    #"yel" is used to index through the secret and "yel_bool" is a boolean to see if the letter that "ind" is on in the guess is present anywhere in the secret
    yel:int = 0
    yel_bool:bool = False
    while (yel < len(sec)):
        if (guess[ind] == sec[yel]):
            yel_bool = True
        yel += 1
        
    #if statements to see if the letter in the guess is green, yellow or white
    if (guess[ind] == sec[ind]):
        emoj += GREEN_BOX
    elif (yel_bool == True):
        emoj += YELLOW_BOX
    else:
        emoj += WHITE_BOX
    ind += 1

#prints final string
print(emoj)

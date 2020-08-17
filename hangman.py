import random
import json
import os

def jsonParser():
    with open('C:/Users/LENOVO/OneDrive/Documents/VSCodeProjects/PythonFiles/lettergame/words_dictionary.json', 'r') as f:
        data = json.load(f)
    
    return random.choice(list(data))

def charvalidation(wordf, nullcheckf, charcheckf, lastspacef,
                   multispacef, firstspacef, commoncheckf):
    if wordf:  # if wordf != []
        for char in range(len(wordf)):
            if (33 <= ord(wordf[char]) <= 64) or \
                    (91 <= ord(wordf[char]) <= 96) or \
                    (123 <= ord(wordf[char]) <= 127):
                charcheckf += 1
                commoncheckf += 1
                break
            if ord(wordf[-1]) == 32:
                lastspacef += 1
                commoncheckf += 1
                break
            if ord(wordf[char]) == 32 and ord(wordf[char + 1]) == 32:
                multispacef += 1
                commoncheckf += 1
        if ord(wordf[0]) == 32:
            firstspacef += 1
            commoncheckf += 1
    else:
        nullcheckf += 1
        commoncheckf += 1
    return nullcheckf, charcheckf, lastspacef, \
        multispacef, firstspacef, commoncheckf

def lettervalidation(letterf, lettercheck):
    if letterf:
        if len(letterf) > 1 or \
            (32 <= ord(letterf) <= 64) or \
            (91 <= ord(letterf) <= 96) or \
            (123 <= ord(letterf) <= 127):
            lettercheck += 1
    else:
        lettercheck += 1
    return lettercheck

def underscore(dashf, presence):
    for m in range(len(dash)):
        if ord(dashf[m]) == 95:
            presence += 1
    return presence

def missedletters(missedlistf, letterf, repititionf):
    for b in range(len(missedlistf)):
        if letterf == missedlistf[b]:
            print("\nYou repeated a wrong guess --> {}".format(missedlistf[b]))
            repititionf += 1
            break
    return repititionf

def hints(wordf, dashf):
    return random.choice(list(set(wordf) - set(dashf)))

game_mode = input("Single player or Multiplayer? (s/m): ")

if game_mode == "m":
    wordp = input("Enter word: ")  # wordp ----> for printing word in the end
    word = list(wordp)

    nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
    charvalidation(word, 0, 0, 0, 0, 0, 0)

    while commoncheck >= 1:
        while nullcheck >= 1:
            word = list(input("Enter something at least: "))
            nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
                charvalidation(word, 0, 0, 0, 0, 0, 0)
            continue
        while charcheck >= 1:
            word = list(input("Only alphabets: "))
            nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
                charvalidation(word, 0, 0, 0, 0, 0, 0)
            continue
        while lastspace >= 1:
            word = list(input("No word ends with a space: "))
            nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
                charvalidation(word, 0, 0, 0, 0, 0, 0)
            continue
        while multispace >= 1:
            word = list(input("You entered more than one space: "))
            nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
                charvalidation(word, 0, 0, 0, 0, 0, 0)
            continue
        while firstspace >= 1:
            word = list(input("No word starts with a space: "))
            nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
                charvalidation(word, 0, 0, 0, 0, 0, 0)
            continue
        continue

else:
    wordp = jsonParser()
    word = list(wordp)

# nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#     charvalidation(word, 0, 0, 0, 0, 0, 0)

# while commoncheck >= 1:
#     while nullcheck >= 1:
#         word = list(input("Enter something at least: "))
#         nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#             charvalidation(word, 0, 0, 0, 0, 0, 0)
#         continue
#     while charcheck >= 1:
#         word = list(input("Only alphabets: "))
#         nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#             charvalidation(word, 0, 0, 0, 0, 0, 0)
#         continue
#     while lastspace >= 1:
#         word = list(input("No word ends with a space: "))
#         nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#             charvalidation(word, 0, 0, 0, 0, 0, 0)
#         continue
#     while multispace >= 1:
#         word = list(input("You entered more than one space: "))
#         nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#             charvalidation(word, 0, 0, 0, 0, 0, 0)
#         continue
#     while firstspace >= 1:
#         word = list(input("No word starts with a space: "))
#         nullcheck, charcheck, lastspace, multispace, firstspace, commoncheck = \
#             charvalidation(word, 0, 0, 0, 0, 0, 0)
#         continue
#     continue

os.system('cls')
print("Start guessing...")

missedlist = []
repitition = 0

dash = []
for j in range(len(word)):
    dash.append("_")
    if ord(word[j]) == 32:
        dash[j] = " "

for k in range(len(word)):
    print(dash[k], end=' ')

print(" ")

usresult = underscore(dash, 0)  # underscore presence result from function

lives = 10
while lives > 0 and usresult >= 1:
    letter = input("\n\nEnter letter or type 'hint' for a hint: ")

    if letter != "hint":
        resultletter = lettervalidation(letter, 0)

        while resultletter >= 1:
            letter = input("Alphabet karao, gaand na marao: ")
            if letter != "hint":
                resultletter = lettervalidation(letter, 0)
                continue
            else:
                break

    pcheck = 0  # pcheck ----> presence check for letter in word
    correctrepeat = 0
    for f in range(len(word)):
        if (letter.lower() == word[f].lower()) and (letter.lower() != dash[f].lower()):
            pcheck += 1
            dash[f] = letter.lower()
        elif (letter.lower() == word[f].lower()) and (letter.lower() == dash[f].lower()):
            correctrepeat += 1
    if pcheck >= 1:
        print("\nCorrect guess...\nWell done!")
    elif correctrepeat >= 1:
        print("\nYou repeated a correct guess...")
    elif letter == "hint":
        hint = hints(word, dash)
        for c in range(len(word)):
            if hint == word[c]:
                dash[c] = hint
        lives -= 1
    else:
        missedlist.append(letter)
        if len(missedlist) > 1:
            del missedlist[len(missedlist) - 1]
            repitition = missedletters(missedlist, letter, 0)
            if repitition >= 1:
                print("\nGuess again...")
            else:
                missedlist.append(letter)
        if repitition == 0:
            lives -= 1
            print("\nWrong guess...\nYou have {0:d} lives remaining\nGuess again...".format(lives))

    print("\nMissed letters: ")
    for s in range(len(missedlist)):
        print(missedlist[s], end=' ')
    print("\n")
    for p in range(len(word)):
        print(dash[p], end=' ')

    usresult = underscore(dash, 0)

if lives >= 1:
    print("\n\nYou won! With {0:d} lives remaining.".format(lives))
else:
    print("\n\nGame over!\nThe word was '{}'".format(wordp))

input()

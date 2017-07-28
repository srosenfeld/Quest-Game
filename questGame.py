import random
import time

def questIntro():
    print('Your quest begins!')

def choosePath():
    path = ''
    while path != '1' or path != '2':
        print('Which path will you choose? (1 or 2)')
        path = input()

        return path

def checkPath(chosenPath):
    goodPath = str(random.randint(1,2))
    print(goodPath)
    if goodPath == chosenPath:
        print('good')
    else:
        print('bad')

questIntro()
pathChoice = choosePath()
checkPath(pathChoice)

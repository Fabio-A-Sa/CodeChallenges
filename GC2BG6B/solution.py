from contextlib import nullcontext
from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC
from math import pow, sqrt
import re as regex

DATA = "data/level"

def getData(level: int) -> str:

    directory = DATA + str(level) + ".txt"
    allData = []
    with open(directory, "r") as file:
        allData = file.readlines()
        file.close()

    return ''.join([element.replace("\n", "").strip() for element in allData])

def root(range: int, letter: str) -> str:
    return abc[(abc.find(letter) + range) % len(abc)] if letter in abc else nullcontext

def solve0():
    print(int(pow(2, 38))) # solution: 274877906944

def solve1():
    
    paper = {
        'k' : 'm',
        'o' : 'q',
        'e' : 'g'
    }

    for i in range(0, 26, 1):
        found = True
        for key, value in paper.items():
            found &= root(i, key) == value

        if found:
            input = "map"
            for letter in input:
                print(root(2, letter)) # solution: ocr
            break

def solve2():

    return 0

if __name__ == "__main__":
    solve2()
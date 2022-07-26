from contextlib import nullcontext
from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC
import math
import re as regex
import sys
from urllib import request
import pickle
import zipfile

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
    print(int(math.pow(2, 38))) # solution: 274877906944

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

    dictionary = dict()
    data = getData(2)
    for char in data:
        if char in dictionary.keys():
            dictionary[char] += 1
        else: dictionary[char] = 1

    minimum = math.inf
    for frequency in dictionary.values():
        minimum = min(minimum, frequency)
    
    for key, value in dictionary.items():
        if value == minimum:
            print(key, end= "") # solution: equality

def solve3():

    data = getData(3)
    regularExpression = "(?<=[a-z][A-Z]{3})[a-z](?=[A-Z]{3}[a-z])"
    for letter in regex.findall(regularExpression, data):
        print(letter, end = "") # solution: linkedlist

def solve4():

    '''
    Depois de 83 iterações, no número 16044, a continuação é com 16044/2 = 8022
    '''
    initial = 8022
    i = 0
    while True:
        try:
            text = repr(request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(initial)).read())
            initial = regex.findall("(?<=the next nothing is )[0-9]+", text)[0]
            print(i, initial)
            i += 1
        except Exception:
            break
    
    # Número de iterações: 83 + 163
    print("Solution: {}".format(initial)) # solution: 66831

def solve5():

    file = open("data/level5.p", "rb")
    items = pickle.load(file)

    for item in items:
        for char, times in item:
            print(char*times, end="")
        print("\n") # Solution: channel

def solve6():

    data = ""
    initial = 90052
    while True:

        data = ""
        with open(DATA + "6/{}.txt".format(initial), "r") as file:
            data = ''.join([line.replace("\n", "").strip() for line in file.readlines()])
            file.close()
            
        try:
            initial = regex.findall("[0-9]+", data)[0]
        except Exception:
            break

    print("Solution: {}\n{}".format(initial, data)) # 46145, Collect the comments
    file = zipfile.ZipFile("data/level6.zip","r").getinfo("{}.txt".format(initial)).comment.decode("utf-8")
    print(file, end="") # Solution: oxygen

if __name__ == "__main__":
    solve6()
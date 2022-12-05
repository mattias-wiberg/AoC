# Path: 2022/3/main.py
import os
import sys
import functools

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    big_matches = []
    small_matches = []

    for rucksack in data.split("\n"):
        mid = int(len(rucksack)/2)
        comp1 = set(rucksack[0:mid])
        comp2 = set(rucksack[mid:])
        m = comp1.intersection(comp2).pop()

        if m.isupper():
            big_matches.append(m)
        else:
            small_matches.append(m)

    b = map(lambda x: x-ord('A')+27, map(ord, big_matches))
    s = map(lambda x: x-ord('a')+1, map(ord, small_matches))
    return sum(b)+sum(s)

def part2(data):
    big_matches = []
    small_matches = []
    lines = data.split("\n")

    for i in range(0, len(lines), 3):
        g = map(set, lines[i:i+3])
        m = functools.reduce(lambda x,y: x.intersection(y), g).pop()

        if m.isupper():
            big_matches.append(m)
        else:
            small_matches.append(m)

    b = map(lambda x: x-ord('A')+27, map(ord, big_matches))
    s = map(lambda x: x-ord('a')+1, map(ord, small_matches))
    return sum(b)+sum(s)

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
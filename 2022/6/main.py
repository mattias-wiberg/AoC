# Path: 2022/6/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    a = []
    for i,c in enumerate(data):
        if c in a:
            a = a[a.index(c)+1:]

        a.append(c)
        if len(a) == 4:
            return i+1

def part2(data):
    a = []
    for i,c in enumerate(data):
        if c in a:
            a = a[a.index(c)+1:]

        a.append(c)
        if len(a) == 14:
            return i+1

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
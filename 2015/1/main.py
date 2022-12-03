# Path: 2015/day1/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    floor = 0
    for i, c in enumerate(data):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    return floor

def part2(data):
    floor = 0
    for i, c in enumerate(data):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        
        if floor == -1:
            return i + 1
    return floor

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
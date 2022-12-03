# Path: 2015/day3/main.py
from collections import namedtuple
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    Position = namedtuple('Position', ['x', 'y'])
    pos = Position(0, 0)
    visited = set([pos])
    for direction in data:
        if direction == '^':
            new_pos = Position(pos.x, pos.y + 1)
        elif direction == 'v':
            new_pos = Position(pos.x, pos.y - 1)
        elif direction == '>':
            new_pos = Position(pos.x + 1, pos.y)
        elif direction == '<':
            new_pos = Position(pos.x - 1, pos.y)
        pos = new_pos
        visited.add(pos)
    return len(visited), visited
            

def part2(data):
    len1, set1 = part1(data[::2])
    len2, set2 = part1(data[1::2])
    #print(len1)
    #print(len2)
    #print(len1+len2)
    return len(set1.union(set2))
if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data)[0])
    print(part2(data))
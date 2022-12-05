# Path: 2022/5/main.py
import os
import sys
import re

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()
"""
    [B]             [B] [S]        
    [M]             [P] [L] [B] [J]
    [D]     [R]     [V] [D] [Q] [D]
    [T] [R] [Z]     [H] [H] [G] [C]
    [P] [W] [J] [B] [J] [F] [J] [S]
[N] [S] [Z] [V] [M] [N] [Z] [F] [M]
[W] [Z] [H] [D] [H] [G] [Q] [S] [W]
[B] [L] [Q] [W] [S] [L] [J] [W] [Z]
 1   2   3   4   5   6   7   8   9 
"""

def init_stack(rows):
    stack = [[] for _ in range(9)]
    for s in rows:
        chars = s[1::4]
        for i,c in enumerate(chars):
            if c != " ":
                stack[i].append(c)
    return stack

def part1(data):
    rows = data.split("\n")
    stack = init_stack(rows[:8][::-1])
    for op in rows[10:]:
        count, _from, to = map(lambda x: int(x)-1, re.findall("\d+", op))
        count += 1
        for _ in range(count):
            item = stack[_from].pop()
            stack[to].append(item)
    
    top = ""
    for pillar in stack:
        if len(pillar) > 0:
            top += pillar.pop()

    return top

def part2(data):
    rows = data.split("\n")
    stack = init_stack(rows[:8][::-1])
    for op in rows[10:]:
        count, _from, to = map(lambda x: int(x)-1, re.findall("\d+", op))
        count += 1
        a = []
        for _ in range(count):
            item = stack[_from].pop()
            a.append(item)
        stack[to].extend(a[::-1])
    
    top = ""
    for pillar in stack:
        if len(pillar) > 0:
            top += pillar.pop()

    return top

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
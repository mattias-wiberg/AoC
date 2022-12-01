# Path: 2021/day1/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    cals = []
    summa = 0
    for line in data.split("\n"):
        if line == "":
            cals.append(summa)
            summa = 0
        else:
            summa += int(line)
    return max(cals)

def part2(data):
    cals = []
    summa = 0
    for line in data.split("\n"):
        if line == "":
            cals.append(summa)
            summa = 0
        else:
            summa += int(line)
    return sum(sorted(cals, reverse=True)[:3])

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
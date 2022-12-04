# Path: 2022/4/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    def contain(a, b): # a contains b
        return a[0]<=b[0] and a[1]>=b[1]

    count = 0
    for row in data.split("\n"):
        a,b = row.split(",")
        a = list(map(int, a.split("-")))
        b = list(map(int, b.split("-")))
        if contain(a, b) or contain(b, a):
            count += 1
    return count

def part2(data):
    def contain(a, b): # a contains b
        return (a[0]<=b[0] and b[0]<=a[1]) or (a[0]<=b[1] and b[1]<=a[1])

    count = 0
    for row in data.split("\n"):
        a,b = row.split(",")
        a = list(map(int, a.split("-")))
        b = list(map(int, b.split("-")))
        if contain(a, b) or contain(b, a):
            count += 1
    return count

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
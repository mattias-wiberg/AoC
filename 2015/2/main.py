# Path: 2015/day2/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    paper = 0
    boxes = data.split("\n")[:-1]
    for box in boxes:
        l, w, h = map(lambda x: int(x), box.split('x'))
        sides = [l*w, w*h, h*l]
        paper += 2*sum(sides)+min(sides)
    return paper

def part2(data):
    ribbon = 0
    boxes = data.split("\n")[:-1]
    for box in boxes:
        l, w, h = map(lambda x: int(x), box.split('x'))
        sides = sorted([l, w, h])
        ribbon += sides[0]*2+sides[1]*2
        ribbon += l*w*h
    return ribbon

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
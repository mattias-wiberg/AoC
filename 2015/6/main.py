# Path: 2015/day6/main.py
import os
import sys
import numpy as np

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    lights = -np.ones((1000, 1000)) 
    for op in data.split("\n"):
        args = op.split(" ")
        if args[0] == "turn":
            action = args[1]
            x1, y1 = map(int, args[2].split(","))
            x2, y2 = map(int, args[4].split(","))

            if action == "on":
                lights[x1:x2+1,y1:y2+1] = 1
            elif action == "off":
                lights[x1:x2+1,y1:y2+1] = -1
            else:
                print("Unkown action " + action)
        elif args[0] == "toggle":
            x1, y1 = map(int, args[1].split(","))
            x2, y2 = map(int, args[3].split(","))
            lights[x1:x2+1,y1:y2+1] = -lights[x1:x2+1,y1:y2+1]
        else:
            print("Unknown arg " + args[0])
    return np.sum(lights == 1)


def part2(data):
    lights = np.zeros((1000, 1000)) 
    for op in data.split("\n"):
        args = op.split(" ")
        if args[0] == "turn":
            action = args[1]
            x1, y1 = map(int, args[2].split(","))
            x2, y2 = map(int, args[4].split(","))

            if action == "on":
                lights[x1:x2+1,y1:y2+1] += 1
            elif action == "off":
                lights[x1:x2+1,y1:y2+1] -= 1
                lights[lights < 0] = 0
            else:
                print("Unkown action " + action)
        elif args[0] == "toggle":
            x1, y1 = map(int, args[1].split(","))
            x2, y2 = map(int, args[3].split(","))
            lights[x1:x2+1,y1:y2+1] += 2
        else:
            print("Unknown arg " + args[0])
    return np.sum(lights)

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
# Path: 2022/10/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    X = 1
    cycles = []

    for row in data.split("\n"):
        op = row.split(' ')
        if op[0] == "addx":
            cycles.append(X)
            cycles.append(X)
            num = int(op[1])
            X += num
        else: # noop
            cycles.append(X)

    s = 0
    for i,c in enumerate(cycles[19:220:40]):
        s += (i*40+20)*c

    return s

def part2(data):
    X = 1
    cycles = []
    crt = []
    
    def add_to_crt():
        if abs(X-(len(crt)%40)) < 2:
            crt.append('#')
        else:
            crt.append(".")

    for row in data.split("\n"):
        op = row.split(' ')
        if op[0] == "addx":
            add_to_crt()
            cycles.append(X)
            add_to_crt()
            cycles.append(X)
            num = int(op[1])
            X += num
        else: # noop
            add_to_crt()
            cycles.append(X)
    
    s = ""
    for row in range(int(len(crt)/40)):
        s += str.join("", crt[row*40:row*40+40])
        s+= "\n"

    print(s)

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
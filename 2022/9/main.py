# Path: 2022/9/main.py
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    rows = data.split("\n")
    s = np.array([0, 0])
    H = np.copy(s)
    T = np.copy(H)
    visits = set([tuple(T)])
    directions = {'R': [1, 0], 'D':[0, -1],'L':[-1, 0],'U':[0, 1]}

    for row in rows:
        op, count = row.split(" ")
        count = int(count)
        direction = directions[op]

        for _ in range(count):
            H += direction
            dist = sum((H-T)**2)**(1/2)
            if dist == 2:
                T += direction
            elif  dist > 2:
                T += np.sign(H-T) # Move diagonally towards H
            
            visits.add(tuple(T))
    plt.scatter(np.array(list(visits))[:,0], np.array(list(visits))[:,1])
    plt.waitforbuttonpress()
    plt.clf()
    return len(visits)

def part2(data):
    rows = data.split("\n")
    R = np.zeros((10, 2)) # 0: head, 1-9: knots
    visits = set([tuple(R[-1])])
    directions = {'R': [1, 0], 'D':[0, -1],'L':[-1, 0],'U':[0, 1]}

    for row in rows:
        op, count = row.split(" ")
        count = int(count)
        direction = directions[op]

        for _ in range(count):
            R[0] += direction # move head
            for i in range(1, 10):
                dist = sum((R[i-1]-R[i])**2)**(1/2)
                if dist == 2:
                    R[i] += np.sign(R[i-1]-R[i])
                elif  dist > 2:
                    R[i] += np.sign(R[i-1]-R[i]) # Move diagonally towards H
            
            visits.add(tuple(R[-1]))

        
    plt.scatter(np.array(list(visits))[:,0], np.array(list(visits))[:,1])
    plt.waitforbuttonpress()
    plt.clf()
    return len(visits)

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
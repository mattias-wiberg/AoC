# Path: 2022/8/main.py
import math
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def get_vis(points: list):
    vis = [False]*len(points)
    top = -1

    for i in range(len(points)):
        if points[i] > top:
            vis[i] = True
            top = points[i]
            if top == max(points):
                break
    return vis

def part1(data):
    grid = np.array(list((map(lambda row: [int(num) for num in row], data.split("\n")))))
    vis_grids = np.zeros((4, len(grid), len(grid[0])))
    for i in range(len(grid)):
        x_ax = grid[i]
        vis_grids[0, i, get_vis(x_ax)] = 1
        vis_grids[1, i, get_vis(x_ax[::-1])[::-1]] = 1

        y_ax = grid[:, i]
        vis_grids[2, get_vis(y_ax), i] = 1
        vis_grids[3, get_vis(y_ax[::-1])[::-1], i] = 1

    plt.imshow(vis_grids.any(axis=0))
    plt.waitforbuttonpress()
    return vis_grids.any(axis=0).sum()

def part2(data):
    grid = np.array(list((map(lambda row: [int(num) for num in row], data.split("\n")))))
    scores = np.zeros((len(grid), len(grid)))
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid)-1):
            # right up left down
            directions = np.array([(np.sin(a), np.cos(a)) for a in np.arange(0, 2*np.pi, np.pi/2)]).astype(int)
            # Alt map(lambda x: (int(x[0]), int(x[1])), [(np.cos(a), np.sin(a)) for a in np.arange(0, 2*np.pi, np.pi/2)])
            score = 1

            for row_dir, col_dir in directions:
                i = 1
                while(grid[row + row_dir*i, col + col_dir*i] < grid[row, col]):
                    i += 1
                    if any(np.array([row + row_dir*i, col + col_dir*i])>len(grid)-1) or any(np.array([row + row_dir*i, col + col_dir*i])<0):
                        i -= 1
                        break
                score *= i
            scores[row, col] = score

    plt.imshow(scores)
    plt.colorbar()
    plt.waitforbuttonpress()
    return scores.max()

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
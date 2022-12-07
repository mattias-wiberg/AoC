# Path: 2022/7/main.py
import os
import sys
import numpy as np

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()



def get_size(directory: dict, total_s: dict):
    dirs = [v for v in directory.values() if type(v) is dict]
    files = [v for v in directory.values() if type(v) is int]
    s = 0
    
    for d in dirs:
        # For every directory
        s += get_size(d, total_s)
    s += sum(files)

    directory.update({"dir_size": s})
    total_s['dir_sizes'].append(s)
    return s

def part1(data):
    curr_path = ["/"]
    dirs = {"/": {}}
    rows = data.split("\n")
    i = 0
    while True:
        args = rows[i].split(" ")
        if args[0] == "$":
            if args[1] == "ls":
                i += 1
                # Set curr_dir to current dir in dict
                curr_dir = dirs[curr_path[0]]
                for d in curr_path[1:]: 
                    curr_dir = curr_dir[d]

                while rows[i].split(" ")[0] != "$": # until next command
                    args = rows[i].split(" ")
                    
                    if args[0] == "dir":
                        dir_name = args[1]
                        if not dir_name in curr_dir.keys():
                            curr_dir.update({dir_name: {}}) # Add dir to dir
                    else:
                        size = int(args[0])
                        name = args[1]
                        curr_dir.update({name: size})
                    i += 1

                    if i >= len(rows):
                        break
            elif args[1] == "cd":
                to_dir = args[2]
                if to_dir == "..":
                    curr_path.pop()
                elif to_dir == "/":
                    curr_path = ["/"]
                else: # To a directory
                    curr_path.append(to_dir)
                i += 1

        if i >= len(rows):
            break

    get_size(dirs["/"], total_s)
    a = np.array(total_s['dir_sizes'])
    return a[a<=100000].sum()

def part2(data):
    a = np.array(total_s['dir_sizes'])
    to = 30000000-(70000000-a.max())
    dir_sizes = a[a>=to]
    closest = dir_sizes[0]
    for d_s in dir_sizes:
        if d_s > to:
            if abs(d_s-to) < abs(closest-to):
                closest = d_s
    return closest
            

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    total_s = {'sum': 0, 'dir_sizes': []}
    print(part1(data))
    print(part2(data))
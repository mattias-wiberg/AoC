# Path: 2015/day4/main.py
import os
import sys
import hashlib

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    key = 'ckczppom'
    i = 1
    result = hashlib.md5(str.encode(key + str(i)))
    while result.hexdigest()[0:5] != '00000':
        i += 1
        result = hashlib.md5(str.encode(key + str(i)))
    return result.hexdigest(), i

def part2(data):
    key = 'ckczppom'
    i = 1
    result = hashlib.md5(str.encode(key + str(i)))
    while result.hexdigest()[0:6] != '000000':
        i += 1
        result = hashlib.md5(str.encode(key + str(i)))
    return result.hexdigest(), i

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
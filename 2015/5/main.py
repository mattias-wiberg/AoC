# Path: 2015/day5/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    vowels = 'aeiou'
    banned = ['ab', 'cd', 'pq', 'xy']
    nice = 0

    for word in data.split('\n'):
        found_banned = False
        found_vowels = 0
        found_repeat = False

        for i in range(len(word)):
            if i != 0:
                if word[i-1]+word[i] in banned:
                    found_banned = True
                    break
                if word[i-1] == word[i]:
                    found_repeat = True
            if word[i] in vowels:
                found_vowels += 1
        if not found_banned and found_repeat and found_vowels >= 3:
            nice += 1
    return nice

def part2(data):
    vowels = 'aeiou'
    banned = ['ab', 'cd', 'pq', 'xy']
    nice = 0

    for word in data.split('\n'):
        found_pair = False
        found_repeat = False
        pairs = []
        index = []
        for i in range(len(word)):
            if i != 0:
                pair = word[i-1] + word[i]
                if pair in pairs:
                    idx = pairs.index(pair)
                    if i - index[idx] > 2: # No overlapping
                        found_pair = True
                else:
                    pairs.append(pair)
                    index.append(i)
            

    return nice

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
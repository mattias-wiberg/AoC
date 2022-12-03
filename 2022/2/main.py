# Path: 2022/2/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    win_matrix = [[3, 6,  0],
                  [0 , 3, 6],
                  [6 , 0, 3]]

    ret = 0
    for game in data.split("\n"):
        player_a, player_b = game.split(" ")
        action_a = ord(player_a)-ord('A')
        action_b = ord(player_b)-ord('X')
        points = win_matrix[action_a][action_b]
        ret += points + (action_b + 1)
    return ret

def part2(data):
    win_matrix = [[3, 6,  0],
                  [0 , 3, 6],
                  [6 , 0, 3]]
    

    ret = 0
    for game in data.split("\n"):
        player_a, player_b = game.split(" ")
        action_a = ord(player_a)-ord('A')
        action_b = ord(player_b)-ord('X')
        outcome = action_b*3
        action = win_matrix[action_a].index(outcome)
        ret += outcome + (action + 1)
    return ret

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
# Path: 2022/11/main.py
from functools import reduce
from collections import namedtuple

import os
import sys
import re

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

Monkey = namedtuple('Monkey', ['items', 'op', 'divisor', 'true', 'false'])

def init_monkeys(data):
    rows = data.split("\n")
    monkeys = []

    for i in range(0, len(rows), 7):
        items = list(map(int, re.findall("\d+", rows[i+1])))
        op = eval('lambda old: '+rows[i+2].split("=")[1].replace(" ", ""))
        divisor = int(re.findall("\d+", rows[i+3])[0])
        true = int(re.findall("\d+", rows[i+4])[0])
        false = int(re.findall("\d+", rows[i+5])[0])
        monkeys.append(Monkey(items, op, divisor, true, false))

    return monkeys

def part1(data):
    monkeys = init_monkeys(data)
    rounds = 20
    counts = [0]*len(monkeys)

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            counts[i] += len(monkey.items)
            for item in monkey.items:
                new_item = int(monkey.op(item)/3)
                
                if new_item%monkey.divisor == 0:
                    monkeys[monkey.true].items.append(new_item)
                else:
                    monkeys[monkey.false].items.append(new_item)

            monkey.items.clear()
            
    return reduce(lambda x,y: x*y, sorted(counts)[-2:])

def part2(data):
    monkeys = init_monkeys(data)
    rounds = 10000
    counts = [0]*len(monkeys)
    lcm = reduce(lambda x,y: x*y, map(lambda m: m.divisor, monkeys))

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            counts[i] += len(monkey.items)
            for item in monkey.items:
                new_item = monkey.op(item)%lcm
                
                if new_item%monkey.divisor == 0:
                    monkeys[monkey.true].items.append(new_item)
                else:
                    monkeys[monkey.false].items.append(new_item)

            monkey.items.clear()
        
    return reduce(lambda x,y: x*y, sorted(counts)[-2:])

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))
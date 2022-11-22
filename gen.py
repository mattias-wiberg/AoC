import os
import requests

session_id = "53616c7465645f5f6ade0dd6ec8ce2d00cc43d73776b5f6bf1b27999f9e920bba41849d6ae79de4a13a39561f7dd80f32a722a8ffef7ff8985f86672e1fb8909"

def generate():
    for year in range(2015, 2021+1):
        for day in range(1, 25+1):
            os.makedirs(f"{year}/{day}", exist_ok=True)
            with open(f"{year}/{day}/input.txt", "w") as f:
                f.write(requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session_id}).text)
            with open(f"{year}/{day}/main.py", "w") as f:
                f.write(f"""# Path: {year}/day{day}/main.py
import os
import sys

def read_input(path):
    with open(os.path.join(path,"input.txt")) as f:
        return f.read()

def part1(data):
    pass

def part2(data):
    pass

if __name__ == "__main__":
    data = read_input(os.path.dirname(os.path.abspath(__file__)))
    print(part1(data))
    print(part2(data))""")
            print(f"Generated {day} of {year}")

generate()
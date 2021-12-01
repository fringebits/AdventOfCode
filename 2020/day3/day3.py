import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

import functools

sample_input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

@utils.timer
def run():
    print("\n***** Day 3 *****")
    
    f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input = [line.strip() for line in f]
    f.close()

    # run the sample 
    run_part1(sample_input)
    run_part1(input)

    run_part2(sample_input)
    run_part2(input)

def run_part1(input):
    "Count the trees encountered using Right3 - Down1"
    count = count_trees(input, utils.Vec2(3,1))
    print("part1: {0} trees".format(count))

def run_part2(input):
    list = []
    list.append(count_trees(input, utils.Vec2(1,1)))
    list.append(count_trees(input, utils.Vec2(3,1)))
    list.append(count_trees(input, utils.Vec2(5,1)))
    list.append(count_trees(input, utils.Vec2(7,1)))
    list.append(count_trees(input, utils.Vec2(1,2)))

    count = functools.reduce((lambda x, y: x * y), list)
    print("part2: {0} trees".format(count))

def count_trees(input, step):
    "Count the trees encountered using Right3 - Down1"
    count = 0
    pos = utils.Vec2(0, 0)
    while pos.Y < len(input):
        if is_tree(input, pos):
            count += 1
        pos += step
    return count

def is_tree(input, pos):
    line = input[pos.Y]
    col = pos.X % len(line)
    return line[col] == '#'

if __name__ == "__main__":
    run()
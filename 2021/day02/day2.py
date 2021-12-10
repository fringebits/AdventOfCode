import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

sample_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"]

@utils.timer
def run():
    print("\n***** Day 2 *****")
    
    f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input = [line.strip() for line in f]
    f.close()

    # part 1:
    #run_part1(sample_input)
    run_part1(input)

    # part 2:
    #run_part2(sample_input)
    run_part2(input)

def run_part1(input):
    "part1: Dive"
    # forward X increases the horizontal position by X units.
    # down X increases the depth by X units.
    # up X decreases the depth by X units.

    pos = utils.Vec2(0, 0)

    for line in input:
        delta = parse_move(line)
        pos += delta
    print("part1: {0}, result = {1}".format(pos, pos.X * pos.Y))
    

def run_part2(input):
    "part2: Dive and Aim"
    # down X increases your aim by X units.
    # up X decreases your aim by X units.
    # forward X does two things:
    #   It increases your horizontal position by X units.
    #   It increases your depth by your aim multiplied by X.    
    aim = 0
    pos = utils.Vec2(0, 0)
    for line in input:
        delta = parse_move(line)
        aim += delta.Y
        pos.X += delta.X
        pos.Y += aim * delta.X
    print("part2: {0}, result = {1}".format(pos, pos.X * pos.Y))

def parse_move(line):
    "Parse single line, return Vec2 representing the move"
    # Parse single line, using a "Forward-Down axis"
    # forward X:  (X, 0)
    # up X: (0, -X)
    # down X: (0, X)
    pair = line.split(' ')
    result = utils.Vec2(0, 0)

    if (pair[0]== 'up'):
        result.Y = -int(pair[1])
    elif (pair[0]== 'down'):
        result.Y = int(pair[1])
    elif (pair[0]== 'forward'):
        result.X = int(pair[1])

    return result

if __name__ == "__main__":
    run()
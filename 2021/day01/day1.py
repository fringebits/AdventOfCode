import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

#
# https://adventofcode.com/2021/day/1
#

sample_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

@utils.timer
def run():
    print("\n***** Day 1 *****")
    
    f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input = list(map(int, f.readlines()))
    f.close()

    # part 1:
    #run_part1(sample_input)
    run_part1(input)

    # part 2:
    #run_part2(sample_input)
    run_part2(input)

def run_part1(input):
    "part1: count the number of times a depth measurement increases from the previous measurement."
    count = count_increases(input, 1)
    print("part1: increases = {0}".format(count))

def run_part2(input):
    "part2: three-measurement sliding window"
    count = count_increases(input, 3)
    print("part2: increases = {0}".format(count))

def count_increases(input, width):
    "Count the number of increases in the input, with a sliding window of 'width' elements."
    # note that in the 'sliding window', there are common elements and we don't need to consider
    # those because their net difference is zero.
    count = 0
    for ii in range(width, len(input)):
        if input[ii] > input[ii-width]:
            count += 1
    return count

if __name__ == "__main__":
    run()
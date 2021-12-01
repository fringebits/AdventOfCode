import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

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
    count = 0
    for ii in range(1, len(input)):
        if input[ii] > input[ii-1]:
            count += 1
    print("part1: increases = {0}".format(count))

def run_part2(input):
    "part2"
    count = 0
    for ii in range(3, len(input)):
        if input[ii] > input[ii-3]:
            count += 1
    print("part2: increases = {0}".format(count))

if __name__ == "__main__":
    run()
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 7 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    crabs = list(map(int, input.split(',')))

    # part 1:
    run_part1(crabs)

    # part 2:
    run_part2(crabs)

def run_part1(crabs):
    # part1: movement is a cost of '1' 
    cost = find_min_cost(crabs, lambda x: x)    
    print("Part1: min cost = {0}".format(cost))
            
def run_part2(crabs):
    # part2: movement is a cost of 1+2+3+... (arithmatic sum) = x * (1+x)/2
    cost = find_min_cost(crabs, lambda x: int(x * ((1 + x) / 2)))
    print("Part2: min cost = {0}".format(cost))

def find_min_cost(crabs, move_cost_func):
    # consider all alignment positions, compute cost for each, return minimum
    cost = cost_to_align(crabs, min(crabs), move_cost_func)
    for ii in range(min(crabs), max(crabs)): # range of positions to consider...
        val = cost_to_align(crabs, ii, move_cost_func)
        if val > cost:
            # once the new cost starts going back up, we're done (will only be one local minima)
            break
        cost = min(cost, val)
    return cost

def cost_to_align(crabs, pos, move_cost_func):
    # compute cost of moving all crabs to specified position using the 'move_cost_func'
    result = 0
    for crab in crabs:
        result += move_cost_func(abs(crab - pos))
    return result

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input[0]

if __name__ == "__main__":
    run()
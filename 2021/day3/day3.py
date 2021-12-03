import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 3 *****")

    sample_input = load_input('sample_input.txt')
    input = load_input('input.txt')
    
    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

def run_part1(input):
    gamma = int(compute_gamma(input), 2)
    epsilon = int(compute_epsilon(input), 2)
    power = gamma * epsilon
    print("part1: gamma={0}, epsilon={1}, power={2}".format(gamma, epsilon, power))
    
def run_part2(input):
    oxygen_rating = compute_oxygen_rating(input)
    scrub_rating = compute_scrub_rating(input)
    life_support = oxygen_rating * scrub_rating
    print("part2: oxygen_rating = {0}, scrub_rating = {1}, life_support = {2}".format(oxygen_rating, scrub_rating, life_support))


def compute_gamma(input):
    # count the number of ones in each position
    count = len(input)
    width = len(input[0])
    one_count = [0] * width
    for line in input:
        for ii in range(width):
            if line[ii] == '1':
                one_count[ii] += 1
    
    result = ""
    for ii in range(width):
        if one_count[ii] >= (count - one_count[ii]):
            result = result + '1'
        else:
            result = result + '0'

    #print("gamma   = {0} = {1}".format(result, int(result, 2)))
    return result

def compute_epsilon(input):
    # count the number of ones in each position
    count = len(input)
    width = len(input[0])
    one_count = [0] * width
    for line in input:
        for ii in range(width):
            if line[ii] == '1':
                one_count[ii] += 1
    
    result = ""
    for ii in range(width):
        if one_count[ii] >= (count - one_count[ii]):
            result = result + '0'
        else:
            result = result + '1'

    #print("epsilon = {0} = {1}".format(result, int(result, 2)))
    return result

def compute_common_mask(input, bit):
    # count the number of ones in each position
    count = len(input)
    width = len(input[0])
    one_count = [0] * width
    for line in input:
        for ii in range(width):
            if line[ii] == '1':
                one_count[ii] += 1
    
    result = ""
    for ii in range(width):
        if one_count[ii] >= (count - one_count[ii]):
            result = result + ('0' if bit else '1')
        else:
            result = result + ('1' if bit else '0')

    #print("epsilon = {0} = {1}".format(result, int(result, 2)))
    return result

def compute_oxygen_rating(input):
    bit = 0
    while len(input) > 1:
        gamma = compute_gamma(input)
        input = [line for line in input if line[bit] == gamma[bit]]
        bit += 1
    result = int(input[0], 2)
    #print("oxygen_rating = {0} = {1}".format(input[0], result))
    return result

def compute_scrub_rating(input):
    bit = 0
    while len(input) > 1:
        gamma = compute_epsilon(input)
        input = [line for line in input if line[bit] == gamma[bit]]
        bit += 1
    result = int(input[0], 2)
    #print("scrub_rating = {0} = {1}".format(input[0], result))
    return result

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    input = [line.strip() for line in f]
    f.close()
    return input


if __name__ == "__main__":
    run()
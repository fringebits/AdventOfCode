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
    gamma = compute_gamma(input)
    epsilon = compute_epsilon(input)
    power = int(gamma,2) * int(epsilon,2)
    print("part1: gamma={0}, epsilon={1}, power={2}".format(gamma, epsilon, power))
    
def run_part2(input):
    oxygen_rating = compute_oxygen_rating(input)
    scrub_rating = compute_scrub_rating(input)
    life_support = oxygen_rating * scrub_rating
    print("part2: oxygen_rating = {0}, scrub_rating = {1}, life_support = {2}".format(oxygen_rating, scrub_rating, life_support))

def compute_gamma(input):
    # Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the input.
    # count the '1's in each position.
    count = len(input)
    width = len(input[0])
    one_count = [0] * width  # array to hold count of 'ones'
    for line in input:
        for ii in range(width):
            if line[ii] == '1':
                one_count[ii] += 1
    
    result = ""
    for ii in range(width):
        # now figure out which is most common (1 or 0)
        if one_count[ii] >= (count - one_count[ii]):
            result = result + '1'
        else:
            result = result + '0'
    return result

def compute_epsilon(input):
    # The epsilon rate is calculated similar to gamma, rather than use the most common bit, the least common bit from each position is used.
    # Since each bit is independent, we can just 'invert the gamma mask'
    gamma = compute_gamma(input)
    return ''.join(list(map(lambda x: ('0' if x == '1' else '1'), gamma)))

def compute_oxygen_rating(input):
    # oxygen rating is computed by filtering based on 'compute_gamma'
    return compute_rating(input, compute_gamma)

def compute_scrub_rating(input):
    # oxygen rating is computed by filtering based on 'compute_epsilon'
    return compute_rating(input, compute_epsilon)

def compute_rating(input, func):
    bit = 0
    while len(input) > 1:
        gamma = func(input)
        input = [line for line in input if line[bit] == gamma[bit]]
        bit += 1
    result = int(input[0], 2)
    return result

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    input = [line.strip() for line in f]
    f.close()
    return input

if __name__ == "__main__":
    run()
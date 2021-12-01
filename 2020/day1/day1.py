import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

sample_input = [1721, 979, 366, 299, 675, 1456]

@utils.timer
def run():
    print("\n***** Day 1 *****")
    
    f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input = list(map(int, f.readlines()))
    f.close()

    # part 1: find the product of two entries that sum to 2020
    #run_part1(sample_input)
    run_part1(input)

    # part 2: find product of three entries that sum to 2020
    #run_part2(sample_input)
    run_part2(input)

def run_part1(input):
    "Given the input array, find the product of two entries that sum to 2020"
    input.sort()
    ret = findpair(input, 2020)
    if (ret is not None):
        product = input[ret[0]] * input[ret[1]]
        print("part1: {0} x {1} = {2}".format(input[ret[0]], input[ret[1]], product))

def run_part2(input):
    "Given the input array, find the product of three entries that sum to 2020"
    input.sort()

    for aa in range(len(input)):
        ret = findpair(input, 2020 - input[aa])
        if ((ret is not None) and (ret[0] != aa) and (ret[1] != aa)):
            product = input[aa] * input[ret[0]] * input[ret[1]]
            print("part2: {0} x {1} x {2} = {3}".format(input[aa], input[ret[0]], input[ret[1]], product))
            break

def findpair(input, value):
    "Given an SORTED input array, find the indices of two entries that sum to the desired total"
    input.sort()

    for jj in range(len(input)):
        aa = input[jj]
        bb = value - aa
        if (bb < input[0]):
            return None

        kk = utils.bisect(input, bb)
        if (kk > 0 and kk < len(input) and input[kk]==bb):
            return (jj, kk)

    return None

if __name__ == "__main__":
    run()
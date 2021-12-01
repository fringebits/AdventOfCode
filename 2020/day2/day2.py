import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

sample_input = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

@utils.timer
def run():
    print("\n***** Day 2 *****")
    
    f = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
    input = list(f.readlines())
    f.close()

    # run the sample 
    #run_part1(sample_input)
    run_part1(input)

    #run_part2(sample_input)
    run_part2(input)

def run_part1(input):
    "Count the number of valid passwords"

    result = 0
    for line in input:
        # parse the rule / password
        lhs, rhs = line.split(":")
        policy = Policy(lhs)
        if policy.IsValid_Part1(rhs):
            result += 1

    print("part1: {0} valid passwords".format(result))

def run_part2(input):
    "Count the number of valid passwords"

    result = 0
    for line in input:
        # parse the rule / password
        lhs, rhs = line.split(":")
        policy = Policy(lhs)
        if policy.IsValid_Part2(rhs):
            result += 1

    print("part2: {0} valid passwords".format(result))

class Policy:
    def __init__(self, line) -> None:
        lhs, self.key = line.split(" ")
        rmin, rmax = lhs.split("-")
        self.range = [int(rmin), int(rmax)]
        # print("Policy: {0}-{1} {2}".format(self.range[0], self.range[1], self.key))

    def IsValid_Part1(self, line):
        "Validate password, returns True if password meets the policy"
        count = len(line) - len(line.replace(self.key, ''))
        return count >= self.range[0] and count <= self.range[1]

    def IsValid_Part2(self, line):
        "Validate password, returns True if password meets the policy"
        first_valid = line[self.range[0]] == self.key
        second_valid = line[self.range[1]] == self.key

        return utils.xor(first_valid, second_valid)

if __name__ == "__main__":

    import sys
    sys.path.append('../..')
    import utils

    run()
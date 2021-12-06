import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

verbose = False

@utils.timer
def run():
    print("\n***** Day 6 *****")

    input = load_input('sample_input.txt')
    #input = load_input('input.txt')

    # part 1:
    run_part1(input)

    # part 2:
    #run_part2(input)

def run_part1(input):
    days = 80
    count = run_sim(input, days)
    print("Part1: {0} days = {1} fish".format(days, count))
            
def run_part2(input):
    days = 256
    count = run_sim(input, days)
    print("Part2: {0} days = {1} fish".format(days, count))

def run_sim(input: str, days: int):
    flock = Flock()
    flock.fishes = [Fish(int(v)) for v in input.split(',')]

    #flock.PrintFlock()
    for d in range(days):
        flock.Tick()
        if verbose:
            flock.PrintFlock()
    return len(flock.fishes)


def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input[0]

class Fish:
    def __init__(self, cooldown: int):
        self.origin = cooldown
        self.cooldown = cooldown

    def __str__(self):
        return "{0}".format(self.cooldown)

class Flock:
    def __init__(self):
        self.fishes = []
        self.elapsed = 0

    def Tick(self):
        self.elapsed += 1
        newfish = []
        for fish in self.fishes:
            if fish.cooldown == 0:
                newfish.append(Fish(8))
                fish.cooldown = 6
            else:
                fish.cooldown = fish.cooldown - 1
        
        self.fishes += newfish

    def PrintFlock(self):
        fish = ["{0}".format(v) for v in self.fishes]
        print("day {0:3}: {2:3} : {1}".format(self.elapsed, ",".join(fish), len(fish)))

if __name__ == "__main__":
    run()
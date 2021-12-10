import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

verbose = False

@utils.timer
def run():
    print("\n***** Day 6 *****")

    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    # part 1:
    run_part1(input)

    # part 2:
    run_part2(input)

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
    for fish in input.split(','):
        flock.pens[int(fish)] += 1
    
    if verbose:
        flock.PrintFlock()

    for d in range(days):
        flock.Tick()
        if verbose:
            flock.PrintFlock()
    return flock.Count()


def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input[0]
class Flock:
    MaxAge = 8
    Respawn = 6

    def __init__(self):
        self.pens = [0] * (self.MaxAge+1)
        self.elapsed = 0

    def Tick(self):
        self.elapsed += 1
        newfish = []
        for slot in range(self.MaxAge+1):
            if slot == 0:
                # all the fishes in slot 0 get moved to slot 6, and we 
                # get that many new fishes
                newfish = self.pens[0]
                self.pens[0] = 0
            else:
                self.pens[slot-1] = self.pens[slot]
                self.pens[slot] = 0
        
        if newfish > 0:
            self.pens[self.MaxAge] = newfish
            self.pens[self.Respawn] += newfish

    def Count(self):
        return sum(self.pens)

    def PrintFlock(self):
        fish = ["{0:3}".format(v) for v in self.pens]
        print("day {0:3}: {2:3} : {1}".format(self.elapsed, " ".join(fish), self.Count()))

if __name__ == "__main__":
    run()
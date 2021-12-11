import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 9 *****")

    #input = load_input('test_input.txt')
    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    map = FlashMap(input)

    # part 1:
    run_part1(map, 100)

    map.Reset()

    # part 2:
    run_part2(map)

def run_part1(map, step_count):
    # part1: count the number of flashes for step_count steps (ticks) of the map
    count = 0
    for ii in range(step_count):
        count += map.Step()
    print("part1: flash_count = {0}".format(count))

def run_part2(map):
    # part2: run simulation until all flash at the same time
    count = 0
    while True:
        count += 1
        if map.Step() == (map.width * map.height):
            break
    print("part2: all flash on step = {0}".format(count))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class FlashMap:
    def __init__(self, input):
        self.width = len(input[0])
        self.height = len(input)
        self.data = []
        for row in input:
            self.data += [int(x) for x in row]
        self.original = list(self.data)

    def Reset(self):
        self.data = list(self.original)

    def IndexToPos(self, index):
        return utils.Vec2(index % self.width, int(index / self.width))
    
    def PosToIndex(self, pos):
        return pos.X + pos.Y * self.width

    def IsValidPos(self, pos):
        if pos.X < 0 or pos.Y < 0:
            return False
        if pos.X > self.width-1 or pos.Y > self.height-1:
            return False
        return True

    def IncrementValueAt(self, pos):
        if pos.X < 0 or pos.Y < 0:
            return None
        if pos.X > self.width-1 or pos.Y > self.height-1:
            return None
        index = self.PosToIndex(pos)
        return self.data[index]


    def Step(self):
        # Step the simulation:
        # 1. The energy level of each octopus increases by 1.
        # 2. Any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
        # 3. Any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

        offsets = [ utils.Vec2(-1, -1), utils.Vec2(-1,  0), utils.Vec2(-1, +1), 
                    utils.Vec2( 0, -1), utils.Vec2( 0, +1),
                    utils.Vec2(+1, -1), utils.Vec2(+1,  0), utils.Vec2(+1, +1) ]
        flashers = []
        flash_count = 0
        needs_reset = []

        for ii in range(len(self.data)):
            self.data[ii] += 1
            if (self.data[ii] > 9):
                flashers.append(ii)

        flash_count += len(flashers)
        needs_reset = list(flashers)

        while len(flashers) > 0:
            ii = flashers.pop()
            fpos = self.IndexToPos(ii) # position of this flasher
            for ofs in offsets:
                pos = fpos + ofs
                if self.IsValidPos(pos): # confirm this position is on the map
                    index = self.PosToIndex(pos)
                    self.data[index] += 1 # increment this spot
                    if self.data[index] > 9:
                        needs_reset.append(index)
                        if self.data[index] == 10:
                            # if we just hit 10 on this, we are a *NEW* flasher
                            flash_count += 1
                            flashers.append(index)

        for ii in needs_reset:
            self.data[ii] = 0

        return flash_count

    def PrintBoard(self):
        for ii in range(0, self.height):
            a = ii * self.width
            b = (ii+1) * self.width
            #row = ["{0}".format('.' if v==0 else v) for v in self.data[a:b]]
            row = ["{0} ".format(v) for v in self.data[a:b]]
            print("".join(row))
        print("---")

if __name__ == "__main__":
    run()
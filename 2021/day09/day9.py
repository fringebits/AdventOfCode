import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 9 *****")

    #lines = load_input('sample_input.txt')
    lines = load_input('input.txt')

    # part 1:
    run_part1(lines)

    # part 2:
    run_part2(lines)

def run_part1(map):
    # part1: movement is a cost of '1' 
    points = map.FindLowPoints()
    result = 0
    for p in points:
        result += map.GetValueAt(p) + 1
    print("part1: risk = {0}".format(result))

def run_part2(map):
    # part1: movement is a cost of '1' 
    points = map.FindLowPoints()

    basins = []
    for p in points:
        basin = map.ComputeBasin(p)
        basins.append(len(basin))

    basins.sort(reverse=True)
    result = basins[0] * basins[1] * basins[2]
    print("part2: basins = {0}".format(result))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()

    return HeightMap(input)

class HeightMap:
    def __init__(self, input):
        self.width = len(input[0])
        self.height = len(input)
        self.data = []
        for row in input:
            self.data += [int(x) for x in row]

    def IndexToPos(self, index):
        return utils.Vec2(index % self.width, int(index / self.width))
    
    def PosToIndex(self, pos):
        return pos.X + pos.Y * self.width

    def GetValueAt(self, pos):
        if pos.X < 0 or pos.Y < 0:
            return None
        if pos.X > self.width-1 or pos.Y > self.height-1:
            return None
        index = self.PosToIndex(pos)
        return self.data[index]

    def FindLowPoints(self):
        result = [] # array of low points
        for ii in range(len(self.data)):
            pos = self.IndexToPos(ii)
            val = self.data[ii]
            if (pos.X > 0): # ok to look left
                newVal = self.data[ii-1]
                if val >= newVal: 
                    continue
            if (pos.X < self.width-1): # ok to look right
                newVal = self.data[ii+1]
                if val >= newVal: 
                    continue
            if (pos.Y > 0): # ok to look UP
                newVal = self.data[ii-self.width]
                if val >= newVal: 
                    continue
            if (pos.Y < self.height-1): # ok to look right
                newVal = self.data[ii+self.width]
                if val >= newVal: 
                    continue
            #print('Min {0} at {1}'.format(val, pos))
            result.append(pos)
        return result

    def ComputeBasin(self, pos):
        basin = []
        visited = []
        open = [pos]

        offsets = [ utils.Vec2(-1, 0), utils.Vec2(1, 0), utils.Vec2(0, -1), utils.Vec2(0, 1) ]

        while len(open) > 0:
            pos = open.pop(0)  #pop the top item off the list
            if pos in visited:
                # we've already looked at pos; skip it
                continue
            basin.append(pos)
            visited.append(pos)
            for ofs in offsets:
                val = self.GetValueAt(pos + ofs)
                if val is None or val == 9:
                    continue
                open.append(pos + ofs)

        return basin

if __name__ == "__main__":
    run()
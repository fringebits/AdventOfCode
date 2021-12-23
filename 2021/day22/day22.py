import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

@utils.timer
def run():
    print("\n***** Day 22 *****")

    #lines = utils.load_input(__file__, "test_input.txt")
    #lines = utils.load_input(__file__, "sample_input.txt")
    lines = utils.load_input(__file__, "input.txt")

    puzzle = Puzzle(lines)
    puzzle.ExecuteAll()
    print(f"Part1: lights = {len(puzzle.lights)}")

def clamp(value, min_val, max_val):
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value

class Step:
    def __init__(self, line):
        ex = re.compile("(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")
        match = ex.match(line)
        
        self.state = True if match.group(1) == 'on' else False
        self.X = self.MakeRange(int(match.group(2)), int(match.group(3))+1)
        self.Y = self.MakeRange(int(match.group(4)), int(match.group(5))+1)
        self.Z = self.MakeRange(int(match.group(6)), int(match.group(7))+1)
        print(f"{self.state} {self.X}, {self.Y}, {self.Z}")

    def MakeRange(self, min_val, max_val):
        _limit = 51
        min_val = clamp(min_val, -_limit, _limit)
        max_val = clamp(max_val, -_limit, _limit)
        return range(min_val, max_val)

class Puzzle:
    def __init__(self, lines):
        self.steps = [Step(x) for x in lines]
        self.lights = set()

    def ExecuteAll(self):
        for step in self.steps:
            self.ExecuteStep(step)

    def ExecuteStep(self, step):
        for xx in step.X:
            for yy in step.Y:
                for zz in step.Z:
                    if step.state:
                        self.lights.add(utils.Vec3(xx, yy, zz))
                    else:
                        self.lights.discard(utils.Vec3(xx, yy, zz))
        




if __name__ == "__main__":
    run()
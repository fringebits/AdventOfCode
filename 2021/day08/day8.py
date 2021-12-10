import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 8 *****")

    #lines = load_input('sample_input.txt')
    lines = load_input('input.txt')
    #lines = [Line(x) for x in ["fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb"]]
    #lines = [Line(x) for x in ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]]

    # part 1:
    run_part1(lines)

    # part 2:
    run_part2(lines)

def run_part1(lines):
    # part1: movement is a cost of '1' 
    count = 0
    for line in lines:
        for d in line.output:
            if d.IsUnique():
                count += 1
    print("Part1: unique count = {0}".format(count))
            
def run_part2(lines):
    count = 0
    for line in lines:
        ret = line.Result()
        #print("value = {0}".format(line.Result()))
        count += ret
    print("Part2: output sum = {0}".format(count))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return [Line(x) for x in input]

class Line:
    def __init__(self, line):
        #print("Parsing line: {0}".format(line))
        digits, output = line.split("|")
        self.segment = Segment([Digit(set(x)) for x in digits.strip().split(" ")])
        self.output = [Digit(set(x)) for x in output.strip().split(" ")]

    def Result(self):
        result = 0
        p = 1
        for d in self.output[::-1]:
            value = self.segment.Evaluate(d)
            result += p * value
            p *= 10
        return result

# Single digit
class Digit:
    def __init__(self, string):
        self.string = string
        self.value = None

    def __str__(self):
        return "{0} ({1})".format(",".join(self.string), self.value)

    def Count(self):
        return len(self.string)

    def SetValue(self, value:int):
        self.value = value
        #print("\t{0}".format(self))

    def IsUnique(self):
        size = self.Count()
        return size == 2 or size == 4 or size == 3 or size == 7

    def Difference(A, B): # start with A, remove matching items from B
        ret = A.string.difference(B.string)
        return Digit(ret)

    def Union(A, B):
        ret = A.string.union(B.string)
        return Digit(ret)

    def IsMatch(A, B):
        return A.string == B.string

    def Contains(self, A):
        return self.string.issuperset(A.string)

# Class to represent a 7-segment display
class Segment:
    def __init__(self, digits):
        self.digits = digits

        assert len(digits) == 10

        d1 = next(filter(lambda x: x.Count() == 2, self.digits), None)
        d1.SetValue(1)

        d4 = next(filter(lambda x: x.Count() == 4, self.digits), None)
        d4.SetValue(4)

        d7 = next(filter(lambda x: x.Count() == 3, self.digits), None)
        d7.SetValue(7)

        d8 = next(filter(lambda x: x.Count() == 7, self.digits), None)
        d8.SetValue(8)

        # d6
        d6 = next(filter(lambda x: x.Count() == 6 and not x.Contains(d1), self.digits), None)
        d6.SetValue(6)

        # d5
        d5 = self.FindDigitByCountAndDifference(5, d6, 1)
        #d5 = next(filter(lambda x: x.Count() == 5 and Digit.Difference(d6, x).Count() == 1, self.digits), None)
        d5.SetValue(5)

        # d9
        r = Digit.Union(d4, d7)
        d9 = next(filter(lambda x: x.Count() == 6 and Digit.Difference(x, r).Count() == 1, self.digits))
        d9.SetValue(9)

        d0 = next(filter(lambda x: x.Count() == 6 and x.value is None, self.digits))
        d0.SetValue(0)

        assert len(list(filter(lambda x: x.Count() == 5 and x.value is None, self.digits))) == 2

        d2 = next(filter(lambda x: x.Count() == 5 and x.value is None and Digit.Difference(d5, x).Count() == 2, self.digits))
        d2.SetValue(2)

        d3 = next(filter(lambda x: x.Count() == 5 and x.value is None and Digit.Difference(d5, x).Count() == 1, self.digits))
        d3.SetValue(3)

    def Evaluate(self, digit: Digit):
        # given a digit, figure out what number it is
        d = next(filter(lambda x: Digit.IsMatch(x, digit), self.digits))
        return d.value

    def FindDigitByCountAndDifference(self, count, ref, delta):
        #ret = next(filter(lambda x: x.Count() == 6 and Digit.Difference(ref, x).Count() == delta, self.digits), None)
        #return ret
        #print("FindDigitByCountAndDifference:  count={0}, ref={1}, delta={2}".format(count, ref, delta))
        for d in [x for x in self.digits if x.Count() == count]:
            ret = Digit.Difference(ref, d)
            #print("\tdigit={2} diff={0} delta={1}".format(ret, ret.Count(), d))
            if ret.Count() == delta:
                return d
        return None

if __name__ == "__main__":
    run()
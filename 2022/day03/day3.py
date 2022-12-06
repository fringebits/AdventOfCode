import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(3, "Rucksack Reorganization", os.path.dirname(__file__))
        self.test_answers = [157, 70]
        self.answers = [7701, 2644]

    def run_part1(self):
        score = 0
        for line in self.input:
            half = len(line) >> 1
            firstpart, secondpart = line[:half], line[half:]
            common = list(set(firstpart) & set(secondpart))
            #print(f"common = {common}")
            score += self.score_letter(common[0])
        return score

    def run_part2(self):
        score = 0
        for ii in range(int(len(self.input) / 3)):
            a = self.input[ii*3]
            b = self.input[ii*3+1]
            c = self.input[ii*3+2]
            common = list(set(a) & set(b) & set(c))
            #print(f"common = {common}")
            score += self.score_letter(common[0])
        return score
        
    def score_letter(self, letter):
        value = ord(letter)
        if (value <= ord('Z')):
            return value - ord('A') + 1 + 26
        return value - ord('a') + 1

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()
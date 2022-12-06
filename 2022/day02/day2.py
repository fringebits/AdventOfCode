import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

## rock    A X 1
## scisors B Y 2
## paper   C Z 3
## 0 = loss, 3 = draw, 6 = win

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(2, "Rock Paper Scissors", os.path.dirname(__file__))
        self.test_answers = [15, 12]
        self.answers = [9651, 10560]

    def run_part1(self):
        score = 0
        score_matrix = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
        for line in self.input:
            score += self.score(line, score_matrix)
        return score

    def run_part2(self):
        score = 0
        score_matrix = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
        for line in self.input:
            score += self.score(line, score_matrix)
        return score

    def score(self, line, score_matrix):
        movemap = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}
        moves = line.split(' ')
        row = movemap[moves[0]]
        col = movemap[moves[1]]
        ret = score_matrix[row][col]
        return ret
        
@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()
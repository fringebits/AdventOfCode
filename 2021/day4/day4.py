import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils
import re

@utils.timer
def run():
    print("\n***** Day 4 *****")

    input, cards = load_input('sample_input.txt')
    input, cards = load_input('input.txt')

    # part 1:
    run_part1(input, cards)

    # Reset all the cards (for sanity)        
    [card.Reset() for card in cards]

    # part 2:
    run_part2(input, cards)

def run_part1(input, cards):
    "Part 1: Find first winning bingo card"
    for num in input:
        # mark all cards with specified input
        for card in cards:
            if card.MarkCard(num):
                # this card is a winner
                score = card.ComputeScore()
                print("Part1: lastNum = {0}, score = {1}, totalScore = {2}".format(num, score, num * score))
                return # break/return on the FIRST winning bingo card we find
    assert False, "Failed to find a winning card"
    
def run_part2(input, cards):
    "Part 2: Find last winning bingo card"
    for num in input:
        winner = False

        # mark all cards with specified input
        for card in cards:
            if card.MarkCard(num): 
                winner = True
        
        #if there was a winner
        if winner:
            if len(cards) == 1: # it was the last and only winner
                score = card.ComputeScore()
                print("Part2: lastNum = {0}, score = {1}, totalScore = {2}".format(num, score, num * score))
                return
            # otherwise, filter out all the cards where we have a winner
            cards = [c for c in cards if c.IsBingo() is False]
    assert False, "Failed to find the last winning card"

def load_input(filename):
    nums = []
    cards = []

    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()

    # parse the input numbers
    nums = list(map(int, input[0].split(',')))
    for ii in range(2, len(input), 6):
        cards.append(Card(input[ii:ii+5]))

    return nums, cards

class Card:
    # A single bingo card is
    #   Array of 25 integers (the bingo card itself)
    #   Array of 25 marks (1 = empty spot, 0 = marked spot) [this makes computing score easier]
    def __init__(self, lines):
        "Create new bingo card from lines of input."
        assert len(lines) == 5
        # input must be 5 lines, 5 numbers on each line (todo, figure out how to assert this??)
        # Card will be comprised of an an array of array of integers
        self.card = []
        self.marks = [1] * 25
        for line in lines:
            row = list(map(int, re.split(r"\s+", line)))
            self.card += row
        assert len(self.card) == 25

    def Reset(self):
        "Clear the bingo card!"
        self.marks = [1] * 25

    def MarkCard(self, num):
        "Find the specified num on the card, set the corresponding spot in the array of marks"
        try:
            pos = self.card.index(num)
            self.marks[pos] = 0
            #note: optimization would be to only check impacted row/col when marking this card
            return self.IsBingo()
        except ValueError:
            return False

    def IsBingo(self):
        # Data is stored by row; we look at 0..4, 5..9, etc.
        for ii in range(0, 5):
            row = self.marks[ii*5 : ii*5+5]
            col = self.marks[ ii : 25 : 5]
            if sum(row)==0 or sum(col)==0:
                #self.PrintCard()
                return True     
        return False

    def ComputeScore(self):
        "Score the card by finding sum of all unmarked numbers on the board"
        score = 0
        for box, mark in zip(self.card, self.marks):
            score += box * mark
        return score

    def PrintCard(self):
        "Print the bingo card"
        for ii in range(0, 5):
            m = ["{0:1}".format('*' if v==0 else '') for v in self.marks[ii*5:ii*5+5]]
            row = self.card[ii*5:ii*5+5]
            row = [val for pair in zip(row,m) for val in pair]            
            print("".join(["{:-5}{} "]*5).format(*row))
        print("---")

    def RunTests():
        "Not entirely sure how to organize tests in Python; but this will help test the Card"
        card = Card(['0 2 3 4 5', '6 7 8 9 10', '11 12 13 14 15', '16 17 18 19 20', '21 22 23 24 25'])

        assert card.IsBingo() == False
        assert card.MarkCard(0) == False
        assert card.MarkCard(2) == False
        assert card.MarkCard(3) == False
        assert card.MarkCard(4) == False
        assert card.MarkCard(5) == True
        card.Reset()

        assert card.MarkCard(21) == False
        assert card.MarkCard(22) == False
        assert card.MarkCard(23) == False
        assert card.MarkCard(24) == False
        assert card.MarkCard(25) == True

        card.Reset()
        assert card.MarkCard(0) == False
        assert card.MarkCard(6) == False
        assert card.MarkCard(11) == False
        assert card.MarkCard(16) == False
        assert card.MarkCard(21) == True

        card.Reset()
        assert card.MarkCard(5) == False
        assert card.MarkCard(10) == False
        assert card.MarkCard(15) == False
        assert card.MarkCard(20) == False
        assert card.MarkCard(25) == True

if __name__ == "__main__":
    run()
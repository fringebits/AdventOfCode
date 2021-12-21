import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 21 *****")

    #lines = load_input('sample_input.txt')
    #lines = load_input('input.txt')
    #puzzle = Puzzle(lines)

    puzzle = Board()
    puzzle.AddPlayer(Player(8))
    puzzle.AddPlayer(Player(2))

    # part 1:
    puzzle.PlayGame()
    print(f"Part 1: {puzzle.part1}")

    # part 2:

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Player:
    def __init__(self, pos):
        self.pos = pos-1 # [ 0 .. 9 ]
        self.score = 0
        self.winner = False

    def Move(self, count):
        startPos = self.pos
        self.pos = (self.pos + count) % 10
        self.score += (self.pos + 1)
        print(f"Player rolls {count} and to {self.pos+1}, score={self.score}")

class Die:
    def __init__(self):
        self.value = 0
        self.rollCount = 0

    def RollOnce(self): # returns the value of the 100-sided die
        result = self.value + 1
        self.value = result % 100
        self.rollCount += 1
        return result

    def Roll(self, count): # returns the value of the 100-sided die
        result = 0
        for ii in range(count):
            result += self.RollOnce()
        return result

class Board:
    def __init__(self):
        self.players = []
        self.die = Die()        
        self.PrintBoard()

    def AddPlayer(self, player):
        self.players.append(player)

    def PlayGame(self):
        gameOver = False
        while not gameOver:
            gameOver = self.TakeTurn()

    def TakeTurn(self):
        for p in self.players:
            move = self.die.Roll(3)
            p.Move(move)
            if p.score >= 1000:
                self.part1 = [x.score for x in self.players if x.score < 1000][0] * self.die.rollCount
                return True
        self.PrintBoard()
        return False

    def PrintBoard(self):
        ii = 0
        for p in self.players:
            ii += 1
            print(f"\tPlayer{ii}: pos={p.pos+1}, score={p.score}")

if __name__ == "__main__":
    run()
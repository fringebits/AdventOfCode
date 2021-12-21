import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

@utils.timer
def run():
    print("\n***** Day 21 *****")

    # test input
    #players = [Player(4), Player(8)]

    # official input
    players = [Player(8), Player(2)]

    # part 1:
    game = Game(1000, players, Die(100))
    game.PlayGame()
    print(f"Part 1: {game.part1}")

    # part 2:
    print(f"Part 2: INCOMPLETE")

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
    def __init__(self, faces = 100):
        self.faces = faces
        self.value = 0
        self.rollCount = 0

    def RollOnce(self): # returns the value of the 100-sided die
        result = self.value + 1
        self.value = result % self.faces
        self.rollCount += 1
        return result

    def Roll(self, count = 3): # returns the value of the 100-sided die
        result = 0
        for ii in range(count):
            result += self.RollOnce()
        return result

class Game:
    def __init__(self, max_score, players, die = Die()):
        self.max_score = max_score
        self.players = players.copy()
        self.die = die
        self.PrintBoard()

    def PlayGame(self):
        gameOver = False
        while not gameOver:
            gameOver = self.TakeTurn()

    def TakeTurn(self):
        for p in self.players:
            move = self.die.Roll()
            p.Move(move)
            if p.score >= self.max_score:
                losers = [x.score for x in self.players if x.score < self.max_score]
                self.part1 = losers[0] * self.die.rollCount if (len(losers) > 0) else 0
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
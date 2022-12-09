import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class TreeMap(utils.HeightMap):
    def __init__(self, input):
        super().__init__(input)
        #print(f'TreeMap: \n{self}')

    def is_visible(self, row, col):
        if row == 0 or row == self.height-1:
            return True 
        if col == 0 or col == self.width-1:
            return True

        h = self.get(row, col)
        row_data = self.get_row(row)
        if h > max(row_data[0:col]):
            return True
        if h > max(row_data[col+1:]):
            return True
        
        col_data = self.get_col(col)
        if h > max(col_data[0:row]):
            return True
        if h > max(col_data[row+1:]):
            return True

        return False

    def count_visible(self, pos, delta):
        h = self.GetValueAt(pos)
        count = 0
        pos += delta
        while self.contains(pos):
            r = self.GetValueAt(pos)
            count += 1
            if r >= h:
                break
            pos += delta
        return count

    def get_scenic_score(self, row, col):
        h = self.get(row, col)

        pos = utils.Vec2(col, row)

        left = self.count_visible(pos, utils.Vec2(-1, 0))
        right = self.count_visible(pos, utils.Vec2(1, 0))
        up = self.count_visible(pos, utils.Vec2(0, -1))
        down = self.count_visible(pos, utils.Vec2(0, 1))

        return left * right * up * down       

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(8, "Tuning Trouble", os.path.dirname(__file__))
        self.test_answers = [21, 8]
        self.answers = [1647, 392080]

    def run_part1(self):
        trees = TreeMap(self.input)
        vismap = utils.Grid(trees.width, trees.height, '.')

        count = 0 ## 2 * map.width + 2 * map.height - 4
        for rr in range(trees.width):
            for cc in range(trees.height):
                if trees.is_visible(rr, cc):
                    vismap.set(rr, cc, f'{trees.get(rr, cc)}')
                    count += 1
        #print(f'{vismap}')
        return count

    def run_part2(self):
        trees = TreeMap(self.input)
        map = utils.Grid(trees.width, trees.height, 0)

        #assert 8 == trees.get_scenic_score(3, 2)

        for rr in range(map.width):
            for cc in range(map.height):
                val = trees.get_scenic_score(rr, cc)
                map.set(rr, cc, val)
        #print(f'{map}')
        return max(map.data)

@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()
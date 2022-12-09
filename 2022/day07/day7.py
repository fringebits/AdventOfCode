import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

class Item:
    def __init__(self, name):
        self.name = name
        self.children = []

    def print_tree(self, depth=0):
        print(f'{"".ljust(depth*4)}{self} [total_size={self.get_size()}]')
        for child in self.children:
            child.print_tree(depth + 1)

    def get_size(self):
        assert False, 'Needs to be implemented by sub-classes'

    def walk_tree(self, func):
        result = []
        if func(self):
            result.append(self)
        for child in self.children:
            result += child.walk_tree(func)
        return result

class File(Item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = int(size)

    def __str__(self):
        return f'{self.name} {self.size}'

    def get_size(self):
        return self.size

class Path(Item):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent

    def __str__(self):
        return f'{self.name}  tot=[{self.get_size()}]'

    def get_size(self):
        sizes = [x.get_size() for x in self.children]
        return sum(sizes)

    def change_dir(self, name):
        if name == '..':
            return self.parent
        matches = [x for x in self.children if (x.name == name) and (type(x) == type(self))]
        assert len(matches) == 1, f'No single match in change_dir({name}) from cwd={self.name}.\n{self.children}'
        return matches[0]

class Puzzle(utils.PuzzleBase):
    def __init__(self):
        super().__init__(7, "No Space Left On Device", os.path.dirname(__file__))
        self.answers = [None, None]

    def parse_input(self):
        re_path = re.compile('dir (.*)') ## begin of 'list directory'
        re_file = re.compile('(\d+) (.*)') ## size, name
        re_cd = re.compile('^\$ cd (.*)') ## (relative) name

        self.root = Path('/', None)
        cwd = self.root

        for line in self.input:
            if line == '$ ls': # we're about to start populating CWD
                continue

            match = re_file.match(line)
            if match is not None:
                cwd.children.append(File(match.group(2), match.group(1)))
                continue

            match = re_path.match(line)
            if match is not None:
                cwd.children.append(Path(match.group(1), cwd))
                continue

            match = re_cd.match(line)
            if match is not None:
                path = match.group(1)
                if path == '/':
                    cwd = self.root
                else:
                    cwd = cwd.change_dir(path)
                continue

        #self.root.print_tree()

    def part1_condition(item):
        if not isinstance(item, Path):
            return False
        if item.get_size() <= 100000:
            return True
        return False

    def part2_condition(item):
        if not isinstance(item, Path):
            return False
        return True

    def run_part1(self):
        result = self.root.walk_tree(Puzzle.part1_condition)
        score = sum([x.get_size() for x in result])
        return score

    def get_size(item):
        return item.get_size()

    def run_part2(self):
        total_space = 70000000
        required_space = 30000000
        unused_space = total_space - self.root.get_size()

        free_space = required_space - unused_space
        paths = self.root.walk_tree(Puzzle.part2_condition)
        paths.sort(key=Puzzle.get_size)
        for item in paths:
            if item.get_size() >= free_space:
                result = item
                break

        return result.get_size()


@utils.timer
def run():
    Puzzle().run()

if __name__ == "__main__":
    run()
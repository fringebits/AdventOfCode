import os
import importlib
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re

def main():
    puzzles = Puzzle.FindPuzzles()
    for p in puzzles:
        p.Run()

class Puzzle:
    def __init__(self, pathname, filename):
        self.path = pathname
        self.file = filename

    def Run(self):
        _key = os.path.basename(self.path)
        _file = os.path.splitext(self.file)[0]
        try:
            _module = importlib.import_module(_key+"."+_file)
            _module.run()
        except ImportError:
            print("Failed to import " + _key)

    def FindPuzzles():
        basepath = os.path.dirname(__file__)
        paths = os.listdir(basepath)
        result = []
        dayex = re.compile("day(\d+)")

        for path in paths:
            print("Found " + path)
            match = dayex.match(path)
            if match is not None:
                index = int(match.group(1))
                pathname = os.path.join(basepath, path)
                filename = "day{0}.py".format(index)
                target = os.path.join(pathname, filename)
                if os.path.exists(target):
                    result.append(Puzzle(pathname, filename))            
        return result

if __name__ == "__main__":
    main()
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
        self.root = os.curdir

    def Run(self):
        _key = os.path.basename(self.path)
        _file = os.path.splitext(self.file)[0]
        original_path = os.getcwd()
        try:
            _module = importlib.import_module(_key+"."+_file)
            _module.main()

        except ImportError:
            print(f"Failed to import {os.getcwd()} {_key}.{_file}")

        finally:
            os.chdir(self.root)

    def FindPuzzles():
        basepath = os.path.dirname(__file__)
        paths = os.listdir(basepath)
        result = []
        re_year = re.compile("(\d+)")

        for path in paths:
            #print("Found " + path)
            match = re_year.match(path)
            if match is not None:
                index = int(match.group(1))
                pathname = os.path.join(basepath, path)
                filename = "run.py".format(index)
                target = os.path.join(pathname, filename)
                if os.path.exists(target):
                    result.append(Puzzle(pathname, filename))            
        return result

if __name__ == "__main__":
    main()
import os
import importlib.util
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re

class Runner:
    def __init__(self, year, basepath):
        self.puzzles = []
        self.basepath = basepath

        print(f"\n\n***** https://adventofcode.com/{year} *****")
        print("*****************************************")

    def RunPuzzles(self):
        for p in self.puzzles:
            self.Run(p)

    def Run(self, p):
        path = p[0]
        file = p[1]
        _key = os.path.basename(file)
        _file = os.path.splitext(path)[0]
        try:
            module_name = f'{_key}.{_file}'
            fullpath = os.path.join(path, file)
            _spec = importlib.util.spec_from_file_location(module_name, fullpath)
            _module = importlib.util.module_from_spec(_spec)
            #sys.modules[module_name] = _module
            _spec.loader.exec_module(_module)
            _module.run()
        except ImportError:
            print(f"Failed to import cwd='{os.getcwd()}', path='{path}' {module_name}")

    def FindPuzzles(self):
        paths = os.listdir(self.basepath)
        result = []
        dayex = re.compile("day(\d+)")

        for path in paths:
            #print("Found " + path)
            match = dayex.match(path)
            if match is not None:
                index = int(match.group(1))
                pathname = os.path.join(self.basepath, path)
                filename = "day{0}.py".format(index)
                target = os.path.join(pathname, filename)
                if os.path.exists(target):
                    result.append([pathname, filename])
        self.puzzles = result

if __name__ == "__main__":
    main()
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils.runner

def main():
    runner = utils.runner.Runner('2021', os.path.dirname(__file__))
    runner.FindPuzzles()
    runner.RunPuzzles()

if __name__ == "__main__":
    main()
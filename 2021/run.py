import os
import importlib
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import utils

def main():
    modules = find_modules()
    for path in modules:
        _key = os.path.basename(path)
        #print("Found module " + _key)
        try:
            _mod = importlib.import_module(_key+"."+_key)
            _mod.run()

        except ImportError:
            print("Failed to import " + _key)

def find_modules():
    basepath = os.path.dirname(__file__)
    paths = os.listdir(basepath)
    result = []
    for path in paths:
        #print("Found " + path)
        fullpath = os.path.join(basepath, path)
        target = os.path.join(fullpath, path+".py")
        if os.path.exists(target):
            result.append(fullpath)            
    return result

if __name__ == "__main__":
    main()
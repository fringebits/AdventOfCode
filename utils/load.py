import os

def load_input(path, filename):
    f = open(os.path.join(os.path.dirname(path), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input
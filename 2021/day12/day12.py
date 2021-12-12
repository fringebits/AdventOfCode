import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

from collections import defaultdict

@utils.timer
def run():
    print("\n***** Day 12 *****")

    input = load_input('test_input.txt')
    #input = load_input('sample_input.txt')
    #input = load_input('input.txt')

    graph = Graph(input)

    # part 1:
    run_part1(graph)

    # part 2:
    run_part2(graph)

def run_part1(graph):
    # part1:
    count = graph.CountPaths("start", "end")
    print("part1: path count = {0}".format(count))

def run_part2(map):
    # part2: run simulation until all flash at the same time
    ""
    #print("part2: all flash on step = {0}".format(count))

def load_input(filename):
    f = open(os.path.join(os.path.dirname(__file__), filename), 'r')            
    input = [line.strip() for line in f]
    f.close()
    return input

class Graph:
    def __init__(self, input):
        self.graph = defaultdict(list)
        for line in input:
            head,tail = line.split('-')
            self.graph[head].append(tail)
            self.graph[tail].append(head) # this helps make it bi-directional

    def CountPaths(self, head, tail):
        #visited = defaultdict(int)
        visited = set()
        count = self.Traverse(head, tail, visited)
        return count

    def Traverse(self, node_a, node_b, visited):
        print("Traverse {0}, visited=[{1}]".format(node_a, visited))
        count = 0 # number of paths (we'll return this)
        visited.add(node_a)
        if node_a == node_b:
            # we reached our destination
            count = 1
        else:
            # look at all the notes connected to node_a
            for n in self.graph[node_a]:
                if self.CanVisit(n, visited):
                    #print("\tTraversing {0}".format(n))
                    count += self.Traverse(n, node_b, visited)
        visited.discard(node_a)
        return count

    def CanVisit(self, node, visited):
        if node not in visited:
            return True
        elif node == 'start' or node == 'end':
            return False
        elif node[0].isupper():
            return True
        return False
        #return visited[node] <= 1

if __name__ == "__main__":
    run()
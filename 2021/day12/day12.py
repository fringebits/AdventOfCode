import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import utils

from collections import defaultdict, Counter

@utils.timer
def run():
    print("\n***** Day 12 *****")

    #input = load_input('test_input.txt')
    #input = load_input('sample_input.txt')
    input = load_input('input.txt')

    graph = Graph(input)

    # part 1:
    run_part1(graph)

    # part 2:
    run_part2(graph)

def run_part1(graph):
    # part1: we can revisit large caves as many times as we want
    count = graph.CountPaths("start", "end", Graph.CanVisit_part1)
    print("part1: path count = {0}".format(count))

def run_part2(graph):
    # part2: we can revisit ONE small cave once
    count = graph.CountPaths("start", "end", Graph.CanVisit_part2)
    print("part2: path count = {0}".format(count))

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

    def CountPaths(self, head, tail, func):
        visited = defaultdict(int)
        #self.paths = set() # set of paths (mainly for debug / printing)
        count = self.Traverse(head, tail, visited, func)
        return count

    def Traverse(self, node_a, node_b, visited, func):
        #print("Traverse {0}, visited={1}".format(node_a, visited))
        count = 0 # number of paths (we'll return this)
        visited[node_a] = visited[node_a] + 1

        if node_a == node_b:
            # we reached our destination
            count = 1
        else:
            # look at all the notes connected to node_a
            for n in self.graph[node_a]:
                if func(n, visited):
                    #print("\tTraversing {0}".format(n))
                    count += self.Traverse(n, node_b, visited, func)
        visited[node_a] = visited[node_a] - 1

        return count

    def CanVisit_part1(node, visited):
        if node[0].isupper() or visited[node] == 0:
            return True
        return False

    def CanVisit_part2(node, visited):
        if node == "start":
            return False
        if node[0].isupper():
            return True
        if visited[node] == 0:
            return True

        small_cave_keys = [v for v in visited.keys() if v.islower() and visited[v] > 1]
        if len(small_cave_keys) == 0:
            return True        

        # # note: i need to find a better data structure to track 'visited' for part 2
        # # this is SAF (slow as ...)
        # small_caves = [v for v in visited if v[0].islower()]
        # counter = Counter([v for v in visited if v[0].islower()])
        # if counter[node] < 1:
        #     return True
        # common = counter.most_common()
        # if common[0][1] <= 1:
        #     return True
        return False

if __name__ == "__main__":
    run()
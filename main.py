import heapq
import numpy as np

input = [[0, 7, 9, 0, 0, 14],
         [7, 0, 10, 15, 0, 0],
         [9, 10, 0, 11, 0, 2],
         [0, 15, 11, 0, 6, 0],
         [0, 0, 0, 6, 0, 9],
         [14, 0, 2, 0, 9, 0]]

class Heap:
    def __init__(self, data=[]):
        self.heap = data
        heapq.heapify(self.heap)

    def push(self, val):
        node = Node(val)
        heapq.heappush(self.heap, node)

    def pop(self):
        top = self.top()
        heapq.heappop(self.heap)
        return top
    
    def top(self):
        return self.heap[0]
    
    def empty(self):
        return len(self.heap) == 0

class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, node):
        return self.val[2] < node.val[2]
    
def initHeap ():
    heap = Heap([])
    return heap

def initShortestPath (input):
    sp = dict()
    for i, row_i in enumerate(input):
        sp[i] = np.inf
    sp[0] = 0
    return sp

def initProcessed (input):
    return np.full(np.array(input).shape, False)

def getSrcDestWeight (input, src):
    sources = np.array(input[src])
    dests_pos = np.arange(sources.shape[0])
    dests = dests_pos[sources != 0]
    weights = sources[dests]
    sources = np.full(dests.shape, src)
    tuples = np.array([sources, dests, weights]).T
    return tuples

    
def main (input, target):
    processed = initProcessed(input)
    heap = initHeap()
    sp = initShortestPath(input)

    while(not heap.empty()):
        src, dest, weight = heap.pop().val
        processed[src][dest] = True
        sp[dest] = min(sp[src] + weight, sp[dest])
        dests = getSrcDestWeight(input, dest)
        for d in dests:
            if not processed[d[0]][d[1]]:
                heap.push(d)

    print(sp[target - 1])

main(input, 5)

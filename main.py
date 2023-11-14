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
    
def initHeap (input, processed):
    heap = Heap([])
    for j, col_j in enumerate(input[0]):
        w = input[0][j]
        src = 0
        dest = j
        heap.push((src, dest, w))
    processed[0] = True
    return heap

def initShortestPath (input):
    sp = dict()
    for i, row_i in enumerate(input):
        sp[i] = np.inf
    sp[0] = 0
    return sp

def initProcessed (input):
    return np.full(np.array(input).shape, False)

def getDests (input, src):
    dests_pos = np.arange(input[src])
    dests = dests_pos[input[src] != 0]
    return dests
    
def main (input, target):
    processed = initProcessed(input)
    heap = initHeap(input, processed)
    sp = initShortestPath(input)

    while(not heap.empty()):
        src, dest, weight = heap.pop().val
        if (not processed[src][dest]):
            sp[dest] = min(sp[src] + weight, sp[dest])
            dests = getDests(input, src)
            for d in enumerate(dests):
                heap.push(d)
            processed[src][dest] = True
            print(sp[dest])

    print(sp[target])

main(input, 5)

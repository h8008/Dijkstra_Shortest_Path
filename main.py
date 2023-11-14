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

    def pop(self, val):
        top = self.top()
        heapq.heappop()
        return top
    
    def top(self):
        return self.heap[0]
    
    def empty(self):
        return len(self.heap) == 0

class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, val):
        return self.val[2] < val[2]
    
def initHeap (input):
    heap = Heap([])
    for i, row_i in enumerate(input):
        for j, col_j in enumerate(row_i):
            w = input[i][j]
            src = i
            dest = j
            heap.push((src, dest, w))
    return heap

def initShortestPath (input):
    sp = dict()
    for i, row_i in enumerate(input):
        sp[i] = np.inf

    return sp

def main (input, target):
    heap = initHeap(input)
    sp = initShortestPath(input)

    while(not heap.empty()):
        src, dest, weight = heap.pop()
        sp[dest] = min(sp[src] + weight, sp[dest])

    print(sp[target])

main(input, 5)

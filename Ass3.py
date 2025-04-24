import sys, heapq
from collections import defaultdict
from math import inf

def selectionSort(A):
    U = A.copy()
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    print(f'Selection Sort:\nUnsorted array: {U}\nSorted array: {A}')
    
if __name__ == '__main__':

    A = [64, 25, 12, 22, 11]
    selectionSort(A)

    A = [
        ['A', 2, 100],
        ['B', 1, 19],
        ['C', 2, 27],
        ['D', 1, 25],
        ['E', 3, 15]
    ]
    

    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0,11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9,14, 0, 0, 0],
        [0, 0, 0, 9, 0,10, 0, 0, 0],
        [0, 0, 4,14,10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8,11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]


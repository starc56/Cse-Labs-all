from heapq import *
def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    print( [heappop(h) for i in range(len(h))])

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
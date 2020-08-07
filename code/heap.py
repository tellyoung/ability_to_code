from heapq import *


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


if __name__ == "__main__":
    h = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(h)
    h = []
    heappush(h, (5, 'write code'))
    heappush(h, (7, 'release product'))
    heappush(h, (1, 'write spec'))
    heappush(h, (3, 'create tests'))
    print(len(h))
    print([heappop(h) for i in range(len(h))])

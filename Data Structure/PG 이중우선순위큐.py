import heapq

def solution(operations):
    heap = []

    for o in operations:
        n = o.split()[1]

        if o[0] == "I":
            heapq.heappush(heap, int(n))

        if len(heap) == 0:
            continue
        elif o == "D 1":
            heap.remove(max(heap))
        elif o == "D -1":
            heapq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
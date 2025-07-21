import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._count = 0  # tie‑breaker to preserve insertion order

    def push(self, priority, item):
        # lower priority values come out first
        heapq.heappush(self._heap, (priority, self._count, item))
        self._count += 1

    def pop(self):
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        priority, count, item = heapq.heappop(self._heap)
        return item

    def peek(self):
        if not self._heap:
            raise IndexError("peek from an empty priority queue")
        return self._heap[0][2]

    def __len__(self):
        return len(self._heap)



pq = PriorityQueue()
pq.push(5, "write report")
pq.push(1, "answer emails")
pq.push(3, "prepare slides")

print(pq.peek())   # → "answer emails"
while pq:
    print(pq.pop())
# answer emails, prepare slides, write report


'''

Max heap implementation using reverse priority

'''


class MaxPriorityQueue(PriorityQueue):
    def push(self, priority, item):
        super().push(-priority, item)

    def pop(self):
        item = super().pop()
        return item

max_pq = MaxPriorityQueue()
max_pq.push(10, "high‑urgency task")
max_pq.push(1, "low‑urgency task")

print(max_pq.pop())  # → "high‑urgency task"


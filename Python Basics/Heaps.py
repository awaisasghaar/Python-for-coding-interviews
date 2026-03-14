# Heaps
# We use heap to find min and max value 
import heapq

# Under the hood are arrays
min_Heap = []
heapq.heappush(min_Heap, 4)
heapq.heappush(min_Heap, 3)
heapq.heappush(min_Heap, 2)

# Min is always at 0
print(min_Heap[0])

while len(min_Heap):
    print(heapq.heappop(min_Heap))

# In Puthon there is by default no max heap
# work around is to use min heap and then
# multiply by -1 when push and pop

max_heap = []
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -3)
print(-1 * max_heap[0])

while len(max_heap):
    print(-1 * heapq.heappop(max_heap))

# Build heap from intial values
array = [1, 4, 11, 7, 8, 90, 23]
heapq.heapify(array)
while array:
    print(heapq.heappop(array))


import heapq

# Creating a Min-Heap
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

# Extracting the smallest element
smallest = heapq.heappop(heap)
print("Smallest element:", smallest)
print("Current Heap:", heap)

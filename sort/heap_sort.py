# In all cases (worst, avg, best)
# Time: O(n log n)
# Space: O(1)
# Just use built in heapq module for interviews...

# What is it?
# It's a tree based data structure that helps you find the largestor smallest element - like a priority queue
# min-heap always has the smallest element at the top
# max-heap always has the largest element at the top (can be compared to a VIP line - highest importance gets in first everyone arrives else stays in spot of arrival)

# How's it work?
# tree parent node is always greater or smaller than its children
# insert and remove: O(log n)
# access top element: O(1)

# Interview tip!
# If you need to get the smallest or max element efficiently - use a heap
# heapq is a min-heap by default

import heapq

heap = []

heapq.heapify(heap)

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 45)
heapq.heappush(heap, 23)

print("min-heap: ", [x for x in heap])

# heappop() will move the last element to the root then restore the heap by heapifying down or sifting down
# Time: O(log n)
heapq.heappop(heap)

# [1, 3, 45, 23] 
# popped: [3, 45, 23]
# last comes up front temp [23, 3, 45]
# restore min-heap property [3, 23, 45] (swap the 3 and 23)
# you keep swapping down the tree until the parents are all bigger than the children but order amongst children don't matter

print("min-heap after popping: ", [x for x in heap])

# Get larget and smallest elements from a heapq object
# heappush == O(log n)
new_heap = []

heapq.heapify(new_heap)

heapq.heappush(new_heap, 30)
heapq.heappush(new_heap, 10)
heapq.heappush(new_heap, 60)
heapq.heappush(new_heap, 20)
heapq.heappush(new_heap, 40)
heapq.heappush(new_heap, 80)


print("N-Smallest: ", heapq.nsmallest(3, new_heap))
print("N-Largest: ", heapq.nlargest(3, new_heap))


# You can Push then pop for efficiency
# Gets top element and pushes a new element
print("Push Pop: ", heapq.heappushpop(new_heap, 100))
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)

print("Last element:",queue[len(queue)-1])

print("\nElements dequeued from queue")
print(queue.pop())
print(queue.pop())
print(queue.pop())
print("\nQueue after removing elements")
print(queue)



# Implement a queue data structure.

# A data structure that follows the principle of first-in-first-out.
# Like stacks, they are implemented using arrays or linked lists.

queue = []

# Enqueue: adds a new element to the queue
queue.append(9)
queue.append(8)
queue.append(7)
queue.append(6)
print(f"Queue after enqueue: {queue}")

# Dequeue: removes and returns the first element from the queue.
dequeued = queue.pop(0)
print(f"Dequeued element: {dequeued}")
print(f"Queue after dequeue: {queue}")

# Peek: returns the first element in the queue
peeked = queue[0]
print(f"Peeked element: {peeked}")
print(f"Queue after peek: {queue}")

# isEmpty: checks if the queue is empty
isempty = not bool(queue)
print(f"Is queue empty? {isempty}")

# Size: returns the number of elements in the queue
size = len(queue)
print(f"Size of queue: {size}")

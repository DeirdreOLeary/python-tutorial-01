# Implement a stack data structure.

# A data structure that follows the principle of last-in-first-out.
# Implemented using arrays or linked lists.

stack = []

# Push: Adding new elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(f"Stack after push: {stack}")

# Pop: remove & return the last element from the stack
popped = stack.pop()
print(f"Popped element: {popped}")
print(f"Stack after pop: {stack}")

# Peek: returns the last element from the stack but does not remove it
peeked = stack[-1]
print(f"Peeked element: {peeked}")
print(f"Stack after peek: {stack}")

# isEmpty: checks if the stack is empty
isempty = not bool(stack)
print(f"Is the stack empty? {isempty}")

# Size: returns the number of elements in the stack
size = len(stack)
print(f"Size of stack: {size}")

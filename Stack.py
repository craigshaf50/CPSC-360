class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []
    
    def get_top(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
    
    def print_stack(self):
        print(self._items)
        

stk = Stack()
stk.push(20)
stk.push(5)
stk.push(3)
stk.print_stack()
print(stk.get_top())
# Easy

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack, self.outstack = [], []

    def move(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.instack.append(x)
        return self.instack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        pop_value = self.outstack.pop()
        return pop_value

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.outstack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.instack) and (not self.outstack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

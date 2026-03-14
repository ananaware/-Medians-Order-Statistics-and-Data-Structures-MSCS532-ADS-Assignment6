# ----------------------------------
# STACK IMPLEMENTATION (using array)
# ----------------------------------

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# ----------------------------------
# QUEUE IMPLEMENTATION (using array)
# ----------------------------------

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue Underflow"
        return self.queue.pop(0)

    def display(self):
        print("Queue:", self.queue)


# ----------------------------------
# LINKED LIST IMPLEMENTATION
# ----------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def delete(self, key):

        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next


    def display(self):

        temp = self.head
        result = []

        while temp:
            result.append(temp.data)
            temp = temp.next

        print("Linked List:", result)


# ----------------------------------
# TESTING DATA STRUCTURES
# ----------------------------------

if __name__ == "__main__":

    print("----- STACK TEST -----")

    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()

    print("Popped:", s.pop())
    s.display()


    print("\n----- QUEUE TEST -----")

    q = Queue()
    q.enqueue(5)
    q.enqueue(15)
    q.enqueue(25)
    q.display()

    print("Dequeued:", q.dequeue())
    q.display()


    print("\n----- LINKED LIST TEST -----")

    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.display()

    ll.delete(2)
    ll.display()

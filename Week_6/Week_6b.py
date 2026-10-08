# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Add element to queue
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Remove element from queue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Deleted:", q.dequeue())

print("Queue after dequeue:")
q.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # a. Create a linked list
    def create(self):
        n = int(input("Enter the number of nodes: "))

        for i in range(n):
            data = int(input("Enter the data: "))
            self.insert_end(data)

        print("Linked list created successfully.")

    # b. Insert at beginning
    def insert_beginning(self):
        data = int(input("Enter the data: "))

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        print("Node inserted at beginning.")

    # c. Insert at end
    def insert_end(self, data=None):
        if data is None:
            data = int(input("Enter the data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        if data is not None:
            print("Node inserted at end.")

    # d. Insert at a specific index
    def insert_at_index(self):
        index = int(input("Enter the index: "))
        data = int(input("Enter the data: "))

        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print("Node inserted at index", index)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range.")
                return
            temp = temp.next

        if temp is None:
            print("Index out of range.")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print("Node inserted at index", index)

    # e. Delete by value
    def delete_by_value(self):
        value = int(input("Enter the value to delete: "))

        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted successfully.")
                return
            temp = temp.next

        print("Value not found.")

    # f. Delete first node
    def delete_first(self):
        if self.head is None:
            print("List is empty.")
            return

        self.head = self.head.next
        print("First node deleted.")

    # g. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        print("Last node deleted.")

    # h. Count number of nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # i. Display
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
linked_list = SinglyLinkedList()

while True:
    print("\n----- SINGLY LINKED LIST MENU -----")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count number of nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.create()

    elif choice == 2:
        linked_list.insert_beginning()

    elif choice == 3:
        linked_list.insert_end()

    elif choice == 4:
        linked_list.insert_at_index()

    elif choice == 5:
        linked_list.delete_by_value()

    elif choice == 6:
        linked_list.delete_first()

    elif choice == 7:
        linked_list.delete_last()

    elif choice == 8:
        linked_list.count_nodes()

    elif choice == 9:
        linked_list.display()

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")

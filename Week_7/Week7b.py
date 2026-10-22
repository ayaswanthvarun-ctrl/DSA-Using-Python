class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None

def insert(x):
    global root
    new = Node(x)

    if root is None:
        root = new
        print("Inserted successfully")
        return

    q = [root]
    while q:
        temp = q.pop(0)

        if temp.left is None:
            temp.left = new
            break
        else:
            q.append(temp.left)

        if temp.right is None:
            temp.right = new
            break
        else:
            q.append(temp.right)

    print("Inserted successfully")

def search(x):
    if root is None:
        print("Tree is empty")
        return

    q = [root]
    while q:
        temp = q.pop(0)

        if temp.data == x:
            print("Element found")
            return

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    print("Element not found")

def delete(x):
    global root
    if root is None:
        print("Tree is empty")
        return

    q = [(root, None)]
    target = None
    last = None
    parent = None

    while q:
        temp, par = q.pop(0)

        if temp.data == x and target is None:
            target = temp

        last = temp
        parent = par

        if temp.left:
            q.append((temp.left, temp))
        if temp.right:
            q.append((temp.right, temp))

    if target is None:
        print("Element not found")
        return

    target.data = last.data

    if parent is None:
        root = None
    elif parent.right == last:
        parent.right = None
    else:
        parent.left = None

    print("Deleted successfully")

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

def display():
    if root is None:
        print("Tree is empty")
        return

    q = [root]
    while q:
        temp = q.pop(0)
        print(temp.data, end=" ")

        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    print()

while True:
    print("\n1.Insert 2.Delete 3.Search")
    print("4.Inorder 5.Preorder 6.Postorder")
    print("7.Display 8.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        insert(x)
    elif ch == 2:
        x = int(input("Enter value to delete: "))
        delete(x)
    elif ch == 3:
        x = int(input("Enter value to search: "))
        search(x)
    elif ch == 4:
        inorder(root)
        print()
    elif ch == 5:
        preorder(root)
        print()
    elif ch == 6:
        postorder(root)
        print()
    elif ch == 7:
        display()
    elif ch == 8:
        break
    else:
        print("Invalid choice")

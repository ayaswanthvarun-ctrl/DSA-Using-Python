tree = [None] * 100
n = 0

def insert(x):
    global n
    if n == 100:
        print("Tree is full")
    else:
        tree[n] = x
        n += 1
        print("Inserted successfully")

def delete(x):
    global n
    if n == 0:
        print("Tree is empty")
        return

    if x not in tree[:n]:
        print("Element not found")
        return

    i = tree.index(x)
    tree[i] = tree[n - 1]
    tree[n - 1] = None
    n -= 1
    print("Deleted successfully")

def search(x):
    if x in tree[:n]:
        print("Element found at index", tree.index(x))
    else:
        print("Element not found")

def inorder(i):
    if i < n:
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)

def preorder(i):
    if i < n:
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)

def postorder(i):
    if i < n:
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")

def display():
    if n == 0:
        print("Tree is empty")
    else:
        for i in range(n):
            print(i, ":", tree[i])

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
        inorder(0)
        print()
    elif ch == 5:
        preorder(0)
        print()
    elif ch == 6:
        postorder(0)
        print()
    elif ch == 7:
        display()
    elif ch == 8:
        break
    else:
        print("Invalid choice")

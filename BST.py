
class Node:
    def __init__(self, v):
        self.v, self.l, self.r = v, None, None

def insert(root, v):
    if not root: return Node(v)
    if v < root.v: root.l = insert(root.l, v)
    elif v > root.v: root.r = insert(root.r, v)
    return root

def inorder(n):
    if n: inorder(n.l); print(n.v, end=" "); inorder(n.r)

def preorder(n):
    if n: print(n.v, end=" "); preorder(n.l); preorder(n.r)

def postorder(n):
    if n: postorder(n.l); postorder(n.r); print(n.v, end=" ")

def sideways(n, d=0):
    if n:
        sideways(n.r, d+1)
        print("    "*d + str(n.v))
        sideways(n.l, d+1)

def search(n, v):
    if not n or n.v == v: return n
    return search(n.l if v < n.v else n.r, v)

def level_order(root):
    q = [root]
    level = 0
    while q:
        print(f"Level {level}:", end=" ")
        for _ in range(len(q)):
            n = q.pop(0)
            print(n.v, end=" ")
            if n.l: q.append(n.l)
            if n.r: q.append(n.r)
        print()
        level += 1

a = list(map(int, input("Enter numbers: ").split()))
root = None
for x in a: root = insert(root, x)

print("\nSideways Tree:")
sideways(root)
print("\nLevel Order:")
level_order(root)

for name, f in [("Inorder", inorder), ("Preorder", preorder), ("Postorder", postorder)]:
    print(name + ":", end=" ")
    f(root)
    print()

v = int(input("\nEnter value to search: "))
print("Element found!" if search(root, v) else "Element not found!")

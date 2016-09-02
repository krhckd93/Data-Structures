class Node:
    def __init__(self, value, lchild=None, rchild=None):
        self.lchild = lchild
        self.rchild = rchild
        self.value = value

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_lchild(self, lchild):
        self.lchild = lchild

    def set_rchild(self, rchild):
        self.rchild = rchild


def inorder(root):
    if root is None:
        return
    inorder(root.lchild)
    print(root.value)
    inorder(root.rchild)


def preorder(root):
    if root is None:
        return
    print(root.value)
    preorder(root.lvalue)
    preorder(root.rvalue)


def postorder(root):
    if root is None:
        return
    postorder(root.lchild)
    postorder(root.rchild)
    print(root.value)


def it_preorder(root):
    cur = root
    s = []
    top = -1
    while 1:
        while cur is not None:
            print(cur)
            s.append(cur.value)
            top += 1
            cur = cur.lchild
        if top != -1:
            cur = s.pop()
            top -= 1
            cur = cur.rchild
        else:
            return


def it_inorder(root):
    s = []
    top = -1
    cur = root
    while 1:
        while cur is not None:
            s.append(cur)
            top += 1
            cur = cur.lchild

        if top != -1:
            cur = s.pop()
            top -= 1
            print(cur.value)
            cur = cur.rchild
        else:
            return

l12 = Node(10)
l11 = Node(15)
l1 = Node(4, l11, l12)
r11 = Node(14)
r12 = Node(18)
r1 = Node(50, r11, r12)
root = Node(5, l1, r1)
it_preorder(root)


def main():
    # root = Node(5)
    while 1:
        print("1. Create new tree.\t2.Add a node\t3.Delete a node\t")
        print("4.Display Inorder\t5.Display Preorder\6.Display Postorder")
        print("7.Exit")
        choice = int(input("Enter choice:"))

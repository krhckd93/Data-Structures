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


def it_postorder(root):
    s = []
    flag = []
    top = -1
    if root is None:
        print("Tree is empty!")
        return

    cur = root

    while 1:
        while cur is not None:
            s.append(cur)
            flag.append(int(1))
            top += 1
            cur = cur.lchild

        while flag[top] == -1:
            cur = s.pop()
            flag.pop()
            top -= 1
            print(cur.value)

            if top == -1:
                return

        if top != -1:
            cur = s[top]
            cur = cur.rchild
            flag[top] = int(-1)




def get_index(inorder, target):
    for i in range(0, len(inorder)):
        if int(inorder[i]) == int(target):
            return i


def build_in_pre(preorder, inorder, start, end, ind_pre):
    if start > end:
        return None
    else:
        ind_in = get_index(inorder, preorder[ind_pre])
        root = Node(inorder[ind_in])
        ind_pre += 1
        root.lchild = build_in_pre(preorder, inorder, start, ind_in-1, ind_pre)
        root.rchild = build_in_pre(preorder, inorder, ind_in+1, end, ind_pre)
        return root

# in_preorder = input("Enter the preorder sequence").split(',')
# in_postorder = input("Enter the postorder sequence").split(',')
# in_inorder = input("Enter the inorder sequence").split(',')
# a = build_in_pre(in_preorder, in_inorder, 0, len(in_inorder), 0)

l12 = Node(10)
l11 = Node(15)
l1 = Node(4, l11, l12)
r11 = Node(14)
r12 = Node(18)
r1 = Node(50, r11, r12)
root = Node(5, l1, r1)
it_postorder(root)

'''
def main():
    # root = Node(5)
    while 1:
        print("1. Create new tree.\t2.Add a node\t3.Delete a node\t")
        print("4.Display Inorder\t5.Display Preorder\6.Display Postorder")
        print("7.Exit")
        choice = int(input("Enter choice:"))
'''
'''
To-do:
    Unchecked:
        Create a tree from user string.
        Create a tree from preorder, inorder and postorder sequences.
        Create a user interface.
    Checked:
        Iterative traversal.
        Recursive traversal.
'''


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
            print(cur.value)
            s.append(cur)
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
            flag[top] = int(-1)
            cur = cur.rchild


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


def build_in_post(start_in, end_in, start_post, end_post, inorder, postorder):
    if start_in > end_in or start_post > end_post:
        return None
    root = Node(postorder[end_post])
    root_in_index = get_index(inorder, root.value)

    root.lchild = build_in_post(start_in, root_in_index-1, start_post, start_post + root_in_index - start_in - 1, inorder, postorder)
    root.rchild = build_in_post(root_in_index+1, end_in, start_post + root_in_index - start_in, end_post-1, inorder, postorder)

    return root

def tree_to_linked_list(root):
    if root is None:
        return root
    cur = root
    s = []
    top = -1
    while 1:
        while cur is not None:
            s.append(cur)
            top += 1
            cur = cur.lchild
        if top == -1:
            return root
        else:
            cur = s.pop()
            top -= 1
            #print(cur.value)
            if cur.rchild is not None:
                cur.lchild = cur.rchild
            else:
                temp = cur
                if top != -1:
                    cur = s.pop()
                    top -= 1
                    temp.lchild = cur.rchild
                else:
                    return root
            temp = cur.rchild
            cur.rchild = None
            cur = temp


# in_preorder = input("Enter the preorder sequence").split(',')
#in_postorder, = input("Enter the postorder sequence").split('')
#in_inorder = input("Enter the inorder sequence").split(',')
in_postorder = [15, 17, 12, 14, 20, 13, 10]
in_inorder = [15, 12, 17, 10, 14, 13, 20]
a = build_in_post(0, len(in_inorder)-1, 0, len(in_postorder)-1, in_inorder, in_postorder)
it_preorder(a)
print("tree created.")
a = tree_to_linked_list(a)
cur = a
while cur is not None :
    print(cur.value)
    cur = cur.lchild




'''l12 = Node(10)
l11 = Node(15)
l1 = Node(4, l11, l12)
r11 = Node(14)
r12 = Node(18)
r1 = Node(50, r11, r12)
root = Node(5, l1, r1)
it_postorder(root)'''

'''
def main():
    # root = Node(5)
    while 1:
        print("1. Create new tree.\t2.Add a node\t3.Delete a node\t")
        print("4.Display Inorder\t5.Display Preorder\6.Display Postorder")
        print("7.Exit")
        choice = int(input("Enter choice:"))
'''


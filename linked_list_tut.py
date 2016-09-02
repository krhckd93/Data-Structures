class Node:
    def __init__(self, content = None, next=None):
        self.content = content
        self.next = next

    def get_content(self):
        return self.content

    def __str__(self):
        return str(self.content)


def display_list(a):
    if a is not None:
        print(a.content)
        temp = a.next
        while temp is not None:
            print(temp.content)
            temp = temp.next
        print()


def add_node(a, node):
    print("Adding ", node.content)
    temp = a
    while temp.next is not None:
        temp = temp.next
    temp.next = node


def delete_node(a):
    if a is not None:
        temp = a.next
        if temp is not None:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            print("a is:")
            display_list(a)

def delete_node_location(a, location):
    temp = a
    while _ in range(0, location-1):
        temp = temp.next
    temp.next = temp.next.next


a = Node(5)
b = Node(10)
a.next = b
display_list(a)
c = Node(15)
add_node(a, c)
display_list(a)
a = delete_node(a)
display_list(a)

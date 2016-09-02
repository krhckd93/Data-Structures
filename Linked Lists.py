class Node:
    def __init__(self, data = -1, node = None):
        self.data = data
        self.next = node

    def update_data(self, data):
        self.data = data


def display(node):
    if node is not None:
        temp = node.next
        print("List :")
        while temp is not None:
            print("->", temp.data),
            temp = temp.next
    else:
        print("List is EMPTY! Try adding a few nodes first.")




def main():
    print("Menu:\n1.New List\t2.Add a node at the head.\n3. Add a node at the end.\n4.Delete a node given the data.")
    print("\n5. Delete a node at the head.\t6. Delete a node at the end.\n7.Print the list.\n8. BREAK!")
    print("\nNote: This program is for a single linked list, singly linked or doubly linked.")
    print("Enter you choice:")
    choice = int(input())
    node = Node()

    while choice != 8:

        if choice == 1:
            node = Node(int(input("Enter data :")), None)
            print("Node list created. Node.data=", node.data)

        elif choice == 2:
            if node is not None:
                temp = Node(int(input("Enter data : ")),node.next)
                node.next = temp
            else:
                print("List is EMPTY! Try adding a few nodes first.")

        elif choice == 3:
            print()
        elif choice == 4:
            print()
        elif choice == 5:
            print()
        elif choice == 6:
            print()
        elif choice == 7:
            display(node)

    print("Enter your choice:")
    choice = int(input())

main()
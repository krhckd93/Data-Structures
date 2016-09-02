def display(s, top):
    if top == -1:
        print("Stack is empty!")
    else:
        while top != -1:
            print(s[top])


def push_item(s, top, max_size, value):
    if top != max_size:
        top += 1
        s.append(value)
        print("Item added :", s[top])
        return top
    else:
        print("Stack is full. Try popping some elements first.")
        return top


def pop_item(s, top):
    if top != -1:
        temp = s.pop()
        top -= 1
        print("Item popped is ", temp)
        return top
    else:
        print("Stack is empty! Try adding some items first.")
        return top


def main():
    s = []
    top = -1
    while 1:
        print("1.Create a new stack\t2.Add\t3.Delete\t4.Display\t5.Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            if max_size is not None:
                ans = input("Stack exists. Do you want to create a new one?")
                if ans == 'y' or ans == 'Y':
                    max_size = int(input("Enter the maximum size of the stack:"))
                    value = int(input("Enter a value:"))
                    top = push_item(s, top, max_size, value)
                    continue
                else:
                    continue
            max_size = int(input("Enter the maximum size of the stack:"))
            value = int(input("Enter a value:"))
            top = push_item(s, top, max_size, value)

        elif choice == 2:
            if top == -1:
                print("Create a stack first.")
                continue
            value = int(input("Enter a value:"))
            top = push_item(s, top, max_size, value)

        elif choice == 3:
            top = pop_item(s, top)
            print()

        elif choice == 4:
            display(s, top)

        elif choice == 5:
            exit()

main()

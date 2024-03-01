# STACK IMPLEMENTATION USING ARRAYS
stack = []


def push(data):
    stack.append(data)


def traverse():
    for i in stack:
        print(i)


def is_empty():
    if len(stack) == 0:
        print("the stack is empty")
    else:
        print("the stack is not empty")


def peek():
    print(f"the peek element of the stack is {stack[-1]}")


def sizeofstack():
    print(f"the size of the stack is {len(stack)}")

    #    STACK IMPLEMENTATION USING LINKED LISTS


class node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class stack1:
    def __init__(self):
        self.top = None
        self.size = 0

    def traverse(self):
        if self.top is None:
            print("the stack is empty")
        else:

            current = self.top
            while current is not None:
                print(current.data)
                current = current.ref

    def push(self, data):
        node1 = node(data)
        node1.ref = self.top
        self.top = node1
        self.size += 1

    def isEmpty(self):
        if self.top is None:
            print("the linked list is empty")
        else:
            print("the stack is not empty")

    def pop(self):
        if self.top is None:
            print("the stack is empty you cant pop item from the stack")
        else:
            popped_item = self.top.data
            self.top = self.top.ref
            self.size -= 1
            return popped_item

    def size1(self):
        print(f"the size of the stack is {self.size}")

    def peek(self):
        if self.top is None:
            print("the stack is empty")
        else:
            print(f"the peek element of the stack is {self.top.data}")

    #     middle of the linked list
    def middle(self):
        if self.size == 0:
            print("the stack is empty")
        else:
            slow = self.top
            fast = self.top
            while fast and fast.ref:
                slow = slow.ref
                fast = fast.ref.ref
            print(f"the middle element is {slow.data}")


l = stack1()
l.push(77)
l.push(76)
l.push(55)
# popped = l.pop()
# print(f"popped = {popped}")
# l.size1()
# l.peek()
# l.isEmpty()
l.middle()



l.traverse()

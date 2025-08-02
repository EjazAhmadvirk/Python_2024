# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Circular Linked List class
class CircularList:
    def __init__(self):
        self.tail = None

    # Push at front
    def push_front(self, val):
        new_node = Node(val)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    # Push at back
    def push_back(self, val):
        new_node = Node(val)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    # Pop from front
    def pop_front(self):
        if not self.tail:
            print("List is empty!")
            return
        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next

    # Pop from back
    def pop_back(self):
        if not self.tail:
            print("List is empty!")
            return
        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            temp = head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.tail.next
            self.tail = temp

    # Display list
    def display(self):
        if not self.tail:
            print("List is empty!")
            return
        temp = self.tail.next
        head = temp
        result = ''
        while True:
            result += str(temp.data) + " -> "
            temp = temp.next
            if temp == head:
                break
        print(result + "(head)")

# Test the Circular Linked List
cll = CircularList()

cll.push_back(10)
cll.push_front(5)
cll.push_back(20)
cll.display()  # 5 -> 10 -> 20 -> (head)

cll.pop_front()
cll.display()  # 10 -> 20 -> (head)

cll.pop_back()
cll.display()  # 10 -> (head)

cll.pop_back()
cll.display()  # List is empty!

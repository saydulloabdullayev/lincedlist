class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def append_list(self, data_list):
        for data in data_list:
            self.append(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Test qismi
if __name__ == "__main__":
    ll = LinkedList()
    my_list = [1, 2, 3, 4, 5]
    ll.append_list(my_list)

    print("Linked list after appending list:")
    ll.print_list()

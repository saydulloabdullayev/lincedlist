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

    def delete_node_at_position(self, position):
        if self.head is None:
            return

        temp = self.head

       
        if position == 0:
            self.head = temp.next
            temp = None
            return


        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return

        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Linked list before deletion:")
    ll.print_list()

    position_to_delete = 2
    ll.delete_node_at_position(position_to_delete)

    print("Linked list after deletion at position", position_to_delete)
    ll.print_list()

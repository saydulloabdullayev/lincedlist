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

    def sum_of_elements(self):
        total_sum = 0
        current = self.head
        while current:
            # Agar element son bo'lsa, uning qiymatini total_sum ga qo'shamiz
            if isinstance(current.data, (int, float)):
                total_sum += current.data
            current = current.next
        return total_sum

# Test qismi
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append("a")
    ll.append(4)
    ll.append("b")
    print("Sum of elements:", ll.sum_of_elements())

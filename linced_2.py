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

    def count_and_sum_of_elements(self):
        count = 0
        total_sum = 0
        current = self.head
        while current:
            if isinstance(current.data, (int, float)):
                total_sum += current.data
                count += 1
            current = current.next
        return count, total_sum

    def average_of_elements(self):
        count, total_sum = self.count_and_sum_of_elements()
        if count == 0:
            return 0  # Agar elementlar son emas bo'lsa, o'rta arifmetigini 0 qaytaramiz
        return total_sum / count

# Test qismi
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append("a")
    ll.append(4)
    ll.append("b")
    print("Average of elements:", ll.average_of_elements())

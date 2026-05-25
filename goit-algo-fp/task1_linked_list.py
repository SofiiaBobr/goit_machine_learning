
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.sorted_merge(left, right)

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def sort(self):
        self.head = self.merge_sort(self.head)

    @staticmethod
    def merge_sorted_lists(list1, list2):
        result = LinkedList()
        result.head = result.sorted_merge(list1.head, list2.head)
        return result


if __name__ == "__main__":
    ll = LinkedList()

    for value in [4, 2, 1, 5, 3]:
        ll.append(value)

    print("Original list:")
    ll.print_list()

    ll.reverse()
    print("Reversed list:")
    ll.print_list()

    ll.sort()
    print("Sorted list:")
    ll.print_list()

    l1 = LinkedList()
    l2 = LinkedList()

    for x in [1, 3, 5]:
        l1.append(x)

    for x in [2, 4, 6]:
        l2.append(x)

    merged = LinkedList.merge_sorted_lists(l1, l2)

    print("Merged sorted lists:")
    merged.print_list()

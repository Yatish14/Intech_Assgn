class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

def create_linked_list():
    elements = input("Enter the elements of the linked list separated by spaces: ").split()
    head = None
    tail = None
    for element in elements:
        new_node = Node(int(element))
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

head = create_linked_list()

print("Middle element :", middle(head))

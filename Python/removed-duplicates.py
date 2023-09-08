class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


# Create a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

# Remove duplicates
new_head = deleteDuplicates(head)

# Print the new linked list
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next

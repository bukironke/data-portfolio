#node - single element in data structure that contains both data and pointer reference

#defines class repping node in single linked list - node-value = val, reference = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    # Removes duplicate nodes from a singly linked list.
    # Traverses the list, adjusting pointers to skip duplicate nodes.
    current = head
    
    while current and current.next:
# Checks for duplicate values in consecutive nodes.
        if current.val == current.next.val:
# Adjusts the pointer to skip the duplicate node.
            current.next = current.next.next
        else:
# Moves to the next node in the linked list.
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

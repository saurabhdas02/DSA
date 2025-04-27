from DSA.LinkedList.main import Node

head = Node(14)
for i in range(13, 2, -1):
    # head.insertAtStart(i)
    head.InsertAtEnd(i)
# for i in range(10, 15):
#     head.InsertAtEnd(i)
# head.printList()
# head.InsertAtEnd(15)
# head.InsertAtIndex(16, 3)
# print("***" * 15)
# head.printList()
# print(head.searchKey(5))
# print(head.searchKey(25))
# print("***" * 15)
# head.printNthFromEnd(4)
# head.printNthFromEndAdvanced(4)

head.printList()
head.printNthFromEnd(1)
"""
Remove Duplicates

head.InsertAtEnd(13)
head.InsertAtEnd(14)
head.InsertAtEnd(14)
head.InsertAtEnd(15)
head.InsertAtEnd(15)
head.InsertAtEnd(15)
head.printList()
print("***" * 15)
head.removeDuplicatesFromSortedLL()
head.reverseLL()
head.printNthElement(7)
head.deleteElement(14)
for i in range(3, 14):
    # head.insertAtStart(i)
    head.InsertAtEnd(i)
head.checkPalindromeLL()
"""

"""
merge 2 linked list
head2 = Node(1)
head1 = Node(0)

for i in range(2, 14, 3):
    # head.insertAtStart(i)
    head1.InsertAtEnd(i)
for i in range(2, 14):
    # head.insertAtStart(i)
    head2.InsertAtEnd(i)

head2.printList()
head1.printList()

Node.merge2LinkedList(head1, head2)
"""


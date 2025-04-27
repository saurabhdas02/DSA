class Node:
    head = None

    def __init__(self, key):
        self.key = key
        self.next = None
        if self.head is None:
            self.head = self

    def insertAtStart(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def deleteFromStart(self, key):
        if self.head is None:
            return None
        else:
            tmp = self.head.next
            self.head = self.head.next
            del tmp

    def InsertAtIndex(self, key, index):
        if index == 0:
            self.insertAtStart(key)
        else:
            new_node = Node(key)
            curr = self.head
            curr_index = 1
            while curr is not None and curr_index < index - 1:
                print(curr.key)
                curr = curr.next
                curr_index += 1

            if curr is not None:
                new_node.next = curr.next
                curr.next = new_node

    def InsertAtEnd(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = new_node

    def searchKey(self, key):
        current = self.head
        index = 1
        while current is not None:
            if current.key == key:
                return index
            index += 1
            current = current.next
        return -1

    def printList(self):
        if self.head is None:
            return "Empty Linked List"
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.key)
                tmp = tmp.next

    def printNthFromEnd(self, index):
        len = 0
        curr = self.head
        while curr:
            curr = curr.next
            len += 1

        if len < index:
            return -1

        curr = self.head
        for i in range(1, len-index+1):
            curr = curr.next
        print(curr.key)

    def printNthFromEndAdvanced(self, index):
        first = self.head
        second = self.head
        for i in range(0, index):
            if first is None:
                return -1
            first = first.next

        while first is not None:
            second = second.next
            first = first.next
        print(second.key)

    def removeDuplicatesFromSortedLL(self):
        curr = self.head
        while curr.next is not None:
            if curr.key == curr.next.key:
                curr.next = curr.next.next
            else:
                curr = curr.next

    def reverseLL(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.printList()

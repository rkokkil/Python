class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def isEmptyList(self):
        if self.head is None or self.head.data == "":
            return True
        else:
            return False

    # Ram -> Babu -> Kokkiligadda
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


    """
    1. IF head is NULL, return -1
    2. Traverse until last node and increment counter
    """
    def listSize(self):
        if self.head is None:
            return -1

        currentNode = self.head
        count = 0
        while currentNode is not None:
            currentNode = currentNode.next
            count += 1

        return count


    def search(self, data):
        if data == "" or data is None:
            print('No element is passed to search')
            return

        currentNode = self.head
        position = 0
        while currentNode is not None:
            # position = position + 1
            if currentNode.data == data:
                break

            currentNode = currentNode.next
            position += 1

        if position > self.listSize()-1:
            print(f'\'{data}\' node is NOT available in the list')
        else:
            print(f'{data} node is available at index {position}')

    """
    1. IF newNode is NULL or empty, THEN return
    2. Assign Head node to newNode's next
    3. Assign newNode to Head
        
    """
    def insertAtHead(self, newNode):
        if newNode is None or newNode.data == "":
            return

        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, newNode):
        """
        1. IF head is NULL
            1.1. Assign newNode to head
        2. IF head is NOT NULL
            2.1. Assign head to temp node
            2.2. Traverse list until last node is not NULL
            2.3. Link new node to last node
        """
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next

            currentNode.next = newNode

    """
    0  1  2  3  4
    1->2->3->4->5->null
    position = 2
    node = 10
    result
    1->2->10->3->4->5->null
    """
    def insertAtPosition(self, node, position):
        if self.head is None:
            return

        currentNode = self.head
        counter = 0
        prevNode = self.head
        while currentNode.next is not None:
            if counter == position:
                node.next = currentNode
                prevNode.next = node
                del currentNode
                break

            prevNode = currentNode
            currentNode = currentNode.next
            counter += 1

    """
    head 
    1->2->3->null
    after 
    2->3->null
    """
    def deleteHead(self):
        if self.head is None:
            return
        currentNode = self.head
        currentNext = currentNode.next
        self.head = currentNext
        del currentNode

    """
    1->2->3->4->5->null
    """
    def deleteAtEnd(self):
        if self.head is None:
            return

        currentNode = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next

        currentNode.next = None

    """
    position = 2
    0  1  2  3  4
    1->2->3->4->5->null
    currentNode = 3
    prevNode = 2
    
    
    """
    def deleteAtPosition(self, position):
        if self.head is None:
            return

        currentNode = self.head
        counter = 0
        prevNode = self.head
        while currentNode.next is not None:
            if counter == position:
                prevNode.next = currentNode.next
                del currentNode
                break

            prevNode = currentNode
            currentNode = currentNode.next
            counter += 1

# Client program or Driver Program

firstNode = Node("Ram")
list = LinkedList()
# print(list.isEmptyList())
# Ram -> Babu -> Kokkiligadda
list.insertAtEnd(firstNode)
secondNode = Node("babu")
list.insertAtEnd(secondNode)
thirdNode = Node("Kokkiligadda")
list.insertAtEnd(thirdNode)
# Mr Ram -> Babu -> Kokkiligadda
fourthNode = Node("Mr")
# fourthNode = Node("")
list.insertAtHead(fourthNode)
# print(list.isEmptyList())

# list.printList()
# print(list.listSize())
# list.search("")
# list.search("Hi")
# list.search("Mr")

list.printList()
# list.deleteHead()
# list.deleteHead()
# list.deleteHead()
# list.deleteHead()
# list.deleteHead()
# list.deleteAtEnd()
# list.deleteAtPosition(2)
fifthNode = Node("Hello")
list.insertAtPosition(fifthNode, 2)
print()
list.printList()

"""
if __name__ == '__main__':
    firstNode = Node()
    
"""

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

    def insertAtPosition(self, node, position):
        pass

    def deleteHead(self):
        pass

    def deleteAtEnd(self):
        pass

    def deleteAtPosition(self, position):
        pass

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
list.search("")
list.search("Hi")
list.search("Mr")

"""
if __name__ == '__main__':
    firstNode = Node()
    
"""

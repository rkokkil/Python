class PurchaseOrder:
    def __init__(self, item_name, quantity, price_per_item, city):
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.city = city

    def __str__(self):
        return f'PurchaseOrder[item_name {self.item_name},' \
               f'quantity {self.quantity},' \
               f'price_per_item {self.price_per_item},' \
               f'city {self.city} ]'


class Node:
    pass

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


firstPurchaseOrder = PurchaseOrder('Vivo1959', 1, 15000, 'Repalle')
firstNode = Node(firstPurchaseOrder)
list = LinkedList()
list.insertAtEnd(firstNode)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def removeFromFront(self):
        if self.head is None:
            return None
        
        removed = self.head
        self.head = self.head.next
        return removed.data

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    
    # This method should insert a new node as the second element in the list.
    def addSecond(self, data):
        #Fill this out! for example for list     
        # running addSecond(10) 
        # 5 ->  3 -> 8 -> None should become 5 -> 10 -> 3 -> 8 -> None
        # if the list is empty: then it becomes  10 -> None
        # if the list has one element like 5 -> None it becomes 5 -> 10 -> None

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head.next
        self.head.next = new_node      
        return
    
    # This method should remove and return the second node in the list.
    def removeSecond(self):
        if self.head is None or self.head.next is None:
            return None
        
        self.head.next = self.head.next.next
        return


    
# after implementing the methods, these should work

ll = LinkedList()

ll.addToFront(8)
ll.addToFront(3)
ll.addToFront(5)

ll.printList()
# # 5 -> 3 -> 8 -> None

ll.addSecond(10)
ll.printList()
# # 5 -> 10 -> 3 -> 8 -> None

print(ll.removeSecond())
# # 10

ll.printList()
# # 5 -> 3 -> 8 -> None


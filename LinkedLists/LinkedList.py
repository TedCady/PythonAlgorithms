class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def addFront(self , value):
        new_node = ListNode(value)
        current_node = self.head
        new_node.next = current_node
        self.head = new_node
        return self
    def addEnd(self,value):
        if self.head == None:
            self.addFront(value)
            return self
        new_node = ListNode(value)
        i = self.head
        while (i.next != None):
            i = i.next
        i.next = new_node
        return self
    def deleteFront(self):
        pass
    def deleteEnd(self):
        pass
    def delete(self,value):
        pass
    def insert(self,value,n):
        pass
    def printNodeList(self):
        i = self.head
        while (i != None):
            print(i.value)
            i=i.next
        print('--------\n')
        return self
list = LinkedList()
list.addFront('5').addFront('4').addFront('3').addEnd('6').addFront('2').addFront('1').printNodeList()
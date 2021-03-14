class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
class SLList:
    def __init__(self):
        self.head = None
    def addToFront(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    def addToBack(self, val):
        if self.head == None:
            self.addToFront(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self
my_list = SLList()
my_list.addToFront('Jim').addToFront('Dwight').addToFront('Andy').addToBack('Pam').print_values()
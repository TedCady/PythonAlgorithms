class UserNode:
    def __init__(self,value):
        self.value = value
        self.next = None
class UserList:
    def __init__(self):
        self.head = None
    def addToFront(self, value):
        new_user = UserNode(value)
        current_node = self.head
        new_user.next = current_node
        self.head = new_user
        return (self)
    def addToBack(self,value):
        if self.head == None:
            self.addToFront
            return self
        new_user = UserNode(value)
        i = self.head
        while (i.next != None):
            i = i.next
        i.next = new_user
        return self
    def allUsers(self):
        i = self.head
        while (i != None):
            print(i.value)
            i = i.next
        return self
user_index = UserList()
user_index.addToFront('Cameron').addToFront('Bill').addToBack('Ted').addToBack('Ben').allUsers()
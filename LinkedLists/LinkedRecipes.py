class RecipeNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class MenuList:
    def __init__(self):
        self.head = None
    def addFront(self, value):
        new_entry = RecipeNode(value)
        current_node = self.head
        new_entry.next = current_node
        self.head = new_entry
        return self
    def addEnd(self, value):
        if self.head == None:
            self.addFront(value)
            return self
        new_entry = RecipeNode(value)
        i = self.head
        while (i.next != None):
            i = i.next
        i.next = new_entry
        return self
    def deleteFront(self):
        if self.head != None:
            self.head = self.head.next
            return self
    def deleteEnd(self):
        if self.head == None:
            return self
        elif self.head.next == None:
            self.head = None
            return self
        else:
            i = self.head
            while i.next.next != None:
                i = i.next
            i.next = None
            return self
    def delete(self, value):
        if self.head == None:
            return self
        elif self.head.value == value:
            self.head = self.head.next
            return self
        else:
            i = self.head
            while (i.next != None and i.next.value != value):
                i = i.next
            if i.next == None:
                return self
            else:
                i.next = i.next.next
                return self
    def insert(self, value, n):
        if self.head == None:
            self.addFront(value)
            return self
        elif self.head != None and self.head.next == None:
            self.addFront(value)
            return self
        else:
            i = self.head
            while (i.next != None and i.next.value != n):
                i = i.next
            else:
                new_entry = RecipeNode(value)
                n = i.next
                i.next = new_entry
                new_entry.next = n
                return self
    def printRecipes(self):
        i = self.head
        while (i != None):
            print(i.value)
            i = i.next
        print('--------------------\n')
        return self
menu = MenuList()
menu.addFront('Buffalo Chicken Sandwich').addFront('Brisket Sandwich').addEnd('Pulled Pork Sandwich').addEnd('Pastrame Sandwich').addEnd('Portobello Caprese Sandwich').addEnd('Crispy Pork Belly Sandwich').addEnd('Pizza').addFront('Wedge Salad').addFront('Ceasar Salad').printRecipes()
menu.insert('Pork Ribs', 'Pulled Pork Sandwich').printRecipes()
menu.delete('Pastrame Sandwich').printRecipes()
menu.deleteEnd().printRecipes()
menu.addEnd('Pastrame Sandwich').printRecipes()
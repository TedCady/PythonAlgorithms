class store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self, objname):
        objname.print_info()
        self.products.remove(objname)
    def inflation(self, percent_changed = 0):
        for product in self.products:
            product.update_price(0, percent_changed, True).print_info()
    def set_clearance(self, category = '', percent_changed = 0):
        for product in self.products:
            product.update_price(category, percent_changed, False).print_info()
    def print_store(self):
        for product in self.products:
            product.print_info()


class product:
    def __init__(self, productID, p_name, cost, category):
        self.productID = productID
        self.p_name = p_name
        self.cost = cost
        self.category = category
    def update_price(self,category, percent_changed, is_increased):
        amount_increased = 0
        amount_decreased = 0
        if is_increased == True:
            amount_increased = self.cost*(percent_changed / 100)
            self.cost += amount_increased
        if is_increased == False and category == self.category:
            amount_decreased = self.cost*(percent_changed / 100)
            self.cost -= amount_decreased
        round(self.cost, 3)
        return self
    def print_info(self):
        print('ID:',self.productID, self.p_name,'$',self.cost,'category:',self.category )
class Item:
    # basically a constructor, gets executed when an instance of the class is created.
    def __init__(self, name, price, qnt=0):
        self.name = name
        self.price = price
        self.quantity = qnt

    def calculate_total_price(self, x, y):
        return x * y


item1 = Item("Phone", 100, 5)

item2 = Item("TV", 550)

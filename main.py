class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    # basically a constructor, gets executed when an instance of the class is created.
    def __init__(self, name: str, price: float, quantity=0):
        # Validate received arguments
        assert price >= 0, f"price {price} should be a positive value"
        assert quantity >= 0, f"quantity {quantity} should be a positive value"

        # assign to self
        self.name = name
        self.price = price
        self.quantity = quantity

        # put the instance inside instances list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self, pay_rate):
        self.price = self.price * pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 15)
item2 = Item("TV", 1200, 7)
item3 = Item("Computer", 700, 4)
item4 = Item("Mouse", 25, 17)

print(Item.all)
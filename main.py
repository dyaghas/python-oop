import csv
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        print(items)
        for i in items:
            Item(
                name=i.get('name'),
                price=float(i.get('price')),
                quantity=int(i.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # .0 floats will be considered integers
        if isinstance(num, float):
            # counts out .0 floats and returns true
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


print(Item.is_integer(15.0))
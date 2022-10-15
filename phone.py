from item import Item


class Phone(Item):
    all = []

    # basically a constructor, gets executed when an instance of the class is created.
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Validate received arguments
        assert broken_phones >= 0, f"broken_phones {broken_phones} can't be a negative value"

        # assign to self
        self.broken_phones = broken_phones

        # put the instance inside instances list
        Phone.all.append(self)
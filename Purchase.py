class Purchase:

    def __init__(self, date, price):
        self.date = date
        self.price = price

    def __str__(self):
        result = self.date.toString() + " - " + "$"+str(self.price)
        return result

    def __repr__(self):
        return self.price

    def __eq__(self, other):
        if (self.title == other.get_title()
        and self.price == other.get_price()):
            return True
        else:
            return False

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

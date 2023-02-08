from payment import Payment

class Cash(Payment):
    def __init__(self, cashTendered, amount):
        super().__init__(amount)
        self.cashTendered = cashTendered
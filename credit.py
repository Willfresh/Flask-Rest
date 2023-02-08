from payment import Payment

class Credit(Payment):
    def __init__(self, number, type, expireDate, amount):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expireDate = expireDate
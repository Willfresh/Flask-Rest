from payment import Payment

class WireTransfer(Payment):
    def __init__(self, bankID, bankName, amount):
        super().__init__(amount)
        self.bankID = bankID
        self.bankName = bankName
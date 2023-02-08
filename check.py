from payment import Payment

class Check(Payment):
    def __init__(self, name, bankID, amount):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID

    def authorized(self):
        # code pour autoriser la verification
        authorized_banks = ["UTB", "Orabank", ""]
        authorized_names = ["John", "Peter"  ]
        
        if self.bankID in authorized_banks and self.name in authorized_names:
            return True
        else:
            return False
        pass
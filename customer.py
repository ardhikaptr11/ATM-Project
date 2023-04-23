class Customer:

    def __init__(self, id_, custPin='123456', custBalance=100_000):
        self.id = id_
        self.balance = custBalance
        self.custPin = custPin
        self.MIN_SAVE = 10_000
        self.MAX_SAVE = 10_000_000

    def checkName(self):
        return self.name

    def checkId(self): 
        return self.id

    def checkBalance(self):
        return self.balance

    def checkPin(self):
        return self.custPin

    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal

    def min_limit(self):
        return self.MIN_SAVE

    def max_limit(self):
        return self.MAX_SAVE


    




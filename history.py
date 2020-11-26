import transaction

class History(transaction.Transaction):
    def __init__(self):
        transaction.Transaction.__init__(self)
        self.trans_type = "History"
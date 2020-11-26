import transaction

class Return(transaction.Transaction):
    def __init__(self):
        transaction.Transaction.__init__(self)
        self.trans_type = "Return"

    def set_data(self, vinyl_album):
        if (vinyl_album is not None):
            self.album_item = vinyl_album
            self.album_item.increase_copies()
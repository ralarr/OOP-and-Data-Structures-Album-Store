import inventory

class Transaction:
    def __init__(self):
        self.trans_type = "Transaction"
        self.album_item = inventory.Inventory()

    def set_data(self):
        raise NotImplementedError()

    def display(self):
        print(self.trans_type, ": ", self.album_item._title, self.album_item._artist)
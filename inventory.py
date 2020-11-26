class Inventory:
    def __init__(self):
        self._title = ""
        self._artist = ""
        self.current_stock = 0
        self.total_stock = 0

    def setData(self):
        raise NotImplementedError()

    def set_stock(self, stock):
        self.current_stock += stock
        self.total_stock += stock

    def decrease_copies(self):
        if self.current_stock != 0:
            self.current_stock -= 1

    def increase_copies(self):
        if self.current_stock + 1 > self.total_stock:
            print("Error: Max Stock Exceeded")
            return
        self.current_stock += 1
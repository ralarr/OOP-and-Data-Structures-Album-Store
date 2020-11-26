import inventory

class Album(inventory.Inventory):
    def __init__(self):
        inventory.Inventory.__init__(self)
        self._title = ""
        self._artist = ""
        self._year = 0

    def set_data(self, title, artist, year):
        self._title = title
        self._artist = artist
        self._year = year
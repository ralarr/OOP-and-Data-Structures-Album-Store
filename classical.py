import album

class Classical(album.Album):
    def __init__(self):
        self.__genre = "CLASSICAL"
        album.Album.__init__(self)

    @property
    def genre(self):
        return self.__genre
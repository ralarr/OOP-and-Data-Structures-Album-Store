import album

class Metal(album.Album):
    def __init__(self):
        self.__genre = "METAL"
        album.Album.__init__(self)

    @property
    def genre(self):
        return self.__genre
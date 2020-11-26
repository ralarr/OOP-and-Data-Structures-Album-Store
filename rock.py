import album

class Rock(album.Album):
    def __init__(self):
        self.__genre = "ROCK"
        album.Album.__init__(self)

    @property
    def genre(self):
        return self.__genre
import classical
import metal
import rock
import borrow
import returns
import history

class Factory:
    def __init__(self):
        self.NUMBER_OF_GENRES = 3

    def create_album(self, genre):
        if genre == 'C':
            return classical.Classical()
        elif genre == 'R':
            return rock.Rock()
        elif genre == 'M':
            return metal.Metal()

    def create_transaction(self, command):
        if command == 'B':
            return borrow.Borrow()
        elif command == 'R':
            return returns.Return()
        elif command == 'H':
            return history.History()
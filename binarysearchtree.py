import album

class BinarySearchTree:
    class Node:
        def __init__(self):
            self.album = album.Album()
            self.left = None
            self.right = None

    def __init__(self):
        self.root = BinarySearchTree.Node()
        self.size = 0

    def insert(self, root, new_album, qty):
        if root.album._title == "":
            root.album = new_album
            root.album.set_stock(qty)
            self.size += 1
        elif root.album._title == new_album._title:
            root.album.set_stock(qty)
            self.size += 1
        elif new_album._title < root.album._title:
            if root.left == None:
                root.left = BinarySearchTree.Node()
            self.insert(root.left, new_album, qty)
        elif new_album._title > root.album._title:
            if root.right == None:
                root.right = BinarySearchTree.Node()
            self.insert(root.right, new_album, qty)

    def search(self, root, title):
        if root is None:
            root = self.root

        if title == root.album._title:
            return root.album
        elif title < root.album._title:
            if root.left is not None:
                return self.search(root.left, title)
            else:
                return None
        elif title > root.album._title:
            if root.right is not None:
                return self.search(root.right, title)
            else:
                return None


    def print_tree(self):
        if self.root.album._title == "":
            return

        print('%s    %s                                %s          %s' %("IN-HAND", "TITLE", "ARTIST", "YEAR"))
        q = []
        q.append(self.root)    
        while len(q) != 0:
            if q[0].left != None:
                q.append(q[0].left)
            if q[0].right != None:
                q.append(q[0].right)

            print('%i         %s                    %s         %i' %(q[0].album.current_stock, q[0].album._title, q[0].album._artist, q[0].album._year))
            q.pop(0)
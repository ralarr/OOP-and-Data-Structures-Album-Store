import customer
import hashtable
import binarysearchtree
import factory
from utility import *

class Business:
    def __init__(self, name):
        self.name = name
        self.customers = hashtable.Hashtable()
        self.classicals = binarysearchtree.BinarySearchTree()
        self.rocks = binarysearchtree.BinarySearchTree()
        self.metals = binarysearchtree.BinarySearchTree()
        self.fact = factory.Factory()

    def build_customers(self, customers_file):
        with open(customers_file) as file:
            for line in file:
                index = 0
                cust = customer.Customer()
                buffer = parse_segment_space(line, index)
                cust.set_customer_id(int(buffer))

                index += len(buffer)+1
                buffer = parse_segment_space(line, index)
                cust.set_first_name(buffer)
                
                index += len(buffer)+1
                buffer = parse_segment_space(line, index)
                cust.set_last_name(buffer)
                self.customers.add_customer(cust)

    def build_inventory(self, inventory_file):
        with open(inventory_file) as file:
            for line in file:
                index = 0
                genre = line[index]
                
                index += len(genre)
                qty = parse_segment_space(line, index)
                
                index += len(qty)+2
                artist = parse_segment_coma(line, index)
                
                index += len(artist)+2
                title = parse_segment_coma(line, index)
                
                index +=len(title)+2
                year = parse_segment_space(line, index)
                
                new_album = self.fact.create_album(genre)
                new_album.set_data(title.strip(), artist.strip(), int(year))

                if genre is 'C':
                    self.classicals.insert(self.classicals.root, new_album, int(qty.strip()))
                elif genre is 'R':
                    self.rocks.insert(self.rocks.root, new_album, int(qty.strip()))
                elif genre is 'M':
                    self.metals.insert(self.metals.root, new_album, int(qty.strip()))


    def display_all_inventory(self):
        print("+++++++++++++ CLASSICALS ++++++++++++++")
        self.classicals.print_tree()
        print("++++++++++++++++ ROCK +++++++++++++++++")
        self.rocks.print_tree()
        print("+++++++++++++++ METALS ++++++++++++++++")
        self.metals.print_tree()


    def process_commands(self, commands_file):
        with open(commands_file) as file:
            for line in file:
                index = 0
                command = line[index]
                if command == 'I':
                    self.display_all_inventory()
                else:
                    current_transaction = self.fact.create_transaction(command)

                    index += len(command)+1
                    customer_id = parse_segment_space(line, index)
                    current_customer = self.customers.get_customer(int(customer_id))

                    if command == 'H':
                        current_customer.display_transactions()
                    elif command == 'B' or command == 'R':
                        current_customer.add_transaction(current_transaction)
                        index += len(customer_id)+1
                        genre = line[index]

                        index += len(genre)+1
                        album_title = parse_segment_coma(line, index)

                        found_album = None
                        if genre == 'C':
                            found_album = self.classicals.search(None, album_title.strip())
                        elif genre == 'R':
                            found_album = self.rocks.search(None, album_title.strip())
                        elif genre == 'M':
                            found_album = self.metals.search(None, album_title.strip())

                        current_transaction.set_data(found_album)
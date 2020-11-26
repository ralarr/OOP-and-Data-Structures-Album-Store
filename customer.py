class Customer:
    def __init__(self):
        self.id = -1
        self.first_name = ""
        self.last_name = ""
        self.next = None
        self.transaction_history = []

    def set_customer_id(self, id):
        self.id = id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_next(self, n):
        self.next = n

    def add_transaction(self, trans):
        self.transaction_history.append(trans)

    def display_transactions(self):
        print("Transacions for customer:", self.id, self.first_name, self.last_name)
        for x in range(0, len(self.transaction_history)):
            self.transaction_history[x].display()

    def print_customer(self):
        print("id:", self.id, "first name:", self.first_name, "last name:", self.last_name)
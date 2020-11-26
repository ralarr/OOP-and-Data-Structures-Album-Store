import customer

class Hashtable:
    def __init__(self):
        self.TABLE_SIZE = 13
        self.table = []
        for _ in range(0, self.TABLE_SIZE):
            self.table.append(customer.Customer())

    def hash(self, id):
        return id%self.TABLE_SIZE

    def add_customer(self, new_customer):
        index = self.hash(new_customer.id)
        if self.table[index].id == -1:
            self.table[index] = new_customer
        else:
            new_customer.set_next(None)

            p = self.table[index]
            while p.next is not None:
                p = p.next

            p.set_next(new_customer)

    def get_customer(self, id):
        index = self.hash(id)
        p = self.table[index]
        if p.id == -1:
            return None
        
        while p is not None:
            if p.id == id:
                return p
            p = p.next

        return p

    def print_table(self):
        for x in range(0 , self.TABLE_SIZE):
            print(x, end =" ")
            self.table[x].print_customer()
            
            p = self.table[x]
            while p.next is not None:
                p = p.next
                print(x, end =" ")
                p.print_customer()
import business

my_store = business.Business("Vinyl Store")
my_store.build_customers("customers.txt")
my_store.build_inventory("albums.txt")
my_store.process_commands("commands.txt")
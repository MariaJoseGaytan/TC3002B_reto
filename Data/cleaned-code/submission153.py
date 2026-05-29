class Publication:
    def __init__(self, name, writer, cost):
                                                            
        self.name = name
        self.writer = writer
        self.cost = cost

    def show_info(self):
                                     
        print(f"Name: {self.name}, Writer: {self.writer}, Cost: ${self.cost}")

    def modify_cost(self, updated_cost):
                                            
        self.cost = updated_cost


def insert_publication(inventory, name, writer, cost):
                                                 
    publication = Publication(name, writer, cost)
    inventory.append(publication)


def change_publication_cost(inventory, name, updated_cost):
                                              
    for publication in inventory:
        if publication.name == name:
            publication.modify_cost(updated_cost)


def display_inventory(inventory):
                           
    for publication in inventory:
        publication.show_info()


def run_store():
                                                 
    inventory = []
    insert_publication(inventory, "Pride and Prejudice", "Jane Austen", 10.49)
    insert_publication(inventory, "1984", "George Orwell", 8.99)

    print("Publications available before cost modification:")
    display_inventory(inventory)

    change_publication_cost(inventory, "1984", 6.99)

    print("\nPublications available after cost modification:")
    display_inventory(inventory)


if __name__ == "__main__":
    run_store()

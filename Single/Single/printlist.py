class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        current = self.head
        print("List Data:")
        while current!= None:
            print(current.get_data(),end=" ")
            current = current.get_next()

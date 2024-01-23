class linkedlist:
    def __init__(self):
        self.head=None
    def search(self,item):
        current=self.head
        found= False
        while current != None and not found:
            if current.get_data() == item:
                found=True
            else:
                found=False
                current= current.get_next()
        return found
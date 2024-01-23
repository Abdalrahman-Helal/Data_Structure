class linkedlist:
    def __init__(self):
        self.head=None
    def size(self):
        count=0
        current=self.head
        while current != None:
            count+=1
            current=current.get_next()
        return count
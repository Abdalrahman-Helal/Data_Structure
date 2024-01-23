class linkedlist:
    def __init__(self):
        self.head=None
        self.tail-None
    def addatend(self,item):
        newnode=node(item)
        current=self.head
        while current !=None:
            current=current.get_next()
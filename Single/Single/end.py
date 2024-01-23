class linkedlist:
    def __init__(self):
        self.head=None
    def addatend(self,item):
        newnode=node(item)
        current=self.head
        while current.get_next()!=None:
            current=current.get_next()
        #n.set_next(self.head)
        current.set_next(newnode)
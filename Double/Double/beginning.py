class linkedlist:
    def __init__(self):
        self.head=None
        self.tail-None
    def addatbeginning(self,item):
        newnode=node(item)
        if self.head==None:
            self.head=self.tail=self.newnode
        else:
            newnode.set_prev(None)
            newnode.set_next(self.head)
            self.head.set_previous(newnode)
            self.head=newnode
class linkedlist:
    def __init__(self):
        self.head=None
    def addatbeginning(self,data):
        temp = node(data)
        temp.set_next(self.head)
        self.head=temp
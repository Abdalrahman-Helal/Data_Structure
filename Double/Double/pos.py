class linkedlist:
    def __init__(self):
        self.head=None
        self.tail-None
    def addatpos(self,item,pos):
            if pos > self.size or pos<0:
                return None 
            else:
                newnode=node(item)
                current=self.head
                count=0
                while count < pos-1:
                    current=current.get_next()
                    count+=1
                newnode.set_next(current.get_next())
                newnode.set_prev(current)
                current.get_next.set_previous(newnode)
                current.set_next(newnode)
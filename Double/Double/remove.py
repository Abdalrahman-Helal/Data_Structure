class linkedlist:
    def __init__(self):
        self.head=None
        self.tail-None
    def remove(item):
                found = False
                current=self.head
            while not found :
                if current.get(data)==item:
                     found = True
                else:
                current=current.get_next()
           
            if current.get_prev()==None :
                self.head=current.get_next()
            else:
                current.get_prev().set_next(current.get_next())
                current.get_next().set_prev(current.get_prev())
class linkedlist:
    def __init__(self):
        self.head=None
    def addAtPosition(self, item, pos):
        if pos > self.size() or pos < 0:
            return None
        else:
            newNode = node(item)
            count = 0
            current = self.head
            while count < pos - 1:
                count += 1
                current = current.get_next()
            newNode.set_next(current.get_next())
            current.set_next(newNode)
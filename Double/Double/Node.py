class node:
    def __init__(self,data=None,next=None,prev=None):
        self.head=next
        self.data=data
        self.prev=prev
        
    def set_data(self,newdata):
        self.data=newdata
        
    def get_data():
        return self.data
    
    def set_next(self,newnext):
        self.next=newnext
        
    def get_next(self):
        return self.next
    
    def has_next(self):
        return self.next!=None
    
    def set_previous(self,newprev):
        self.previous=newprev
    
    def get_previous(self):
        return self.previous
    
    def has_prev(self):
        return self.previous !=None
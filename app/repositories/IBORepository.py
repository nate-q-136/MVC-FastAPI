from app.BO.base import BaseBO

class IBORepository:
    def __init__(self, instance:BaseBO):
        self.instance = instance
    
    def get(self, id):
        return self.instance.get(id)
    
    def list(self, skip: int = 0, limit: int = 100):
        return self.instance.list(skip, limit)
    
    def create(self, *args, **kwargs):
        return self.instance.create(*args, **kwargs)
    
    def update(self, id, data):
        return self.instance.update(id, data)
    
    def delete(self, id):
        return self.instance.delete(id)


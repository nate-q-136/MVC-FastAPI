class BaseBO:
    def __init__(self, db):
        self.db = db

    def get(self, id):
        return self.db.get(id)

    def list(self):
        return self.db.list()

    def create(self, data):
        return self.db.create(data)

    def update(self, id, data):
        return self.db.update(id, data)

    def delete(self, id):
        return self.db.delete(id)
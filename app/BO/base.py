from abc import ABC, abstractmethod

class BaseBO:
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def create(self, data):
        raise NotImplementedError

    @abstractmethod
    def update(self, id, data):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id):
        raise NotImplementedError

    @abstractmethod
    def list(self, skip: int = 0, limit: int = 100):
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError


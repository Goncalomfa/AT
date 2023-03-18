from alchemy import alchemy

class UserModel(alchemy.Model):
    __tablename__ = 'users'

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    username = alchemy.Column(alchemy.String(80))
    password = alchemy.Column(alchemy.String(80))
    devices = alchemy.relationship('DeviceModel', back_populates="user")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

"""
from alchemy import alchemy


class UserModel(alchemy.Model):
    __tablename__ = 'users'

    id = alchemy.Column(alchemy.Integer, primary_key=True)
    username = alchemy.Column(alchemy.String(80))
    password = alchemy.Column(alchemy.String(80))
    devices = alchemy.relationship('DeviceModel', back_populates="user")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
"""
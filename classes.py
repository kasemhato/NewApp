from google.appengine.ext import db
from google.appengine.ext.db import polymodel


class Admin(db.Model):
    name = db.StringProperty()
    password = db.StringProperty()

    def getKey(self):
        return self.key()


class City(db.Model):
    name = db.StringProperty()

    def getKey(self):
        return self.key()


class Restaurant(db.Model):
    name = db.StringProperty()
    address = db.StringProperty()
    speciality = db.StringProperty()
    phone = db.StringProperty()
    prices = db.StringProperty()
    city = db.ReferenceProperty(City, collection_name='restaurants')

    def getKey(self):
        return self.key()


class MyComments(db.Model):
    user = db.StringProperty()
    comment = db.StringProperty()
    restaurant = db.ReferenceProperty(Restaurant, collection_name='comments')

    def getKey(self):
        return self.key()
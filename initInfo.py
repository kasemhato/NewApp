import webapp2

from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from classes import *
import os
from google.appengine.ext.webapp import template


def init():
    c1 = City.get_or_insert('AMM')
    if c1.name:
        pass
    else:
        c1.name = 'Amman'
        c1.put()
        r1 = Restaurant.get_or_insert('BK')
        if r1.name:
            pass
        else:
            r1.name = 'Burger King'
            r1.address = 'Madina St.'
            r1.city = c1
            r1.phone = '0798414533'
            r1.prices = 'Medium'
            r1.speciality = 'Fast Food'
            r1.put()



    c1 = City.get_or_insert('AQ')
    if c1.name:
        pass
    else:
        c1.name = 'Aqaba'
        c1.put()
        r1 = Restaurant.get_or_insert('AM')
        if r1.name:
            pass
        else:
            r1.name = 'Al Mankal'
            r1.address = 'Tunisan Falls St.'
            r1.city = c1
            r1.phone = '5438432'
            r1.prices = 'Medium'
            r1.speciality = 'Fast Food'
            r1.put()


    c1 = City.get_or_insert('IR')
    if c1.name:
        pass
    else:
        c1.name = 'Irbid'
        c1.put()
        r1 = Restaurant.get_or_insert('HA')
        if r1.name:
            pass
        else:
            r1.name = 'Hashem'
            r1.address = 'Sport City'
            r1.city = c1
            r1.phone = '5414233'
            r1.prices = 'Low'
            r1.speciality = 'Falafel'
            r1.put()
            comment = MyComments.get_or_insert('C')
            if comment.comment:
                pass
            else:
                comment.comment = "Very Good"
                comment.user = "Qasem Hato"
                comment.restaurant = r1
                comment.put()



    a1 = Admin.get_or_insert('QA')
    if a1.name:
        pass
    else:
        a1.name = 'kasemhato'
        a1.password = '1234'
        a1.put()

    a1 = Admin.get_or_insert('AR')
    if a1.name:
        pass
    else:
        a1.name = 'arieg'
        a1.password = '1234'
        a1.put()

    a1 = Admin.get_or_insert('HA')
    if a1.name:
        pass
    else:
        a1.name = 'hassan'
        a1.password = '1234'
        a1.put()




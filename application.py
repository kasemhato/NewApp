import webapp2

from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from classes import *
import os
from google.appengine.ext.webapp import template
from initInfo import *


class logInPage(webapp2.RequestHandler):
    def get(self):
        init()

        file = os.path.join(os.path.dirname(__file__), 'logIn.html')

        self.response.out.write(template.render(file, None))


    def post(self):
        file = os.path.join(os.path.dirname(__file__), 'logIn.html')

        self.response.out.write(template.render(file, None))


class ChooseCityPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('username')
        password = self.request.get('password')
        q = db.Query(Admin)
        q.filter('name =',name)
        for x in q:
            user = x

        admin = False

        if user.name == name and user.password == password:
            admin = True

        cities = City.all()

        file = os.path.join(os.path.dirname(__file__), 'ChooseCity.html')
        context = {
            'admin' : admin,
            'cities': cities
        }
        self.response.out.write(template.render(file, context))

class addCityPage(webapp2.RequestHandler):
    def post(self):
        file = os.path.join(os.path.dirname(__file__), 'addCity.html')
        
        self.response.out.write(template.render(file, None))

class ViewRestaurants(webapp2.RequestHandler):
    def post(self):

        name = self.request.get('city')
        c = City.get(name)
        restaurants = db.Query(Restaurant)
        restaurants.filter('city =',c.key())

        file = os.path.join(os.path.dirname(__file__), 'viewRes.html')
        context = {
            'city': c,
            'restaurants': restaurants
        }
        self.response.out.write(template.render(file, context))



app = webapp2.WSGIApplication([('/logIn', logInPage), \
                               ('/chooseCity', ChooseCityPage), \
                               ('/viewRes', ViewRestaurants), \
                               ('/addCity', addCityPage)], debug=True)
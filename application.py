import webapp2

from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from classes import *
import os
from google.appengine.ext.webapp import template
from initInfo import *


isAdmin = False
flag = False
class logInPage(webapp2.RequestHandler):
    def get(self):
        init()

        file = os.path.join(os.path.dirname(__file__), 'logIn.html')

        self.response.out.write(template.render(file, None))


    def post(self):
        file = os.path.join(os.path.dirname(__file__), 'logIn.html')

        self.response.out.write(template.render(file, None))

class SignOut(webapp2.RequestHandler):
    def post(self):
        global isAdmin, flag
        isAdmin = False
        flag = False
        file = os.path.join(os.path.dirname(__file__), 'logIn.html')

        self.response.out.write(template.render(file, None))


class ChooseCityPage(webapp2.RequestHandler):
    def post(self):

        cities = City.all()
        global isAdmin, flag
        if flag == False:
            name = self.request.get('username')
            password = self.request.get('password')
            q = db.Query(Admin)
            q.filter('name =',name)
            user = Admin()
            for x in q:
                user = x
            if user.name == name and user.password == password:
                isAdmin = True

        file = os.path.join(os.path.dirname(__file__), 'ChooseCity.html')
        context = {
            'isAdmin': isAdmin,
            'cities': cities
        }
        self.response.out.write(template.render(file, context))

class addCityPage(webapp2.RequestHandler):
    def post(self):
        file = os.path.join(os.path.dirname(__file__), 'addCity.html')
        self.response.out.write(template.render(file, None))

class cityAddedPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('cityname')
        c = City()
        c.name = name
        c.put()

        file = os.path.join(os.path.dirname(__file__), 'cityAdded.html')
        context = {
            'city' : c
        }
        self.response.out.write(template.render(file, context))

class ViewRestaurants(webapp2.RequestHandler):
    def post(self):
        global isAdmin
        name = self.request.get('city')
        c = City.get(name)
        restaurants = db.Query(Restaurant)
        restaurants.filter('city =',c.key())

        file = os.path.join(os.path.dirname(__file__), 'viewRes.html')
        context = {
            'isAdmin' : isAdmin,
            'city': c,
            'restaurants': restaurants
        }
        self.response.out.write(template.render(file, context))

class RestaurantPage(webapp2.RequestHandler):
    def post(self):
        global isAdmin
        name = self.request.get('restaurant')
        r = Restaurant.get(name)
        comments = db.Query(MyComments)
        comments.filter('restaurant =', r.key())

        file = os.path.join(os.path.dirname(__file__), 'Restaurant.html')
        context = {
            'isAdmin' : isAdmin,
            'comments': comments,
            'restaurant': r
        }
        self.response.out.write(template.render(file, context))

class AddRestaurantPage(webapp2.RequestHandler):
    def post(self):
        cities = db.Query(City)
        file = os.path.join(os.path.dirname(__file__), 'addRestaurant.html')
        context = {
            'cities': cities
        }
        self.response.out.write(template.render(file, context))

class RestaurantAddedPage(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('resName')
        phone = self.request.get('resPhone')
        address = self.request.get('resAddress')
        special = self.request.get('resSpecial')
        price = self.request.get('resPrice')
        key = self.request.get('city')
        city = City.get(key)

        r = Restaurant()
        r.name = name
        r.address = address
        r.phone = phone
        r.prices = price
        r.speciality = special
        r.city = city
        r.put()


        file = os.path.join(os.path.dirname(__file__), 'resAdded.html')
        context = {
            'restaurant': r,
            'city': city
        }
        self.response.out.write(template.render(file, context))

class CommentAdded(webapp2.RequestHandler):
    def post(self):

        name = self.request.get('restaurant')
        r = Restaurant.get(name)
        u = self.request.get('user')
        c = self.request.get('comment')

        newComment = MyComments()
        newComment.user = u
        newComment.comment = c
        newComment.restaurant = r
        newComment.put()
        context = {
            'restaurant': r
        }
        file = os.path.join(os.path.dirname(__file__), 'CommentAdded.html')

        self.response.out.write(template.render(file, context))





app = webapp2.WSGIApplication([('/logIn', logInPage), \
                               ('/chooseCity', ChooseCityPage), \
                               ('/viewRes', ViewRestaurants), \
                               ('/addCity', addCityPage), \
                               ('/cityAdded', cityAddedPage), \
                               ('/Restaurant', RestaurantPage), \
                               ('/Comment', CommentAdded), \
                               ('/SignOut', SignOut), \
                               ('/addRes', AddRestaurantPage), \
                               ('/RestaurantAdded', RestaurantAddedPage)], debug=True)
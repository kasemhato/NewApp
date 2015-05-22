import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

html = '''
    <h1> Welcome to Find Your Restaurant Application .</h1>
    <p> Click <a href = "logIn">here<a> to enter the website</p>
    '''

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(html)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authentication.views import home, signup,signin,signout
""" Test de URL's  """
class TestUrls (SimpleTestCase) :

    def test_home_url_resolved(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    def test_signup_url_resolved(self):
        url=reverse('signup')
        self.assertEquals(resolve(url).func,signup)
    def test_signin_url_resolved(self):
        url=reverse('signin')
        self.assertEquals(resolve(url).func,signin)
    def test_signout_url_resolved(self):
        url=reverse('signout')
        self.assertEquals(resolve(url).func,signout)
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
class TestHomePage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Chrome('functional_tests/chromedriver.exe')
    def tearDown(self):
        self.browser.close()
    def test_all_display(self):
        self.browser.get(self.live_server_url)
        # El usuario ingresa a la pagina por primera vez
        self.assertEquals(self.browser.find_element_by_tag_name('h2').text,'Universidad Tecnológica de Chihuahua')
        self.assertEquals(self.browser.find_element_by_tag_name('h3').text,'LogIn hecho con Django')
    def test_redirect_to_signup(self):
        self.browser.get(self.live_server_url)
        signup_url=self.live_server_url+reverse('signup')
        self.browser.find_element_by_class_name('signup').click()
        self.assertEquals(self.browser.current_url,signup_url)
    def test_redirect_to_signin(self):
        self.browser.get(self.live_server_url)
        signin_url=self.live_server_url+reverse('signin')
        self.browser.find_element_by_class_name('signin').click()
        self.assertEquals(self.browser.current_url,signin_url)
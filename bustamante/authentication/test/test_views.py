from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth.models import User
class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.home_url=reverse('home')
        self.signup_url=reverse('signup')
        self.signin_url=reverse('signin')
        self.signout_url=reverse('signout')
     
        
      
    def test_home_view(self):
        response=self.client.get(self.home_url)
        self.assertTemplateUsed(response,'authentication/index.html')
    def test_signup_view_POST(self):
        response=self.client.post(self.signup_url,{
            "username":"usernametest",
            "fname":"name",
            "lname_patern":"apellido1",
            "lname_matern":"apellido2",
            "tel":"6144101010",
            "email":"email@email.com",
            "pass1":"Passworld_1",
            "pass2":"Passworld_1"})
        self.assertRedirects(response,"/signin")
    def test_signup_view_POST_alreadyexists(self):
        username="usernametest"
        email="email@email.com"
        pass1="passworld"
        User.objects.create_user(username, email, pass1)
        response=self.client.post(self.signup_url,{
            "username":"usernametest",
            "fname":"name",
            "lname_patern":"apellido1",
            "lname_matern":"apellido2",
            "tel":"6144101010",
            "email":"email@email.com",
            "pass1":"passworld",
            "pass2":"passworld"})
        self.assertRedirects(response,"/signup")
    def test_signup_view_POST_passless8(self):
        response=self.client.post(self.signup_url,{
            "username":"usernametest",
            "fname":"name",
            "lname_patern":"apellido1",
            "lname_matern":"apellido2",
            "tel":"6144101010",
            "email":"email@email.com",
            "pass1":"pass",
            "pass2":"pass"})
        self.assertRedirects(response,"/signup")
    def test_signup_view_POST_nocoinciden(self):
        response=self.client.post(self.signup_url,{
            "username":"usernametest",
            "fname":"name",
            "lname_patern":"apellido1",
            "lname_matern":"apellido2",
            "tel":"6144101010",
            "email":"email@email.com",
            "pass1":"passworld",
            "pass2":"passworld1"})
        self.assertRedirects(response,"/signup")
    def test_signin_view_POST(self):
        username="user"
        email='email@testemail.com'
        pass1='passworld1'
        User.objects.create_user(username, email, pass1)
        response=self.client.post(self.signin_url,{
            "username":username,
            "pass1":pass1})
        self.assertTemplateUsed(response,'authentication/index.html')
        self.assertEquals(response.status_code,200)
    def test_signin_view_POST_nodata(self):
        username="user"
        email='email@testemail.com'
        pass1='passworld1'
        response=self.client.post(self.signin_url,{
            "username":username,
            "pass1":pass1})
        self.assertRedirects(response,"/signin")
    def test_signout(self):
       response= self.client.get(self.signout_url)
       self.assertRedirects(response,'/home')
        
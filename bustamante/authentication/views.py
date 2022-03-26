from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):
#Cuando llamamos de nuevo este url en el formulario, lo hacemos con el metodo POST
#asi que tomando eso en cuenta, usamos un if para obtener los datos del formulario
#y los guardamos en diferentes variables
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname_patern = request.POST['lname_patern']
        lname_matern = request.POST['lname_matern']
        tel = request.POST['tel']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Este nombre de usuario ya existe¡¡")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Esta dirección de correo ya esta registrada¡¡")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Las contraseñas no coinciden¡¡")
            return redirect('signup')

        if len(pass1)<8:
            messages.error(request, "La contraseña debe ser mayor a 8 caracteres¡¡")
            return redirect('signup')

        if pass1.isalnum():
            messages.error(request, "La contraseña debe tener caracteres especiales¡¡")
            return redirect('signup')

        if not any(c.isupper() for c in pass1):
            messages.error(request, "La contraseña debe tener mayúsculas y minúsculas¡¡")
            return redirect('signup')

        if not any(c.islower() for c in pass1):
            messages.error(request, "La contraseña debe tener mayúsculas y minúsculas¡¡")
            return redirect('signup')

        if not any(c.isdigit() for c in pass1):
            messages.error(request, "La contraseña debe tener números¡¡")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        #esto posiblemente no funciona
        myuser.last_name_patern = lname_patern
        myuser.last_name_matern = lname_matern
        myuser.tel = tel

        myuser.save()

        messages.success(request, "Usuario creado exitosamente")

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        #Esto devuelve una respuesta "none" o una respuesta "not none" en base al resultado
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Has iniciado sesión correctamente")
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Las credenciales no coinciden")
            return redirect('signin')


    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Ha cerrado sesión exitosamente")
    return redirect('home')
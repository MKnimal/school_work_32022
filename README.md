# Login_Practice
Una practica de un "login" haciendo uso de Django para la tarea de seguridad

Chicos, para poder arrancar esto abro la carpeta en el simbolo del sistema,
ejecuto el comando

    pip install virtualenv

Luego el comando

    venv\Scripts\activate

y ya en el entorno virtual ejecuto el comando

    python manage.py runserver

por ultimo pongo la direccion que me marque en

    Starting development server at AQUI VA LO QUE PONES EN EL NAVEGADOR

Esto lo hice en base al tutorial del video

https://www.youtube.com/watch?v=1UvTNMH7zDo

En caso de recibir el error 

    ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
    
Ejecuta el comando 

    pip install django

###### CHECKLIST DE LA RUBRICA

    [OK]    Desarrollar una app para Web donde  solicite al usuario:

        [OK]        username,

        [OK]        nombre,

        [OK]        apellido paterno,

        [OK]        apellido materno,

        [OK]        password,

        [OK]        teléfono, y

        [OK]        dirección,

        [OK]        todos los campos son obligatorios

    [OK]    La clave debe ser

        [OK]        mínimo de 8 caracteres

            [OK]            (incluir una letra mayúscula,

            [OK]            un número y

            [OK]            un carácter especial)

        [OK]    El username solo puede registrarse una sola vez

        [OK]    No debe haber duplicidad del username

        [OK]    La app debe poder autenticar a los usuarios registrados

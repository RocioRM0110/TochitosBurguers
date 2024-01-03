from django.shortcuts import render, redirect
from rest_framework.views import APIView
# from .forms import RegistroForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Guarda los datos del formulario en la base de datos
            form.save()
            # Redirige a la página de inicio de sesión u otra página que desees
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            messages.success(request, 'El registro se ha creado con éxito.')  # Añade un mensaje de confirmación
            # Redirige a la página de inicio de sesión u otra página que desees
            
            # Envía el correo de bienvenida
            subject = 'Bienvenido a BURGER TOCHITOS'
            from_email = 'chio7933@gmail.com'
            recipient_list = [correo]
            contexto = {'correo': correo, 'password': password}
            contenido_correo = render_to_string('correo.html', contexto)
            send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

        return redirect('iniciar_sesion')
        
    else:
        form = RegistroForm()
    return render(request, 'register.html', {'form': form})
# views.py
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.template.loader import render_to_string
# from django.core.mail import send_mail
# from .forms import RegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # Guarda los datos del formulario en la base de datos
#             form.save()

#             # Redirige a la página de inicio de sesión u otra página que desees
#             messages.success(request, 'El registro se ha creado con éxito.')

#             # Envía el correo de bienvenida
#             subject = 'Bienvenido a BURGER TOCHITOS'
#             from_email = 'chio7933@gmail.com'
#             correo = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             recipient_list = [correo]
#             contexto = {'correo': correo, 'password': password}
#             contenido_correo = render_to_string('correo.html', contexto)
#             send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

#             return redirect('iniciar_sesion')

#     else:
#         form = RegisterForm()

#     return render(request, 'register.html', {'form': form})



class Login(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Index(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Validar que las contraseñas coincidan
        if password != password_confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('register')  # Redirigir de vuelta al formulario de registro con el mensaje de error

        # Crear el usuario
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('login')  # Redirigir a la página de inicio de sesión después del registro exitoso
        except Exception as e:
            messages.error(request, f'Error durante el registro: {e}')
            return redirect('register')  # Redirigir de vuelta al formulario de registro con el mensaje de error

    return render(request, 'register.html')  # Asegúrate de cambiar 'tu_app' por el nombre real de tu aplicación

    
class Password(APIView):
    template_name="password.html"
    def get(self,request):
        return render(request,self.template_name)
    
class About(APIView):
    template_name="about.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Blog(APIView):
    template_name="blog.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Contact(APIView):
    template_name="contact.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Recipe(APIView):
    template_name="recipe.html"
    def get(self,request):
        return render(request,self.template_name)

class Login(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)

class Dash(APIView):
    template_name="dash.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Products(APIView):
    template_name="products.html"
    def get(self,request):
        return render(request,self.template_name)

class Index2(APIView):
    template_name="index2.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Index3(APIView):
    template_name="index3.html"
    def get(self,request):
        return render(request,self.template_name)
# # views.py
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'index.html', {'recipes': recipes})

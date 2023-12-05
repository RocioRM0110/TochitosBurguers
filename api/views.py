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


class Login(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Index(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Register(APIView):
    template_name="register.html"
    def get(self,request):
        return render(request,self.template_name)
    
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

# # views.py
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'index.html', {'recipes': recipes})

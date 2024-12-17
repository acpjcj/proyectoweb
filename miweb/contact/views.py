from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from miweb.settings import EMAIL_HOST_USER

# Create your views here.
# def contact(request):
#     errors = []
#     if request.method == "POST":
#         if not request.POST.get('nombre',''):
#             errors.append("Por favor, introduce el nombre")
#         if not request.POST.get('mensaje',''):
#             errors.append("Por favor, introduce el mensaje")
#         if not request.POST.get("email") and '@' not in request.POST['email']:
#             errors.append("Por favor, introduce un email valido")
#         if not errors:
#             #enviamos email y redireccionamos
#             return redirect(reverse('contact')+"?ok") 
        
#     return render(request, "contact/contact.html", {'errors': errors,
#                   'asunto': request.POST.get('asunto',''),
#                   'mensaje': request.POST.get('mensaje',''),
#                   'email': request.POST.get('email','')
#                   })

def contact(request):
    if request.method == 'POST':         #en este caso procesaremos el formulario
        form = ContactForm(request.POST)#aquí almacenamos los datos del formulario
        if form.is_valid():#comprobamos que los datos del formulario son válidos
            # Limpia los datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #enviaremos el email y redireccionamos
            # Configura el correo electrónico
            email_subject = 'Nuevo mensaje de contacto'
            email_body = f'De: {name} <{email}>\n\nMensaje:\n\n{message}'
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email='no-reply@tusitio.com',  # Cambia esto según tu configuración
                to=['acpjcj@gmail.com'],  # Correo destino
                reply_to=[email],
            )

            #AQUÍ INTRODUCIMOS EL ENVÍO DEL MAIL
            try:
                email.send()
                #si todo va ok, redireccionamos a ?ok
                return redirect(reverse('contact')+'?ok')
            except:
                #si algo falla, redireccionamos a ?fail
                return redirect(reverse('contact')+'?fail')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

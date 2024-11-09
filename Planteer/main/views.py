from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from plants.models import Plant

# Create your views here.


def home(request):

    plants = Plant.objects.all()  
    return render(request, 'main/home.html', {'plants': plants})



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'main/contact_us.html', {'form': form})

def contact_messages(request):
    messages = Contact.objects.all()
    return render(request, 'main/contact_messages.html', {'messages': messages})





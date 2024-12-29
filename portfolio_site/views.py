from django.shortcuts import render, redirect
from .models import Project, ContactMessage
from .forms import ContactForm

# Homepage view
def home(request):
    projects = Project.objects.all()  # Retrieve all projects
    return render(request, 'home.html', {'projects': projects})

# Contact form view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the contact message to the database
            return redirect('thankyou')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

# Thank you page view
def thankyou(request):
    return render(request, 'thankyou.html')

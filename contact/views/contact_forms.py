from django.shortcuts import render  # get_object_or_404
from django.http import HttpRequest
from contact.forms import ContactForm


def create(request: HttpRequest):
    if request.method == 'POST':
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))

    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST),
            'title': 'Create Contact',
        }
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm(),
        'title': 'Create Contact',
    }
    return render(
        request,
        'contact/create.html',
        context
    )

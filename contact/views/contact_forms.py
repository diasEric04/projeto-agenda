from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact


def create(request: HttpRequest):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            # se o formulario ja ter sido respondido, vai passar o mesmo
            # formulario que ja foi respondido para que os campos
            # nao fiquem em branco
            'form': form,
            'title': 'Create Contact',
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact.id)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        # se apenas entrar na pagina, vai passar um formalario vazio
        'form': ContactForm(),
        'title': 'Create Contact',
        'form_action': form_action,
    }
    return render(
        request,
        'contact/create.html',
        context
    )


def update(request: HttpRequest, contact_id):
    form_action = reverse('contact:update', args=(contact_id, ))
    contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True
    )

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            # se o formulario ja ter sido respondido, vai passar o mesmo
            # formulario que ja foi respondido para que os campos
            # nao fiquem em branco
            'form': form,
            'title': 'Create Contact',
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact.id)

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        # se apenas entrar na pagina, vai passar um formalario vazio
        'form': ContactForm(instance=contact),
        'title': 'Create Contact',
        'form_action': form_action,
    }
    return render(
        request,
        'contact/create.html',
        context
    )


def delete(request, contact_id):
    contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True
    )
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    page_title = f'{contact.first_name} {contact.last_name}'

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'title': page_title,
            'confirmation': confirmation
        }
    )

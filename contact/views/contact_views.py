from django.shortcuts import render  # get_object_or_404
from contact.models import Contact
from django.http import Http404


def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')\

    context = {
        'title': 'Home',
        'contacts': contacts
    }
    print(contacts)
    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):

    single_contact = Contact.objects.filter(id=contact_id, show=True).first()

    # single_contact = get_object_or_404(
    #   Contact.objects.filter(id=contact_id).first()
    # )

    # metodo last retorna o ultimo elemento da queryset
    # metodo first retorna primeiro elemento da queryset

    if single_contact is None:
        raise Http404()

    page_title = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'title': page_title or 'not found',
        'contact': single_contact
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

from django.shortcuts import render, redirect  # get_object_or_404
from django.db.models import Q
from contact.models import Contact
from django.http import Http404, HttpRequest
from django.core.paginator import Paginator


def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')\

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Home',
        'page_obj': page_obj
    }
    return render(
        request,
        'contact/index.html',
        context
    )


def search(request: HttpRequest):
    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    # iexact = exatamente o que tem escrito, sem considerar letras maisculas
    # exact = exatament o que tem escrito
    # contains = contem um trecho no campo
    # icontains = contem um techo no campo, sem considerar letras maisculas
    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value)
        )\
        .order_by('-id')\
        # [10:20] = [limit:offset] na consulta

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Home',
        'page_obj': page_obj
    }
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

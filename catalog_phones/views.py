
from django.shortcuts import render, redirect

from catalog_phones.models import Phone



def index(request):
    return redirect('catalog.html')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog_phones/catalog.html',

    sort_by = request.GET.get('sort', None)
    if sort_by == 'name':
        phones = phones.order_by('name')

    if sort_by == 'min_price':
        phones = phones.order_by('-price')

    if sort_by == 'max_price':
        phones = phones.order_by('price')


    return render(request, template, {'phones': phones})



def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context)
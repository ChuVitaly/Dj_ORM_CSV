from django.shortcuts import render, redirect

from catalog_phones.models import Phone



def index(request):
    return redirect('catalog.html')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog_phones/catalog.html',
    context = {
        'phones': phones,
        'title': 'Каталог'
    }
    return render(request, template, context)
    # return render(request, 'catalog_phones/catalog.html', {'phone': phone, 'title': 'Каталог', 'main': 'КАТАЛОГ'})



def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
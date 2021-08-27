from django.shortcuts import render

from mainapp.models import Product

from mainapp.views import get_basket


def index(request):
    title = 'магазин'

    products = Product.objects.all()

    context = {
        'title': title,
        'products': products,
        'basket': get_basket(request),
    }

    return render(request, 'index.html', context=context)


def contacts(request):
    title = 'contacts us'

    context = {
        'title': title,
        'basket': get_basket(request),
    }

    return render(request, 'contact.html', context=context)


def about(request):
    title = 'about us'

    context = {
        'title': title,
        'basket': get_basket(request),
    }

    return render(request, 'about.html', context=context)

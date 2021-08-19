from django.shortcuts import render


def products(request):

    title = 'прордукты | каталог'


    Filter_menu = [
        {'Filter': '*', 'name': 'ALL Products'},
        {'Filter': '.new', 'name': 'Newest'},
        {'Filter': '.low', 'name': 'Low Prise'},
        {'Filter': '.higt', 'name': 'Hight Prise'},
    ]


    context = {
        'title': title,
    }

    return render(request, 'mainapp/products.html', context=context)



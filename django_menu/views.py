from django.shortcuts import render
from .models import Menu

def show_menu(request):
    menu_items = Menu.objects.filter(parent__isnull=True)
    context = {
        'menu_items': menu_items
    }
    return render(request, 'django_menu/menu.html', context=context)


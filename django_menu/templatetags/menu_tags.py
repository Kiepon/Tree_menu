from django import template
from django_menu.models import Menu

register = template.Library()

@register.inclusion_tag('django_menu/tree_menu.html')
def render_menu(parent=None):
    if parent is None:
        menu_items = Menu.objects.filter(parent=None).select_related('parent')
    else:
        menu_items = parent.children.all()
    return {'menu_items': menu_items}


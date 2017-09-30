from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
# def get_category_list():
#     return {'cats': Category.objects.all()}

# with this parameter the category we're visiting will be bold on the sidebar
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),
        'act_cat': cat}

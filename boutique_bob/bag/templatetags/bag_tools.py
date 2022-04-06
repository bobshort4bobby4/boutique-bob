"""docstring"""

from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """function docstring"""
    return price * quantity

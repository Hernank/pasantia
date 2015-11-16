from django.template import Library
register = Library()

@register.filter(name='modulo')
def modulo(num, val):
    return num % val == 0
@register.filter(name='len')
def len(mistr, val):
    return mistr[:val] 
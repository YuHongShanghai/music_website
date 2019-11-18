from django import template

register = template.Library()

@register.filter('nrange')
def nrange(i,max_p):
    d=2
    if max_p<=2*d+1:
        return range(1,max_p+1)
    if i-d>=1 and i+d<=max_p:
        return range(i-d,i+d+1)
    if i-d>=1 and i+d>max_p:
        return range(max_p-2*d,max_p+1)
    if i-d<1 and i+d<=max_p:
        return range(1,2*d+2)
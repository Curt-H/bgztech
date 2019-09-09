import time

from django import template

register = template.Library()


@register.simple_tag(name='to_date')
def to_date(time_sec):
    t = time_sec
    t_date = time.localtime(t)
    result = time.strftime("%Y-%m-%d", t_date)
    return result

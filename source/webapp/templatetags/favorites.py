from django import template

register = template.Library()


@register.filter
def added_by(obj, user):
    return obj.added_by(user)
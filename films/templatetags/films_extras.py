"""
Це файл для власних фільтрів django.
Наприклад, у шаблоні можна прописати таке:
{{ p.list_of_likers|check_if_liked:user.id }}
Таким чином, можна передати один параметр у функцію.
"""

from django import template

register = template.Library()

@register.filter
def check_if_liked(value, user_id):
    if int(user_id) in value:
        return True
    else:
        return False
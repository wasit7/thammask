from django import template
from donate.models import Profile

register = template.Library()

@register.filter(name='get_full_name') 
def get_full_name(user_pk):
    profile = ''
    if user_pk is not None:
        profile = Profile.objects.get(user__id=user_pk)
        return profile

    else:
        return profile
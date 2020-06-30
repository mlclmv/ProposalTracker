from django.template.defaulttags import register

# Filter to get the nth item.VALUE from a dict
@register.filter
def get_item(d, k):
    try:
        return d.get(k)
    except:
        return None
    
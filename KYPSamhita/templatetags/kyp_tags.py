from django.template.defaulttags import register

# Filter to get the nth item.VALUE from a dict
@register.filter
def get_item(dictionary, key):
    print ("get_item",dictionary,key)
    return dictionary.get(key)
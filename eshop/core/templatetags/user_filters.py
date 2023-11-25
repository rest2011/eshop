from django import template

register = template.Library()

@register.filter
def addclass(field, css):
    if field.name == 'fast_charge':
        return field
    return field.as_widget(attrs={'class': css})

@register.filter
def recursive_subcategories(category):
    subcategories = category.subcategories.all()
    results = list(subcategories)
    for subcategory in subcategories:
        results.extend(recursive_subcategories(subcategory))
    return results

@register.filter
def attr(obj, attr_name):
    if hasattr(obj, attr_name):
        return getattr(obj, attr_name)
    else:
        return None

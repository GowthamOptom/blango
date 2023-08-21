from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):
      return ""

    if author == current_user:
      return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        return f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
      prefix = format_html('<a href="mailto:{}">', author.email)
      suffix = format_html("</a>")
    else:
      prefix = ""
      suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)
    

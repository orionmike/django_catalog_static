
import re

from django.core.paginator import Paginator
from slugify import slugify


def get_slug(line_str: str) -> str:

    result = line_str.lower().strip()
    result = re.sub(r'\s+', ' ', result)
    result = result.replace('й', 'j')
    result = slugify(result)
    result = result.replace('ia', 'ya')
    return result


def get_pagination(request, object_list, PAGINATE_BY):

    paginator = Paginator(object_list, PAGINATE_BY)
    page_number = request.GET.get('page', 1)
    page_object_list = paginator.get_page(page_number)
    is_paginated = page_object_list.has_other_pages()

    print(page_number)

    if page_object_list.has_previous():
        prev_url = f'?page={page_object_list.previous_page_number()}'
    else:
        prev_url = ''

    if page_object_list.has_next():
        next_url = f'?page={page_object_list.next_page_number()}'
    else:
        next_url = ''

    return page_object_list, paginator, is_paginated, prev_url, next_url

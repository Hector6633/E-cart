from django import template

register = template.Library()

@register.filter(name="row_spliters")
def row_spliters(product_list_data,chunk_size):             
    chunk = []
    i=0
    for product_list_data in product_list_data:
        chunk.append(product_list_data)
        i += 1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    yield chunk    
from .models import Category


def all_links(request):
    links = Category.objects.all()
    return dict(links=links)

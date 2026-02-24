from .models import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
# means we are returning the categories by fetching from the db one time and used by all the templates at once and
# making it globally variable
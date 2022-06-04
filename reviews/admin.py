from django.contrib import admin
from .models import Publisher, Contributor, Book, Review, BookContributor
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BookContributor)
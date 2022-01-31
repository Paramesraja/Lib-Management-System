from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Damage)
admin.site.register(Copy)
admin.site.register(Author)
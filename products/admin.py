from django.contrib import admin
from .models import Review, Footwears, CategoryFootwears, FootwearCompany, Company

admin.site.register(Footwears)
admin.site.register(CategoryFootwears)
admin.site.register(FootwearCompany)
admin.site.register(Review)
admin.site.register(Company)


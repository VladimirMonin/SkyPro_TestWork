from django.contrib import admin

from companies.models import Product, Company

admin.site.register(Company)
admin.site.register(Product)

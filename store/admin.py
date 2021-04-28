from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'item_name',
        'total_stock_quantity',
        'issued_quantity',
        'issued_by',
        'issued_to'
    ]
    form = StockCreateForm
    list_filter = ['category', 'item_name']
    search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(StockHistory)

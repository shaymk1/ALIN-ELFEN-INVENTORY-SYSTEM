from django import forms
from django.forms import ModelForm
from . models import *


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [
            'category',
            'item_name',
            'total_stock_quantity',
            'reorder_level',
            'issued_quantity',
            'issued_to',
            'issued_by',
            'new_stock_received_by',
            # 'date',
            'sizes_ferrules',
            'sizes_lugs',
            'sizes_others',
            'returned',
            'condition_returned'


        ]

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        for instance in Stock.objects.all():
            if instance.category == category:
                raise forms.ValidationError(category + ' already exists')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name


class ReceiveNewStockItems(forms.ModelForm):
    model = Stock
    fields = ['category',
              'item_name',
              'total_stock_quantity',
              'reorder_level',
              'new_stock_received_by',
              'sizes_ferrules',
              'sizes_lugs',
              'sizes_others',
              'returned',
              'condition_returned'

              ]

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        for instance in Stock.objects.all():
            if instance.category == category:
                raise forms.ValidationError(category + ' already exists')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')
        return item_name


class StockHistorySearchForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)

	class Meta:
		model = StockHistory
		fields = ['category', 'item_name', 'start_date', 'end_date']

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'total_stock_quantity']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issued_quantity', 'issued_to', 'issued_by']


# , 'date_issued'

class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['received_new_stock_quantity', 'new_stock_received_by']


class ReceiveStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['received_new_stock_quantity', 'new_stock_received_by']


class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']



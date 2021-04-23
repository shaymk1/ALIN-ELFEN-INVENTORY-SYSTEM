from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import csv
from django.contrib import messages

# Create your views here.


def home(request):
    title = 'Alin Elfen Inventory Management System'
    form = 'Alin Elfen Inventory Management System'
    context = {
        'title': title,
        'form': form
    }

    return render(request, 'home.html', context)


def list_items(request):
    header = 'List Of Items'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    context = {
        'header': header,
        'queryset': queryset,
        'form': form
    }

    if request.method == 'POST':
        queryset = Stock.objects.filter(
            # category__icontains=form[' category'].value(),
            item_name__icontains=form['item_name'].value()
        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'TOTAL STOCK QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                    [stock.category, stock.item_name, stock.total_stock_quantity])
            return response

        context = {
            'header': header,
            'queryset': queryset,
            'form': form
        }

    return render(request, 'list_items.html', context)


def add_items(request):
    title = 'Add Items'
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added!')
        return redirect('/list_items')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'add_items.html', context)


def update_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    form = StockUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated!')
            return redirect('/list_items')

    context = {
        'form': form
    }
    return render(request, 'add_items.html', context)


def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Successfully Deleted!')
        return redirect('/list_items')
    return render(request, 'delete_items.html')

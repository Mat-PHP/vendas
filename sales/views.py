from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Sale, Product
from .forms import SaleForm, ProductForm
def index(request):
    qs = Sale.objects.select_related('product').all().order_by('-date')
    start = request.GET.get('start_date')
    end = request.GET.get('end_date')
    product = request.GET.get('product')
    if start:
        qs = qs.filter(date__gte=start)
    if end:
        qs = qs.filter(date__lte=end)
    if product:
        qs = qs.filter(product__name__icontains=product)
    totals = qs.values('product__name').annotate(total=Sum('quantity'))
    context = {
        'sales': qs,
        'totals': list(totals),
        'start': start or '',
        'end': end or '',
        'product_q': product or '',
    }
    return render(request, 'sales/index.html', context)
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:index')
    else:
        form = SaleForm()
    return render(request, 'sales/sale_form.html', {'form': form})
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales:index')
    else:
        form = ProductForm()
    return render(request, 'sales/sale_form.html', {'form': form})

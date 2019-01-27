from django.shortcuts import render

# Create your views here.


from .models import Product
from .forms import ProductForm, RowProductForm

def render_initial_data(request):
    initial_data = {
        'title' : 'This is my awesome title',
    }
    obj = Product.objects.get(id=2)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'create_view',context)
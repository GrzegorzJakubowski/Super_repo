from django.shortcuts import render

# Create your views here.


from .models import Product
from .forms import ProductForm, RowProductForm

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context ={
        'title' : obj.title,
        'description' : obj.description
    }
    return render(request,'client',context)


'''def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request,'create_view',context)'''


'''def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == 'POST':
        my_new_title = request.POST.get('title')
        print(my_new_title)
    context = {}
    return render(request,'create_view',context)'''



def product_create_view(request):
    my_form = RowProductForm()
    if request.method == "POST":
        my_form = RowProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form' : my_form
    }
    return render(request,'create_view',context)

def home_view(request):
    context = {}
    return render(request,'home',context)



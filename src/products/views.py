from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import RawProductForm
from .forms import ProductForm, RawProductForm

def product_list_view_link(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_detail.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()

    context = {
        "obj": obj
    }
    return render(request, "product/delete_form.html", context)


def dynamic_lookup_view(request, my_id):
    try:
        obj: object = Product.objects.get(id=int(my_id))
    except Product.DoesNotExist:
        raise Http404
    # obj = get_object_or_404(product, id=my_id)

    context = {
        "obj": obj
    }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "Mi titulo",

    }
    obj = Product.objects.get(id=13)
    form = RawProductForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    print(request.user)
    return render(request, "hello_world.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        'my_title': 'requested title',
        'my_number': 123,
        'my_list': [12, 46, 886, 445]
    }
    return render(request, "contact_view.html", my_context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    my_context = {
        'obj': obj
    }
    return render(request, "products/product_detail.html", my_context)


'''
def product_create_view(request, *args, **kwargs):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            print(my_form.errors)

    my_context = {
        "form": my_form
    }
    return render(request, "product/product_create.html", my_context)

'''
'''
def product_create_view(request, *args, **kwargs):

    title = request.POST.get('title')
    print(title)
    my_context = { }
    return render(request, "product/product_create.html", my_context)
'''


def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    my_context = {
        'form': form
    }
    return render(request, "product/product_create.html", my_context)

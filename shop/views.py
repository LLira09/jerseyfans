from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


def index(request):
    products = Product.objects.order_by('-created_at')[:3]
    context = {
        'products': products,
    }
    return render(request, 'shop/index.html', context)

def allProdCat(request, cat_slug=None):
    cat_page = None
    products_list = None
    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        products_list = Product.objects.filter(category=cat_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    
    paginator = Paginator(products_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'category':cat_page,
        'products':products_list,
        'products': products
    }
    
        
    return render(request, 'shop/category.html', context)

def ProdCatDetail(request, cat_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=product_slug)
    except Exception as e:
        raise e
    products = Product.objects.order_by('-created_at')[:3]

    return render(request, 'shop/product.html', {'product':product, 'products':products})

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:allProdCat')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form})
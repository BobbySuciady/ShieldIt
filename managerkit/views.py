
from .forms import UserRegistrationForm, AddCategoryForm, AddItemForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Category

def register_or_home(request):
    if User.objects.exists():
        return redirect('home')
    else:
        return redirect('register')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


# Item
def kits_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    categories = user.categories.all()
    items = categories.all()
    return render(request, 'kits_detail.html', {'user': user, 'categories': categories, 'item': items})

def add_category(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)  # Don't save immediately
            category.user = user  # Assign the user to the category
            category.save()  # Now save the category
            return redirect('kits_detail', user_id=user_id)  # Redirect to home or a relevant page
    else:
        form = AddCategoryForm()
    return render(request, 'add_category.html', {'form': form, 'user': user})

def add_item(request, user_id, category_id):
  category = get_object_or_404(Category, pk=category_id)
  if request.method == 'POST':
      form = AddItemForm(request.POST)
      if form.is_valid():
          item = form.save(commit=False)
          item.category = category
          item.save()
          return redirect('kits_detail', user_id=user_id)  # Adjust redirect as necessary
  else:
      form = AddItemForm()
  return render(request, 'add_item.html', {'form': form, 'category': category})
    


# User management functions below
def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user_detail.html', {'user': user})

def delete_user(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.delete()
    return redirect('manage_users')

def update_user(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('manage_users')  # Redirect to user detail page
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

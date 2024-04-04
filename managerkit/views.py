
from .forms import UserRegistrationForm, AddCategoryForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import User

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

def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    categories = user.categories.all()  # Assuming you have related_name='categories' on the ForeignKey in Category model
    return render(request, 'user_detail.html', {'user': user, 'categories': categories})

def add_category(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)  # Don't save immediately
            category.user = user  # Assign the user to the category
            category.save()  # Now save the category
            return redirect('home')  # Redirect to home or a relevant page
    else:
        form = AddCategoryForm()
    return render(request, 'add_category.html', {'form': form, 'user': user})

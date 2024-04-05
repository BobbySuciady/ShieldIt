
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
            user = form.save(commit=False)
            dietary_restrictions = form.cleaned_data.get('dietary_restrictions', '')
            user.dietary_restrictions = dietary_restrictions

            user.save()

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

def edit_user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'edit_user_detail.html', {'user': user})

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

def setting(request):
    return render(request, 'settings.html')
def notifications(request):
    return render(request, 'notifications.html')


def recommendations(request, user_id):
    user = User.objects.get(pk=user_id)


    dietary_restrictions = user.dietary_restrictions

    recommendations = []

    if dietary_restrictions == 'No Dietary Restrictions':
        recommendation_message = f"{user.name} can enjoy all variety of food options :)"
        recommendations.append(recommendation_message)
    elif dietary_restrictions == 'FODMAP':
        recommendation_message = f"FODMAP food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Rice cakes with almond butter")
        recommendations.append("Banana slices with peanut butter")
        recommendations.append("Canned tuna or salmon")
        recommendations.append("Dried fruits (ensure they're free from added sugars and high-FODMAP fruits)")
        recommendations.append("Mixed nuts (avoiding high-FODMAP varieties like cashews and pistachios)")
    elif dietary_restrictions == 'Gluten Free':
        recommendation_message = f"Gluten Free food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Popcorn")
        recommendations.append("Gluten-free granola bars")
        recommendations.append("Canned beans or lentils")
        recommendations.append("Canned tuna or chicken")
        recommendations.append("Canned vegetables (e.g., tomatoes, corn)")
    elif dietary_restrictions == 'Lactose Free':
        recommendation_message = f"Lactose Free food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Dark chocolate")
        recommendations.append("Roasted chickpeas")
        recommendations.append("Rice crackers with hummus")
        recommendations.append("Canned coconut milk")
        recommendations.append("Chia seed pudding")
    elif dietary_restrictions == 'Nut Free':
        recommendation_message = f"Nut Free food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Pretzels")
        recommendations.append("Sunflower seeds")
        recommendations.append("Instant mashed potatoes")
        recommendations.append("Rice noodle soup bowls")
        recommendations.append("Canned vegetable soup")
    elif dietary_restrictions == 'Vegan':
        recommendation_message = f"Vegan food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Vegan jerky")
        recommendations.append("Vegan protein bars")
        recommendations.append("Pickled vegetables (cucumbers, carrots, cauliflower)")
        recommendations.append("Instant noodles (check for vegan options)")
        recommendations.append("Trail mix (without nuts)")
    elif dietary_restrictions == 'Vegetarian':
        recommendation_message = f"Vegetarian food {user.name} might like :"
        recommendations.append(recommendation_message)
        recommendations.append("Preserved fruit jams and spreads")
        recommendations.append("Instant noodles (check for vegetarian options)")
        recommendations.append("Canned fruits (peaches, pears, pineapple)")
        recommendations.append("Canned vegetables (corn, green beans, peas)")
        recommendations.append("Canned beans (chickpeas, black beans, kidney beans)")
    else:
        recommendation_message = f"Complicated food restriction! Beware with choosing food for {user.name} :"
        recommendations.append(recommendation_message)
    
    recommendations.append("")
    
    recommendations.append("Personal Care items :")
    recommendations.append("Sanitary wipes and hygiene products")
    recommendations.append("Incontinence supplies (diapers, pads)")
    recommendations.append("Extra clothing appropriate for the climate")
    
    recommendations.append("")
    
    recommendations.append("Emergency Items :")
    recommendations.append("Blankets or sleeping bags")
    recommendations.append("Flashlights with extra batteries")
    recommendations.append("Multi-tool or Swiss army knife with accessible features")
    
    recommendations.append("")
    
    medical_conditions = user.medical_conditions
    if medical_conditions != "No Medical Conditions":
        recommendation_message = f"Medical Condition: {medical_conditions}!"
        recommendations.append(recommendation_message)
        recommendations.append(f"Don't forget to pack medicine for {user.name}'s {medical_conditions}!")
        
    recommendations.append("")
    
    disability = user.disability
    if disability == "Disable":
        recommendation_message = f"Disabled?! Does {user.name} needs following items? :"
        recommendations.append(recommendation_message)
        recommendations.append("Communication Aids")
        recommendations.append("Medical Supplies")
        recommendations.append("Mobility Aids")
        
    
    return render(request, 'recommendations.html', {'recommendations': recommendations, 'user': user})


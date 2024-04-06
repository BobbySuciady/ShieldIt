
from .forms import UserRegistrationForm, AddCategoryForm, AddItemForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Category, Item

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
  if request.method == 'POST':
    if "add_item_form" in request.POST:
      add_item_form = AddItemForm(request.POST)
      add_category_form = AddCategoryForm()
      if add_item_form.is_valid():
          item = add_item_form.save(commit=False)
          category_id = request.POST.get('category')
          # Use the category ID to get the Category object
          item.category = get_object_or_404(Category, id=category_id)
          item.save()
          return redirect('kits_detail', user_id=user_id)  # Adjust redirect as necessary
    elif "add_category_form" in request.POST:
      add_category_form = AddCategoryForm(request.POST)
      add_item_form = AddItemForm()
      if add_category_form.is_valid():
          category = add_category_form.save(commit=False)  # Don't save immediately
          category.user = user  # Assign the user to the category
          category.save()  # Now save the category
          return redirect('kits_detail', user_id=user_id)  # Redirect to home or a relevant page
  else:
    add_item_form = AddItemForm()
    add_category_form = AddCategoryForm()
  items = categories.all()
  return render(request, 'kits_detail.html', {'add_item_form':add_item_form, 'add_category_form':add_category_form, 'user': user, 'categories': categories, 'item': items})

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

def delete_category(request, user_id, category_id):
    if request.method == 'POST':
      category = Category.objects.get(id=category_id)
      category.delete()
    return redirect('kits_detail', user_id=user_id)

def add_item(request, user_id, category_id):
  user = get_object_or_404(User, pk=user_id)
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
  return render(request, 'add_item.html', {'add_item_form': form, 'category': category, 'user':user})
    
def delete_item(request, user_id, category_id, item_id):
  if request.method == 'POST':
    #category = Category.objects.get(id=category_id)
    item = Item.objects.get(id=item_id)
    item.delete()
  return redirect('kits_detail', user_id=user_id)

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
        recommendation_message = f"{user.name} can enjoy all variety of food options =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.woolworths.com.au/?utm_source=google&utm_medium=cpc&utm_campaign=WW-0001&cq_net=g&cq_src=GOOGLE&cq_cmp=Woolies_8458_BAU_Brand_Exact_Head%20Term%20Pure_WW-0001&cq_med=71700000071994282&cq_plac=&cq_term=woolies&ds_adt=&cq_plt=gp&cq_gclid=CjwKCAjwwr6wBhBcEiwAfMEQs0LTL0K9WQsjlfL0C7vkjsplhKqdyNsMYG53Eq9bYewVUZbH6x2TWhoCCrcQAvD_BwE&ds_de=c&ds_pc=&ds_cr=528130855897&ds_tid=aud-848956741194:kwd-13485966&ds_locphys=9071353&ds_pid=&cmpid=smsm:ds:GOOGLE:Woolies_8458_BAU_Brand_Exact_Head%20Term%20Pure_WW-0001:woolies&gad_source=1&gclid=CjwKCAjwwr6wBhBcEiwAfMEQs0LTL0K9WQsjlfL0C7vkjsplhKqdyNsMYG53Eq9bYewVUZbH6x2TWhoCCrcQAvD_BwE&gclsrc=aw.ds' title='shop'>Buy Food</a>")
    elif dietary_restrictions == 'FODMAP':
        recommendation_message = f"FODMAP food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://fodmapfriendly.com/fodmap_products/lewis-son-traditional-pickled-cucumbers-2/' title='shop'>FODMAP pickled cucumber</a>")
        recommendations.append("<a href='https://fodmapfriendly.com/fodmap_products/semper-choc-chip-cookies/' title='shop'>chocolate chips cookies</a>")
        recommendations.append("<a href='https://fodmapfriendly.com/fodmap_products/fodmapped-chicken-soup/' title='shop'>FODMAP chicken and vegetable soup</a>")
        recommendations.append("<a href='https://fodmapfriendly.com/fodmap_products/totopos/' title='shop'>Tortilla chips</a>")
        recommendations.append("<a href='https://fodmapfriendly.com/fodmap_products/fodmapped-for-you-coconut-bites-raspberry-vanilla/' title='shop'>Coconut bites</a>")
        recommendations.append("<a href='https://fodmapfriendly.com/certified-products/' title='shop'>Reference to other FODMAP food</a>")
    elif dietary_restrictions == 'Gluten Free':
        recommendation_message = f"Gluten Free food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.gfnation.com.au/products/ellys-salted-caramel-pop-140g?_pos=5&_sid=5e8a5aae7&_ss=r' title='shop'>Gluten-free salted caramel popcorn</a>")
        recommendations.append("<a href='https://www.gfnation.com.au/products/allrite-organic-rice-cakes-mini-30g' title='shop'>Gluten-free Rice cake</a>")
        recommendations.append("<a href='https://www.gfnation.com.au/products/amazonia-raw-protein-bars-triple-choc-brownie-1-x-40g' title='shop'>Gluten-free protein bar</a>")
        recommendations.append("<a href='https://www.gfnation.com.au/products/schar-digestive-biscuits-150g' title='shop'>Gluten-free digestive biscuits</a>")
        recommendations.append("<a href='https://www.gfnation.com.au/products/amisa-organic-gluten-free-buckwheat-crispbread-120g' title='shop'>Gluten-free crispbread</a>")
        recommendations.append("<a href='https://www.gfnation.com.au/collections/grocery-products' title='shop'>Reference to other Gluten Free food</a>")
    elif dietary_restrictions == 'Lactose Free':
        recommendation_message = f"Lactose Free food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.healthybeing.com.au/banana-joe-crispy-banana-chips-sea-salt-6x47g' title='shop'>Banana chips</a>")
        recommendations.append("<a href='https://www.healthybeing.com.au/mindful-foods-organic-activated-mixed-nuts-450g' title='shop'>Mixed nuts</a>")
        recommendations.append("<a href='https://www.healthybeing.com.au/yava-chocolate-vanilla-granola-bites-125g' title='shop'>Granola bites</a>")
        recommendations.append("<a href='https://www.healthybeing.com.au/mindful-foods-organic-activated-sunflower-seeds-225g' title='shop'>Sunflower seeds</a>")
        recommendations.append("<a href='https://www.healthybeing.com.au/gimme-organic-roasted-seaweed-snacks-teriyaki-6x5g' title='shop'>Seaweed snack</a>")
        recommendations.append("<a href='https://www.healthybeing.com.au/dietary/dairy-free/' title='shop'>Reference to other Lactose Free food</a>")
    elif dietary_restrictions == 'Nut Free':
        recommendation_message = f"Nut Free food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/products/blue-dinosaur-hand-baked-bite-berry-coconut-30g' title='shop'>Brownie</a>")
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/products/ceres-organics-gluten-free-coconut-wafer-rolls-original-80g' title='shop'>Wafer Rolls</a>")
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/products/eskal-gluten-free-pretzel-party-mix-300g' title='shop'>Pretzel</a>")
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/products/leda-mini-gluten-free-rice-cakes-dark-chocolate-60g' title='shop'>Rice cake</a>")
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/products/leda-triple-berry-baked-fruit-filled-gluten-free-bars'>Fruit bar</a>")
        recommendations.append("<a href='https://happytummies.com.au/collections/gluten-free-snacks/nut-free-ingredients' title='shop'>Reference to other Nut Free food</a>")
    elif dietary_restrictions == 'Vegan':
        recommendation_message = f"Vegan food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/natures-charm-vegan-calamari-130g' title='shop'>Vegan calamari</a>")
        
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/orgran-vegan-easy-egg-250g' title='shop'>Vegan egg</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/vego-bar-150-grams-vegan-chocolate-dairy-free-gluten-free' title='shop'>Hazelnut chocolate bar</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/km-foods-barbeque-vegan-jerky-70g' title='shop'>Vegan jerky</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/copy-of-dr-mcdougalls-pad-thai-noodle-soup-56g' title='shop'>Vegan Instant Noodle</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/' title='shop'>Reference to other Vegan food</a>")
    elif dietary_restrictions == 'Vegetarian':
        recommendation_message = f"Vegetarian food {user.name} might like =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/plantasy-food-the-good-soup-cock-a-leekie-30g' title='shop'>Leek soup</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/copy-of-dr-mcdougalls-pad-thai-noodle-soup-56g' title='shop'>Instant noodles</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/plantasy-foods-instant-potato-mash-mix-150g' title='shop'>Instant mash potato</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/the-british-crisp-co-cheese-onion-flavoured-crisps-40g' title='shop'>Cheese and onion crisps</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/collections/vegan-food-chocolate-cheese/products/plantasy-foods-mac-n-cheez-cheez-n-chive-200g' title='shop'>Mac and cheese</a>")
        recommendations.append("<a href='https://www.fivevegans.com.au/' title='shop'>Reference to other Vegetarian food</a>")
    else:
        recommendation_message = f"Complicated food restriction! Beware with choosing food for {user.name} =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://goodnessme.com.au/collections/dairy-free' title='shop'>Reference for complicated dietary restriction</a>")
    
    recommendations.append("")
    
    recommendations.append("Personal Care items =>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/personal-care-hygiene/abena-shower-bath-soap-with-pump-500ml-each/' title='shop'>Soap</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/personal-care-hygiene/dermaveen-oatmeal-shampoo-250ml-each/' title='shop'>Shampoo</a>")
    recommendations.append("<a href='https://supportsmallbusinessaustralia.com.au/products/sunslayer-spf-50-face-body-natural-physical-sunscreen-reef-safe-100ml/' title='shop'>Sunscreen</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/paper-products/toilet-paper-roll-kleenex-soft-jumbo-5749-6-x-300-metres-carton/' title='shop'>Toilet paper</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/personal-care-hygiene/colgate-toothpaste-120gm-each/' title='shop'>Tooth paste</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/personal-care-hygiene/colgate-toothbrush-zig-zag-medium-each/' title='shop'>Tooth brush</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/personal-care-hygiene/aqium-hand-sanitiser-gel-1-litre-bottle-each/' title='shop'>Hand sanitizer</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/incontinence-aids/tena-pad-instadry-long-length-6-pack/' title='shop'>Incontinence supplies (diapers, pads)</a>")
    recommendations.append("<a href='https://everythingaustralian.com.au/' title='shop'>Extra clothing appropriate for the climate</a>")
    recommendations.append("<a href='https://www.alphamedicalsolutions.com.au/' title='shop'>Reference to other Personal Care Items</a>")
    
    recommendations.append("")
    
    recommendations.append("Emergency Necessity =>")
    recommendations.append("Important Document")
    
    recommendations.append("<a href='https://www.aussiestormshop.com.au/15-in-1-multi-tool' title='shop'>Knife</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/15-in-1-multi-tool' title='shop'>Can opener</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/speras-powerbank' title='shop'>Phone charger</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/Nitecore-EC23-1800-Lumen-Flashlight' title='shop'>Flashlights</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/?rf=kw&kw=eneloop' title='shop'>Spare batteries</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/clearance-combat-tactical-glove' title='shop'>Sturdy gloves</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/P2-/-N95-Mask-2-pack' title='shop'>Face mask</a>")
    recommendations.append("<a href='https://www.bloomsthechemist.com.au/Bodichek-First-Aid-Kit-62-Pieces/' title='shop'>First aid kit</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/products/digitech-9-band-shortwave-radio-7' title='shop'>Battery operated radio</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/clearance-dd-hammocks-scarba-sleeping-bag-regular' title='shop'>Blankets or sleeping bags</a>")
    recommendations.append("<a href='https://www.aussiestormshop.com.au/' title='shop'>Reference to other emergency necessary tools</a>")
    
    recommendations.append("")
    
    medical_conditions = user.medical_conditions
    if medical_conditions != "No Medical Conditions":
        recommendation_message = f"Medical Condition => {medical_conditions}"
        recommendations.append(recommendation_message)
        recommendations.append(f"Don't forget to pack medicine for {user.name}'s {medical_conditions}!")
        recommendations.append("<a href='https://www.bloomsthechemist.com.au/' title='shop'>Reference to Medicine</a>")
        
    recommendations.append("")
    
    disability = user.disability
    if disability == "Disable":
        recommendation_message = f"Disabled?! Does {user.name} needs following items? =>"
        recommendations.append(recommendation_message)
        recommendations.append("<a href='https://www.hearingaidsspecialist.com.au/hearing-services?gad_source=1&gclid=CjwKCAjwwr6wBhBcEiwAfMEQs5CCW3dxGiy4nL5tB93PbIaY_NQ4O1Opy5Qfrf-t5LYSyLlKK50DVhoCKwcQAvD_BwE' title='shop'>Communication Aids</a>")
        recommendations.append("<a href='https://www.mobilityandwellness.com.au/' title='shop'>Mobility Aids</a>")
        recommendations.append("<a href='https://medimart.com.au/' title='shop'>Specialized products</a>")
        recommendations.append("<a href='https://askned.com.au/catalog?gad_source=1&gclid=CjwKCAjwwr6wBhBcEiwAfMEQs0-e0gVm_0er9mlY09OmFTgPKqKCvR-9lY65EVKeI7IWAlb3rgU30RoCbwYQAvD_BwE' title='shop'>Reference to other Supplies</a>")
    
    return render(request, 'recommendations.html', {'recommendations': recommendations, 'user': user})


# In your views.py
from django.shortcuts import render
from .models import ExpiringItem

def notifications(request):
    expiring_items = ExpiringItem.objects.all()
    return render(request, 'notifications.html', {'expiring_items': expiring_items})
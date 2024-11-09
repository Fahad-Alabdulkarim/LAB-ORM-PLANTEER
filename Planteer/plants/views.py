from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from django.core.paginator import Paginator
from .models import Plant
from .forms import PlantForm


# Create your views here.


def all_plants(request):
    plants = Plant.objects.all()
    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')
    if category:
        plants = plants.filter(category=category)
    if is_edible:
        plants = plants.filter(is_edible=(is_edible == 'true'))
    paginator = Paginator(plants, 6)
    page_number = request.GET.get('page')
    page_plant = paginator.get_page(page_number)
    return render(request, 'plants/all_plant.html', {'page_plant': page_plant})

def plant_detail(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:4]
    return render(request, 'plants/plant_detail.html', {'plant': plant, 'related_plants': related_plants})




def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()
    return render(request, 'plants/add_plant.html', {'form': form})




def update_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)

    if request.method == "POST":
        plant.name = request.POST["name"]
        plant.about = request.POST["about"]
        plant.category = request.POST["category"]
        plant.is_edible = request.POST["is_edible"] == "True"
        
        if "image" in request.FILES:
            plant.image = request.FILES["image"]
        
        plant.save()  

        return redirect("plant_detail", plant_id=plant.id)  
    
    return render(request, "plants/update_plant.html", {"plant": plant})





def delete_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('all_plants')
    return redirect('plant_detail', plant_id=plant.id)



def search_plants(request):
    categories = [
        Plant.CategoryChoices.TREE,
        Plant.CategoryChoices.FRUIT,
        Plant.CategoryChoices.VEGETABLE,
        Plant.CategoryChoices.FLOWER,
    ]

    if "search" in request.GET and len(request.GET["search"]) >= 1:
        search_query = request.GET["search"]
        plants = Plant.objects.filter(name__icontains=search_query) 
        
        if "category" in request.GET:
            category = request.GET["category"]
            plants = plants.filter(category=category)

        if "order_by" in request.GET:
            order_by = request.GET["order_by"]
            if order_by == "created_at":
                plants = plants.order_by("-created_at")
            elif order_by == "is_edible":
                plants = plants.order_by("-is_edible")
    else:
        plants = []  

    return render(request, "plants/search.html", {"plants": plants ,'categories': categories})




from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from .models import Consume, Food
from .models import Image
from .form import ImageForm


@login_required
def index(request):

    if request.method == "POST":
        # is_private = request.POST.get('is_private', False)
        food_consumed=request.POST.get('food_consumed')
        # food_consumed=request.POST['food_consumed']
        consume=Food.objects.get(name=food_consumed)
        user=request.user
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        foods=Food.objects.all()
    else:
        foods=Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'foods':foods, 'consumed_food':consumed_food}) 



def delete_consume(request,id):
    consume_food=Consume.objects.get(id=id)
    if request.method=='POST':
        consume_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')
# Create your views here.
@login_required
def add_food(request):
    
    if request.method=='POST':
        form=ImageForm(data=request.POST,files=request.FILES)
        food_name=request.POST['name']
        carbs = request.POST['carbs']
        fats = request.POST['fats']
        protein= request.POST['protein']
        calorie = request.POST['calorie']
        
        
    
        if form.is_valid():
            form.save()
            obj=form.instance
            food_img=obj.image.url
            food_add=Food(name=food_name,carbs=carbs,protien=protein,fats=fats,calorie=calorie,food_img=food_img)
            food_add.save()
            return render(request,"myapp/upload.html",{"obj":obj})

            # return render(request,"users/upload.html",)
    else:
         form=ImageForm()
         img=Image.objects.all()  
         return render(request,'myapp/add.html',{"img":img,"form":form})
        
    # return render(request,'myapp/add.html',{"obj":obj})


def catalog(request):
     foods=Food.objects.all()
     return render(request,'myapp/catalog.html',{'foods':foods,})

def update_consume(request,id):
    upfood = Consume.objects.get(id=id)
    name=upfood.food_consumed.name
    

    if request.method == 'POST':
        upfood.food_consumed.carbs = request.POST['carbs']
        upfood.food_consumed.fats = request.POST['fats']
        upfood.food_consumed.protien= request.POST['protein']
        upfood.food_consumed.calorie = request.POST['calorie']
        upfood.save()
        return redirect('/')
    return render(request,'myapp/update.html',{'name':name,'id':id})


# def upload(request):
#     if request.method == "POST":
        
#     else:
#         form=ImageForm()
#         img=Image.objects.all()
#         return render(request,"users/upload.html",{"img":img,"form":form})
  

    

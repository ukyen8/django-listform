from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List
from django.core.exceptions import ValidationError
from .forms import ItemForm, EMPTY_ITEM_ERROR

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    print("list_id : ", list_id)
    form = ItemForm()
    if request.method == 'POST':
        print(request.POST)
        form = ItemForm(data=request.POST)
        print("form is post ", form, form.is_valid())
        if form.is_valid():
            print("form redirect ", list_)
            form.save(for_list=list_)
            print("finish form save ", list_)
            return redirect(list_)
    print("form is get ", form, form.is_valid())
    print("finish view")
    return render(request, 'list.html', {'list': list_, "form": form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


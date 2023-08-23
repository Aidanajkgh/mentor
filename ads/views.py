from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
import pkg_resources


from .models import Ads, Category
from .forms import AdForm


def category_list(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories
    }
    return render(request, 'category.html', context=context)


def ads_list(request):
    all_ads = Ads.objects.all()
    context = {
        'all_ads': all_ads
    }
    return render(request, 'index.html', context=context)


def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ads-list')
    else:
        form_of_ad = AdForm()
    return render(request, 'create_ad.html', {'form_of_ad': form_of_ad })


def update_ad(request, pk):
    ad = get_object_or_404(Ads, id=pk)

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Success Edited </h1>')
        else:
            return HttpResponse('<h1> Error Edited </h1>')
    else:
        form_of_ad = AdForm()
        return render(request, 'update_ad.html', {'form_of_ad': form_of_ad })


def retrieve_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    context = {
        "ad": ad
    }
    return render(request, 'retrieve_ad.html', context=context)



def delete_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, 'Объект успешно удален.')
    return redirect('ads-list')


from typing import Any, Dict
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.utils import timezone
import datetime
from users.models import User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


from .models import Ads, Category
from .forms import AdForm


def category_list(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories': all_categories
    }
    return render(request, 'category.html', context=context)


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'


class AdsDetailView(DetailView):
    template_name = 'retrieve_ad.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'


class AdsDeleteView(DeleteView):
    template_name = 'delete_ad.html'
    queryset = Ads.objects.all()
    success_url = reverse_lazy('ads-list')


class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self) -> str:
        return reverse('ads-list')


class AdsCreateView(CreateView):
    template_name = 'create_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self) -> str:
        return reverse('ads-list')
    




















# class AdsView(View):
#     template_name = 'index.html'
#     def get(self, request, *args, **kwargs ):
#         all_ads = Ads.objects.all()
#         return render(request, self.template_name, {'all_ads': all_ads})

    #all_ads - Ads.objects.filter(created_at__lte=timezone.now())
    #all_ads = Ads.objects.filter(title__contains="test")
    #all_ads = Ads.objects.filter(owner__isnull=False)
    #all_ads = Ads.objects.filter(description__icontains=('s')).filter(created_at__year=2023)
    #all_ads = Ads.objects.filter(price__in=[3000, 2500, 343, 200])
    # aidana = User.objects.get(username="aidana")
    # all_ads = Ads.objects.filter(owner=aidana)


# def create_ad(request):
#     if request.method == 'POST':
#         form = AdForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('ads-list')
#     else:
#         form_of_ad = AdForm()
#     return render(request, 'create_ad.html', {'form_of_ad': form_of_ad })


# def update_ad(request, pk):
#     ad = get_object_or_404(Ads, id=pk)

#     if request.method == 'POST':
#         form = AdForm(request.POST, request.FILES, instance=ad)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1> Success Edited </h1>')
#         else:
#             return HttpResponse('<h1> Error Edited </h1>')
#     else:
#         form_of_ad = AdForm()
#         return render(request, 'update_ad.html', {'form_of_ad': form_of_ad })
    

# def retrieve_ad(request, pk):
#     ad = Ads.objects.get(id=pk)
#     context = {
#         "ad": ad
#     }
#     return render(request, 'retrieve_ad.html', context=context)


# def delete_ad(request, pk):
#     ad = Ads.objects.get(id=pk)
#     ad.delete()
#     messages.success(request, 'Объект успешно удален.')
#     return redirect('ads-list')
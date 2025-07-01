from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed



# Create your views here.

class CatList(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.count()
        cat_list = Cat.objects.all()
        ctx = {'breed_count': breed_count, 'cats_list': cat_list}
        return render(request, 'cats/cats_list.html', ctx)


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {'breed_list': breed_list}
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cats:cats_list")


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cats:cats_list")

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cats:cats_list")

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cats_list')


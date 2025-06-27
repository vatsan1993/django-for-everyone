from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make
# from autos.forms import MakeForm
# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.count()
        autos_list = Auto.objects.all()
        ctx = {'make_count': make_count, 'auto_list': autos_list}
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        make_list = Make.objects.all()
        ctx = {'make_list': make_list}
        return render(request, 'autos/make_list.html', ctx)

# class MakeCreate(LoginRequiredMixin, View):
#     template_name = 'autos/make_form.html'
#     success_url = reverse_lazy('autos:all')
#     def get(self, request):
#         # create an empty form
#         form = MakeForm()
#         ctx = {'form': form}
#         # render the form with no data
#         return render(request, self.template_name, ctx)

#     def post(self, request):
#         # fill the form class with the attributes form the request
#         form = MakeForm(request.POST)
#         # if the form is not valid, return back to the same form with errors
#         # Errors are auto populated due to validations
#         if not form.is_valid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)

#         # if no error save the form data
#         make = form.save()
#         # redirect to success url.
#         return redirect(self.success_url)


# class MakeUpdate(LoginRequiredMixin, View):
#     template = "autos/make_form.html"
#     success_url = 'autos/make_form.html'
#     model = Make

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk = pk)
#         form = MakeForm(instance = make)
#         ctx = {'form': form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk = pk)
#         form = MakeForm(instance = make)
#         if not form.isvalid():
#             ctx = {'form': form}
#             return render(request, self.template, ctx)
#         form.save()
#         return redirect(self.success_url)

# class MakeDelete(LoginRequiredMixin, View):
#     template = "autos/make_confirm_delete.html"
#     success_url = reverse_lazy('autos:all')
#     model = Make

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk = pk)
#         ctx = {'make': make}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk = pk)
#         make.delete()
#         return render(self.success_url)


# these classes does the same thing as above.
# Note the template files needs to have specific conventions
# Also forms.py is not needed anymore

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy("autos:all")


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy("autos:all")

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy("autos:all")

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


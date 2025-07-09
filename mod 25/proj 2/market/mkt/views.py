from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from mkt.models import Ad
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from mkt.forms import CreateForm


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


# Using a custom view instead of using the OwnerCreateView
# class AdCreateView(OwnerCreateView):
class AdCreateView(LoginRequiredMixin, View):
    # model = Ad
    template_name = 'mkt/ad_form.html'
    # List the fields to copy from the Article model to the Article form
    # fields = ['title', 'text', 'price']
    success_url = reverse_lazy('mkt:all')
    def get(self, request):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)


    def post(self, request, pk = None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit = False)
        ad.owner = request.user
        ad.save()

        return redirect(self.success_url)

class AdUpdateView(LoginRequiredMixin, View):
    # model = Ad
    # fields = ['title', 'text', 'price']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']
    template_name = 'mkt/ad_form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id = pk, owner = request.user)
        form = CreateForm(instance = ad)
        ctx = {'form' : form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk = None):
        ad = get_object_or_404(Ad, id = pk, owner = request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad )

        if not form.is_valid():
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit = False)
        ad.owner = request.user
        ad.save()
        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
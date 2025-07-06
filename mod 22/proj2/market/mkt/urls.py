from django.urls import path, reverse_lazy
from . import views

app_name='mkt'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='detail'),
    path('ad/create',
        views.AdCreateView.as_view(success_url=reverse_lazy('mkt:all')), name='create'),
    path('ad/<int:pk>/update',
        views.AdUpdateView.as_view(success_url=reverse_lazy('mkt:all')), name='update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('mkt:all')), name='delete'),
]
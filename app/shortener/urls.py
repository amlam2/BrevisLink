from django.urls import path
from . import views
#limit class views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

app_name = 'shortener'
urlpatterns = [
    path('', view=views.IndexView.as_view(), name='index'),
    path('shortener/new/', view=login_required(views.create_urls), name='new'),
    # path('shortener/update/<int:pk>/', view=views.update_urlentry, name="update"),
    # path('shortener/delete/<int:pk>/', view=login_required(views.DeleteUrlentry.as_view(), login_url=reverse_lazy('auth:login')), name='delete'),
    path('details/<int:pk>/', view=login_required(views.DetailView.as_view(), login_url=reverse_lazy('auth:login')), name='detail'),
    path('shortener/<int:pk>/statistics/', view=login_required(views.StatisticsView.as_view(), login_url=reverse_lazy('auth:login')), name='statistics'),
    # path('shortener/<int:pk>/results/get', view=views.ClicksView.as_view(), name='get'),
    path('<str:hash>/', view=views.add_lead_and_redirect, name='short'),
]

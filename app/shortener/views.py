from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from .forms import UrlentryForm
from .models import Urlentry
from .models import Leads


class IndexView(generic.ListView):
    template_name = 'shortener/index.html'
    context_object_name = 'links_list'
    def get_queryset(self):
        return Urlentry.objects.filter(created_at__lte=timezone.now()).order_by('-created_at') #[:10]


class DetailView(generic.DetailView):
    model = Urlentry
    template_name = 'shortener/detail.html'


class StatisticsView(generic.DetailView):
    model = Urlentry
    template_name = 'shortener/statistics.html'


@login_required(login_url=reverse_lazy('auth:login'))
def create_urls(request):
    urlentry_formset = inlineformset_factory(Urlentry, Leads, fields=['clicked_host'], extra=0)
    formset = urlentry_formset()
    if request.method == "POST":
        urlentry_form = UrlentryForm(request.POST, hide_condition=True)
        if urlentry_form.is_valid():
            urlentry = urlentry_form.save(commit=False)
            urlentry.created_at = timezone.now()
            urlentry.owner = request.user
            urlentry.save()
            formset = urlentry_formset(request.POST, instance=urlentry)
            if formset.is_valid():
                formset.save()
                return redirect('shortener:detail', pk=urlentry.pk)
        else:
            return HttpResponse('This link already exists.')
    else:
        urlentry_form = UrlentryForm(hide_condition=True)
        formset = urlentry_formset()
        return render(request, 'shortener/new_link.html',{
                                                            'urlentry_form': urlentry_form,
                                                            'formset': formset
                                                         })


def add_lead_and_redirect(request, hash):
    urlentry = get_object_or_404(Urlentry, url_hash=hash)
    Leads(
            urlentry = urlentry,
            clicked_host = request.META['HTTP_HOST'],
            clicked_conf = request.headers.get('User-Agent'),
            clicked_ip = request.META['REMOTE_ADDR']
         ).save()
    return HttpResponseRedirect(urlentry.full_url)

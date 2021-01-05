from display.forms.agencies_form import CreateAgencyForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

from youtubeapi.models.agency import Agency

def agencyIndex(request):

    form = CreateAgencyForm()

    if request.method == 'POST':
        form = CreateAgencyForm(request.POST, request.FILES)
        if form.is_valid():
            agency = form.save()
            name = form.cleaned_data.get('name')

            messages.success(request, 'Added agency: ' + name)
            return HttpResponseRedirect(reverse('agency-index'))

    agencies = Agency.objects.all()
    paginator = Paginator(agencies, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj':page_obj,
        'form':form,
    }

    return render(request, 'agency/index.html', context=data)

def DeleteAgency(request, id):

    agency = Agency.objects.get(pk=id)
    agency.delete()
    messages.success(request, 'Deleted agency %s.' % agency)
    return HttpResponseRedirect(reverse('agency-index'))
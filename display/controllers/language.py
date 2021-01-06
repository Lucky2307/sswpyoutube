from display.forms.language_form import CreateLanguageForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
login_required = login_required(login_url='user:login')

from youtubeapi.models.language import Language

@login_required
def languageIndex(request):

    form = CreateLanguageForm()

    if request.method == 'POST':
        form = CreateLanguageForm(request.POST, request.FILES)
        if form.is_valid():
            language = form.save()
            name = form.cleaned_data.get('name')

            messages.success(request, 'Added language: ' + name)
            return HttpResponseRedirect(reverse('language-index'))

    languages = Language.objects.all()
    paginator = Paginator(languages, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj':page_obj,
        'form':form,
    }

    return render(request, 'language/index.html', context=data)

@login_required
def DeleteLanguage(request, id):

    language = Language.objects.get(pk=id)
    language.delete()
    messages.success(request, 'Deleted language %s.' % language)
    return HttpResponseRedirect(reverse('language-index'))
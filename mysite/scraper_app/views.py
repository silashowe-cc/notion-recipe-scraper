from django.shortcuts import render
from django.http import HttpResponse
from .forms import ScraperForm
from .scraper import main as scraper
from django.shortcuts import redirect

# Create your views here.
# These are used to return something to a http request To map them, we also need to set up something with URLs

def index (request):
    if request.method == 'POST':
        form = ScraperForm(request.POST)
        if form.is_valid():
            recipe_url = form.cleaned_data['recipe_url']
            token = form.cleaned_data['token']
            db = form.cleaned_data['dbid']
            icon = form.cleaned_data['icon']
            scrape_res = scraper(recipe_url, token, db, icon)
            return HttpResponse(scrape_res)
    else:
        form = ScraperForm()
    return render(request, 'scraper_app/index.html', {'form': form})

def redirect_view(request):
    return redirect('/scraper')

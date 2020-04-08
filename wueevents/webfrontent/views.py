from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Websites

# Create your views here.


def read_all(request):
    import pdb; pdb.set_trace()
    websites = get_list_or_404("Websites")
    render(request=request, template_name="webfrontend/read_all_websites.html", context={
        "websites", websites
    })


def read(request, id):
    website = get_object_or_404("Websites", pk=id)
    return render(request=request, template_name="webfrontent/read_website.html")

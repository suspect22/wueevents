from django.shortcuts import render, get_list_or_404, get_object_or_404


def read_all(request):
    websites = get_list_or_404("Websites")
    render(request=request,
           template_name="webfrontend/read_all_websites.html",
           context={"websites", websites}
           )


def read(request, id):
    website = get_object_or_404("Websites", pk=id)
    return render(request=request,
                  template_name="webfrontent/read_website.html",
                  context={"websites", website}
                  )

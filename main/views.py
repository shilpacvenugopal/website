from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html') # Assuming index.html is in templates/

def about_view(request):
    return render(request, 'about.html') # Assuming about.html is in templates/

def service_view(request):
    return render(request, 'service.html')

def blog_grid_view(request):
    return render(request, 'blog.html')

def blog_detail_view(request):
    return render(request, 'detail.html')

def pricing_view(request):
    return render(request, 'price.html')

def features_view(request):
    return render(request, 'feature.html')

def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')

def quote_view(request):
    return render(request, 'quote.html')

def contact_view(request):
    return render(request, 'contact.html')
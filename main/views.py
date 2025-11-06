from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import InvestorQuery,Job
from .serializers import InvestorQuerySerializer



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import InvestorQuery  # Only if you have this model

@csrf_exempt
@require_http_methods(["GET", "POST"])
def submit_investor_query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            area_of_interest = data.get('area_of_interest')
            message = data.get('message')

            # ✅ Save to database (only if you have the model)
            InvestorQuery.objects.create(
                name=name, phone=phone, email=email, area_of_interest=area_of_interest, message=message
            )

            return JsonResponse({'status': 'success', 'message': 'Data saved successfully!'}, status=201)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    elif request.method == 'GET':
        # ✅ Return all investor entries
        investors = list(InvestorQuery.objects.values())
        return JsonResponse({'status': 'success', 'data': investors}, safe=False)

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


def get_jobs(request, category):
    jobs = Job.objects.filter(category=category)
    data = [
        {
            "title": job.title,
            "description": job.description or "",
            "posted_on": job.posted_on.strftime("%Y-%m-%d")
        }
        for job in jobs
    ]
    return JsonResponse({"jobs": data})



from .models import JobApplication

@csrf_exempt
def submit_application(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        resume = request.FILES.get('resume')
        print(request.POST)

        application = JobApplication.objects.create(
            role=role,
            name=name,
            email=email,
            phone=phone,
            qualification=qualification,
            resume=resume
        )
        print(application)
        return JsonResponse({'success': True, 'message': 'Application submitted successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

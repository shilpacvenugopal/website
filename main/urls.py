from django.urls import path
from . import views

app_name = 'BYN' # Important for namespacing URLs


urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('service/', views.service_view, name='service'),
    path('blog/', views.blog_grid_view, name='blog_grid'),
    path('blog/detail/', views.blog_detail_view, name='blog_detail'), # Example for nested paths
    path('price/', views.pricing_view, name='pricing'),
    path('feature/', views.features_view, name='features'),
    path('team/', views.team_view, name='team'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
    path('quote/', views.quote_view, name='quote'),
    path('contact/', views.contact_view, name='contact'),
]

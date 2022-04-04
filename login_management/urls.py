from django.urls import path
from login_management import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.HomePageView.as_view()),
    path('dashboard/',views.dashboard),
    path('checkout/',views.checkout),
    
    
]
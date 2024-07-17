from django.urls import path
import include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('swag/',views.about, name='about'),
    path('swag/me/',views.footer, name='footer'),
    path('swag/me/and/you/',views.hero, name='hero'),
]
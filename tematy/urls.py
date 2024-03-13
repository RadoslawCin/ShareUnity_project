"""
URL configuration for shareunity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'tematy'

urlpatterns = [
    #Główna
    path('',views.index, name='index'),

    #Informacje
    path('About_us/', views.About_us, name='About_us'),
    path('Contact/', views.Contact, name='Contact'),
    path('radoslaw', views.radoslaw, name='radoslaw'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),

    #Wyświetlanie kategorii Blogów
    path('kategorie/', views.kategorie, name='kategorie'),
    #Pojedyńczy temat
    path('kategorie/<int:temat_id>/', views.temat, name='temat'),
    #Nowy temat użytkownika
    path('nowy_temat/', views.nowy_temat, name='nowy_temat'),
    #Nowy wpis użytkownika
    path('nowy_wpis/<int:temat_id>/', views.nowy_wpis, name='nowy_wpis'),
    #Edycja wpisu
    path('edycja_wpisu/<int:wpisy_id>', views.edycja_wpisu, name='edycja_wpisu'),
    # Usuń wpis
    path('usun_wpis/<int:wpisy_id>/', views.delete_entry, name='usun_wpis'),
    # Usuń blog
    path('usun_blog/', views.delete_blog, name='usun_blog'),

    #Użytkownik
    path('moj_blog/', views.moj_blog, name='moj_blog'),
    path('moja_strona/', views.my_page, name='moja_strona'),
    path('zmien_haslo/', views.zmien_haslo, name='zmien_haslo'),
    path('usun_konto/', views.usun_konto, name='usun_konto'),


]

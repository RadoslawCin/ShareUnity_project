from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.db.models import Max
from .models import Tematy, Wpisy
from .forms import TopicForm, EntryForm

def index(request):
    najnowsze_wpisy = Wpisy.objects.order_by('-date_added')[:5]
    najnowsi_uzytkownicy = User.objects.exclude(username='admin').order_by('-date_joined')[:5]
    context = {'najnowsze_wpisy': najnowsze_wpisy, 'najnowsi_uzytkownicy': najnowsi_uzytkownicy}
    return render(request, "tematy/index.html", context)

def About_us(request):
    return render(request, "tematy/About_us.html")

def Contact(request):
    return render(request, "tematy/Contact.html")

def radoslaw(request):
    return render(request, "tematy/radoslaw.html")

def privacy_policy(request):
    return render(request, "tematy/privacy_policy.html")

def terms_of_service(request):
    return render(request, "tematy/terms_of_service.html")

@login_required
def delete_entry(request, wpisy_id):
    wpis = Wpisy.objects.get(id=wpisy_id)

    if request.method == 'POST':
        #Czy jest ownerem?
        if request.user != wpis.temat.owner:
            messages.error(request, "Nie masz uprawnień do usunięcia tego wpisu.")
            return redirect('tematy:temat', temat_id=wpis.temat.id)


        wpis.delete()
        messages.success(request, "Wpis został usunięty.")
        return redirect('tematy:temat', temat_id=wpis.temat.id)

    return render(request, 'tematy/usun_wpis_confirm.html', {'wpis': wpis})

@login_required
@user_passes_test(lambda u: hasattr(u, 'blog_owner'), login_url='tematy:kategorie')
def delete_blog(request):
    if request.method == 'POST':

        if not hasattr(request.user, 'blog_owner'):
            messages.error(request, "Nie masz bloga do usunięcia.")
            return redirect('tematy:moj_blog')


        request.user.blog_owner.delete()
        messages.success(request, "Twój blog został usunięty wraz z wpisami.")
        return redirect('tematy:moj_blog')

    return render(request, 'tematy/usun_blog_confirm.html')

@login_required
def my_page(request):
    return render(request, 'tematy/moja_strona.html')

@login_required
def zmien_haslo(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Twoje hasło zostało pomyślnie zmienione!')
            return redirect('tematy:moja_strona')
        else:
            messages.error(request, 'Proszę poprawić błędy poniżej.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'tematy/zmien_haslo.html', {'form': form})

@login_required
def usun_konto(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, 'Twoje konto zostało usunięte.')
        return redirect('tematy:index')
    return render(request, 'tematy/usun_konto.html')

@login_required
def moj_blog(request):
    tematy_uzytkownika = Tematy.objects.filter(owner=request.user)
    context = {'tematy_uzytkownika': tematy_uzytkownika}
    return render(request, 'tematy/moj_blog.html', context)

@login_required
def kategorie(request):
    kategorie = Tematy.objects.annotate(
        latest_entry_date=Max('wpisy__date_added')
    ).order_by('-latest_entry_date')


    for temat in kategorie:
        temat.is_new = False

        if temat.latest_entry_date:
            temat.is_new = (timezone.now() - temat.latest_entry_date) <= timedelta(days=2)

    context = {'kategorie': kategorie}
    return render(request, 'tematy/kategorie.html', context)

@login_required
def temat(request, temat_id):
    temat = Tematy.objects.get(id=temat_id)
    wpisy = Wpisy.objects.filter(temat=temat).order_by('-date_added')
    context = {'temat': temat, 'wpisy': wpisy}
    return render(request, 'tematy/temat.html', context)

@login_required
def nowy_temat(request):
    if hasattr(request.user, 'blog_owner'):
        return redirect('tematy:kategorie')

    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_temat = form.save(commit=False)
            new_temat.owner = request.user
            new_temat.save()
            return redirect('tematy:moj_blog')

    context = {'form': form}
    return render(request, 'tematy/nowy_temat.html', context)

@login_required
def nowy_wpis(request, temat_id):
    temat = Tematy.objects.get(id=temat_id)

    if request.user != temat.owner:
        messages.error(request, "Nie masz uprawnień do dodawania wpisów do tego bloga.")
        return redirect('tematy:kategorie')

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            nowy_wpis = form.save(commit=False)
            nowy_wpis.temat = temat
            nowy_wpis.save()
            return redirect('tematy:temat', temat_id=temat_id)

    context = {'temat': temat, 'form': form}
    return render(request, 'tematy/nowy_wpis.html', context)

@login_required
def edycja_wpisu(request, wpisy_id):
    wpis = Wpisy.objects.get(id=wpisy_id)
    temat = wpis.temat

    if request.user != wpis.temat.owner:
        messages.error(request, "Nie masz uprawnień do edycji tego wpisu.")
        return redirect('tematy:temat', temat_id=temat.id)

    if request.method != 'POST':
        form = EntryForm(instance=wpis)
    else:
        form = EntryForm(instance=wpis, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tematy:temat', temat_id=temat.id)

    context = {'wpis': wpis, 'temat': temat, 'form': form}
    return render(request, 'tematy/edycja_wpisu.html', context)


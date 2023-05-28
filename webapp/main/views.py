from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import *

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect("create_basket")
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = User.objects.get(id=request.user.id)
    context = {"user":user}
    return render(request, "main/profile.html", context)

def movement_info(request):
    movement = Movement.objects.all()
    context = {"movement": movement}
    return render(request, "main/table.html", context)


def company_view(request):
    company = Company.objects.all()
    context = {"company": company}
    return render(request, "main/company.html", context)


def room_view(request):
    room = Room.objects.all()
    context = {"room": room}
    return render(request, "main/room.html", context)


def section_view(request):
    section = Section.objects.all()
    context = {"section": section}
    return render(request, "main/section.html", context)


def create_mov(request):
    error = ''
    if request.method == 'POST':
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table')

        else:
            error = 'Check the data for correct input'

    form = MovementForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_mov.html', data)


def delete_movement(request, pk):
    if request.user.is_authenticated:
        movement = Movement.objects.get(id=pk)
        movement.delete()
        return redirect('table')
    else:
        return redirect('table')


class UpdateMovement(UpdateView):
    model = Movement
    template_name = 'main/create_mov.html'
    fields = ["date", "user_name", "rooms", "company"]
    success_url = reverse_lazy("table")


def create_company(request):
    error = ''
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')

        else:
            error = 'Check the data for correct input'

    form = CompanyForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_company.html', data)


def delete_company(request, pk):
    if request.user.is_authenticated:
        company = Company.objects.get(id=pk)
        company.delete()
        return redirect('company')
    else:
        return redirect('company')


class UpdateCompany(UpdateView):
    model = Company
    template_name = 'main/create_company.html'
    fields = ["company_name"]
    success_url = reverse_lazy("company")



def create_room(request):
    error = ''
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room')

        else:
            error = 'Check the data for correct input'

    form = RoomForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_room.html', data)


def delete_room(request, pk):
    if request.user.is_authenticated:
        room = Room.objects.get(id=pk)
        room.delete()
        return redirect('room')
    else:
        return redirect('room')


class UpdateRoom(UpdateView):
    model = Room
    template_name = 'main/create_room.html'
    fields = ["room_name"]
    success_url = reverse_lazy("room")


def create_section(request):
    error = ''
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section')

        else:
            error = 'Check the data for correct input'

    form = SectionForm()
    data = {
        'form': form,
    }
    return render(request, 'main/create_section.html', data)


def delete_section(request, pk):
    if request.user.is_authenticated:
        section = Section.objects.get(id=pk)
        section.delete()
        return redirect('section')
    else:
        return redirect('section')


class UpdateSection(UpdateView):
    model = Section
    template_name = 'main/create_section.html'
    fields = ["name", "leader"]
    success_url = reverse_lazy("section")

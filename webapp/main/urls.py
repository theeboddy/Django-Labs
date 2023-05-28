from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("table/", movement_info, name="table"),
    path("company/", company_view, name="company"),
    path("room/", room_view, name="room"),
    path("section/", section_view, name="section"),
    path("create_mov/", create_mov, name="create_mov"),
    path('update_mov/<int:pk>', UpdateMovement.as_view(), name='update_mov'),
    path('delete_mov/<int:pk>', delete_movement, name='delete_mov'),
    path("create_company/", create_company, name="create_company"),
    path('update_company/<int:pk>', UpdateCompany.as_view(), name='update_company'),
    path('delete_company/<int:pk>', delete_company, name='delete_company'),
    path("create_room/", create_room, name="create_room"),
    path('update_room/<int:pk>', UpdateRoom.as_view(), name='update_room'),
    path('delete_room/<int:pk>', delete_room, name='delete_room'),
    path("create_section/", create_section, name="create_section"),
    path('update_section/<int:pk>', UpdateSection.as_view(), name='update_section'),
    path('delete_section/<int:pk>', delete_section, name='delete_section'),
]

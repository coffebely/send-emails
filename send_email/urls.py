from django.urls import path
from .views import upload_file, LoginUserView, logout_user



urlpatterns = [
    path('', upload_file, name='send_email'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]

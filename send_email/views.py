from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import File, Log
from .handler import handler, time_now, limit
from .logs import get_logs, delivered


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = File(file=request.FILES['file'])
            instance.save()

            time_start = time_now()
            lim = limit(str(instance.file))

            if not handler(str(instance.file)):
                return render(request, 'send_email/upload_file.html', {'form': form, 'error': True})
            else:
                logs = get_logs(time_start, lim).json()
                logger = Log(log=logs, file=instance)
                logger.save()
                delivered_message = delivered(logs)
                return render(request, 'send_email/logs.html', {'logs': logs['items'], 'delivered': delivered_message})

    else:
        form = UploadFileForm()
    return render(request, 'send_email/upload_file.html', {'form': form, 'error': False})


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'send_email/login.html'


def logout_user(request):
    logout(request)
    return redirect('send_email')

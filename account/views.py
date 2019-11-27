from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from .models import Patient, Specialist
from activity.models import Appointment, History

User = get_user_model()


def index(request):
    return render(request, 'account/index.html')


def sign_up(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create(
        email=email,
        name=name
    )

    user.is_patient = True
    user.set_password(password)
    user.save()

    Patient.objects.create(user=user)

    return redirect('/', request)


def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    if user:
        login(request, user)
        return redirect('/', request)
    return redirect('/', request)


def sign_out(request):
    logout(request)
    return redirect('/', request)


def search(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        specialists = Specialist.objects.values('id', 'user__name', 'title')
    else:
        specialists = Specialist.objects.filter(user__name__contains=keyword).values('id', 'user__name', 'title')
    return JsonResponse({"success": True, "result": list(specialists)})


def specialist(request):
    specialist_id = request.GET.get('id')
    specialist = Specialist.objects.get(id=specialist_id)
    appointments = Appointment.objects.filter(specialist=specialist)
    result = {
        'id': specialist.id,
        'name': specialist.user.name,
        'title': specialist.title,
        'schedule': [{'date': appointment.date, 'status': appointment.status} for appointment in appointments]
    }
    return JsonResponse({"success": True, "result": result})


def patient(request):
    keyword = request.GET.get('keyword')
    if not keyword:
        patients = Patient.objects.values('id', 'user__name')
    else:
        patients = Patient.objects.filter(user__name__contains=keyword).values('id', 'user__name')
    return JsonResponse({"success": True, "result": list(patients)})

import json
from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
@login_required(login_url='/study_tracker/login/')
def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
    'list_of_assignments': assignment_data,
    'name': request.user.username,
    'last_login': request.COOKIES['last_login'],

}

    return render(request, "tracker.html", context)



@csrf_exempt
def create_assignment_ajax(request):  
    # create object of form
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = Assignment.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'name':data.name,
            'subject':data.subject,
            'date':data.date,
            'progress':data.progress,
            'description':data.description,
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_assignment.html", context)


def create_assignment(request):
    form = AssignmentForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "create_assignment.html", context)

def show_xml(request):
    data = Assignment.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Assignment.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Assignment.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('study_tracker:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("study_tracker:show_tracker")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong username or password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:login'))
    response.delete_cookie('last_login')
    return response

def modify_assignment(request, id):
    # Get data berdasarkan ID
    task = Assignment.objects.get(pk = id)

    # Set instance pada form dengan data dari task
    form = AssignmentForm(request.POST or None, instance=task)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "modify_assignment.html", context)

def delete_assignment(request, id):
    # Get data berdasarkan ID
    assignment = Assignment.objects.get(pk = id)
    # Hapus data
    assignment.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

@csrf_exempt
def create_assignment_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_assignment = Assignment.objects.create(
            name = data["name"],
            subject = data["subject"],
            progress = int(data["progress"]),
            description = data["description"]
        )

        new_assignment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)







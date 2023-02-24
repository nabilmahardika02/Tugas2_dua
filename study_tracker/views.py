from django.shortcuts import render
from study_tracker.models import Assignment

# Create your views here.
def show_tracker(request):
    transaction_data = Assignment.objects.all()
    context = {
    'list_of_transactions': transaction_data,
    'name': 'Nabil'
}

    return render(request, "assignment_list.html")

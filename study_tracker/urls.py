from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import create_assignment
from study_tracker.views import show_xml #sesuaikan dengan nama fungsi yang dibuat
from study_tracker.views import show_json #sesuaikan dengan nama fungsi yang dibuat
from study_tracker.views import show_xml_by_id, show_json_by_id




app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),



]

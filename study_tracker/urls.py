from django.urls import path
from study_tracker.views import show_tracker
from study_tracker.views import create_assignment
from study_tracker.views import show_xml 
from study_tracker.views import show_json 
from study_tracker.views import show_xml_by_id, show_json_by_id
from study_tracker.views import register 
from study_tracker.views import login_user 
from study_tracker.views import logout_user 
from study_tracker.views import modify_assignment
from study_tracker.views import delete_assignment
from study_tracker.views import create_assignment_ajax
from study_tracker.views import create_assignment_flutter




app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('modify/<int:id>', modify_assignment, name='modify_assignment'), #sesuaikan dengan nama fungsi yang dibuat
    path('delete/<int:id>', delete_assignment, name='delete_assignment'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-ajax/', create_assignment_ajax, name='create_assignment_ajax'),
    path('create-flutter/', create_assignment_flutter, name='create_assignment_flutter'),






]

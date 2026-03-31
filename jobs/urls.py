from django.urls import path
from .views import *

urlpatterns = [
    path('add/',create_job, name="add_job"),
    path('list/',list_job, name="list_job"),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('applicants/<int:job_id>/', view_applicants, name='view_applicants'),
    path('update-status/<int:app_id>/', update_status, name='update_status'),

    path('candidate-dashboard/', candidate_dashboard,name="candidate_dashboard"),
    path('recruiter-dashboard/', recruiter_dashboard,name="recruiter_dashboard"),

]
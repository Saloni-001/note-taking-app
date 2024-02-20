from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('notes/create/', views.note_create),
    path('notes/<int:id>/', views.note_detail),
    path('notes/<int:id>/update/', views.note_update),  # New URL pattern for updating note
    path('notes/version-history/<int:id>/', views.version_history),
    # Define other URL patterns for endpoints
]
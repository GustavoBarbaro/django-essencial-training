from django.urls import path


from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
    path('notes/new', views.NotesCreatedView.as_view(), name="notes.new"),

]









""" urlpatterns = [
    path('notes', views.list, name="notes.list"),
    path('notes/<int:pk>', views.detail, name="notes.detail"),

] """
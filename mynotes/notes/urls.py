from unicodedata import name
from django.urls import path
from .views import delete_note, index, add_note, get_note, edit_note

urlpatterns = [
    path('', index, name='home' ),
    path('add_note/', add_note, name='add_note'),
    path('note/<int:id>', get_note, name='note'),
    path('note/<int:id>/delete', delete_note, name='delete_note'),
    path('note/<int:id>/edit', edit_note, name='edit_note'),
    
]
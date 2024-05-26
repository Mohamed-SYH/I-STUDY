from django.db import IntegrityError
from django.urls import reverse
from django.test import Client
#from django.contrib.auth.models import User  # Importez la classe User ici
import pytest

from profiles.models import User

@pytest.mark.django_db
def test_create_classroom_view():
    client = Client()
    # Créer un utilisateur 
    user = User.objects.create_user(email='Teacher1@gmail.com', password='Teacher@2002')
    # Login en tant qu'un utilisateur 
    client.login(email='Teache1r@gmail.com', password='Teacher@2002')
    # Creer la class My class
    response = client.post(reverse('create_class'), {'classroom_name': 'MyClass'})
   
    assert response.status_code == 302 


def test_create_classroom_invalid_username():
    with pytest.raises(ValueError):
        # Attempt to create a classroom with an invalid username
        User.objects.create_user(username='', email='', password='')

@pytest.mark.django_db
def test_create_classroom_duplicate_username():
    # Create a user with a username that already exists
    User.objects.create(username='teacher')
    with pytest.raises(IntegrityError):
        # Attempt to create another user with the same username
        User.objects.create(username='teacher')        


def test_create_classroom_view_unauthorized_access():
    client = Client()
    # Attempt to create a classroom without logging in
    response = client.post(reverse('create_class'), {'classroom_name': 'MyClass'})
    assert response.status_code == 302  # Redirect to login page

@pytest.mark.django_db
def test_create_classroom_view_authenticated_access():
    client = Client()
    # Create a user and log in
    user = User.objects.create_user(email='teacher2@example.com', password='Teacher@2002')
    client.login(email='teacher11@example.com', password='Teacher@2002')
    # Attempt to create a classroom
    response = client.post(reverse('create_class'), {'classroom_name': 'MyClass'})
    assert response.status_code == 302  # Redirect to dashboard or success page    
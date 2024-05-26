import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from profiles.models import Teacher, Student

User = get_user_model()

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def create_teacher(db):
    def make_teacher(user, **kwargs):
        return Teacher.objects.create(user=user, **kwargs)
    return make_teacher

@pytest.fixture
def create_student(db):
    def make_student(user, **kwargs):
        return Student.objects.create(user=user, **kwargs)
    return make_student

def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

def test_teacher_dashboard_view(client, create_user, create_teacher):
    user = create_user(email='teacher@example.com', password='password')
    create_teacher(user, name='John Doe')
    client.force_login(user)
    url = reverse('teacher')
    response = client.get(url)
    assert response.status_code == 200

def test_student_dashboard_view(client, create_user, create_student):
    user = create_user(email='student@example.com', password='password')
    create_student(user, name='Jane Doe')
    client.force_login(user)
    url = reverse('student')
    response = client.get(url)
    assert response.status_code == 200

def test_signup_teacher_view(client):
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200

def test_signup_student_view(client):
    url = reverse('student_register')
    response = client.get(url)
    assert response.status_code == 200

def test_login_view(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

def test_logout_view(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302  # Redirects to login page after logout

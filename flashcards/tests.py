import pytest
from django.urls import reverse
from django.test import Client
from .models import Flashcard

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def create_flashcard():
    return Flashcard.objects.create(
        question='What is the capital of France?',
        option1='London',
        option2='Paris',
        option3='Berlin',
        option4='Rome',
        correct_answer='Paris'
    )

@pytest.mark.django_db
def test_flashcard_list_view(client):
    url = reverse('flashcard_list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_flashcard_detail_view(client, create_flashcard):
    flashcard = create_flashcard
    url = reverse('flashcard_detail', args=[flashcard.pk])
    response = client.get(url)
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_add_flashcard_view(client):
    url = reverse('flashcard_list')
    response = client.get(url)
    assert response.status_code == 200

    # Test POST request to add a new flashcard
    data = {
        'question': 'What is the capital of Spain?',
        'option1': 'Paris',
        'option2': 'Madrid',
        'option3': 'London',
        'option4': 'Rome',
        'correct_answer': 'Madrid'
    }
    response = client.post(url, data)
    assert response.status_code == 200  # Should stay on the same page after successful POST


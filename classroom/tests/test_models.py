import pytest
from profiles.models import User
from classroom.models import Teacher

@pytest.mark.django_db
def test_create_classroom():
    # Créer un utilisateur
    user = User.objects.create(username='teacher')
    # Créer un enseignant avec cet utilisateur
    teacher = Teacher.objects.create(user=user)
    # Vérifier si l'utilisateur associé est correct
    assert teacher.user.username == 'teacher'

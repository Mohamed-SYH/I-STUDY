# flashcards/forms.py
from django import forms
from .models import Flashcard

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

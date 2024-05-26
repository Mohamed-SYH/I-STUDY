# flashcards/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from .forms import FlashcardForm

def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    is_teacher = request.user.is_authenticated and request.user.is_teacher
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards, 'is_teacher': is_teacher})

def flashcard_detail(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, pk=flashcard_id)
    selected_answer = None
    feedback = None

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        if selected_answer == flashcard.correct_answer:
            feedback = "Correct! Well done."
        else:
            feedback = "Incorrect."
            # Provide the correct answer to the student if their response is incorrect

    return render(request, 'flashcards/flashcard_detail.html', {'flashcard': flashcard, 'selected_answer': selected_answer, 'feedback': feedback})
def add_flashcard(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_list')
    else:
        form = FlashcardForm()
    return render(request, 'flashcards/add_flashcard.html', {'form': form})

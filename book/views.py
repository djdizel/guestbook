from django.shortcuts import render, redirect
from .models import GuestbookEntry
from .forms import GuestbookForm

def guestbook_view(request):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')  # Перенаправление на ту же страницу после отправки формы
    else:
        form = GuestbookForm()

    entries = GuestbookEntry.objects.order_by('-created_at')  # Последние сообщения сверху
    return render(request, 'book/guestbook.html', {'form': form, 'entries': entries})

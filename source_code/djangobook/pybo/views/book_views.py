# pybo/views/book_views.py
from django.shortcuts import render, get_object_or_404
from ..models import Book, BorrowHistory
from pybo.services.book_service import get_borrow_history_for_book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'pybo/book_list.html', {'books': books})

def book_history(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        histories = get_borrow_history_for_book(book)
    except Exception as e:
        return render(request, 'pybo/no_history.html', {'book': book, 'error': str(e)})
    return render(request, 'pybo/book_history.html', {'book': book, 'histories': histories})
from pybo.models import Book, BorrowHistory
from pybo.services.exceptions import BookNotFound, BookHasNoBorrowHistory

def get_book_by_id(book_id):
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise BookNotFound(f"도서(id={book_id})가 존재하지 않습니다.")

def get_borrow_history_for_book(book):
    histories = BorrowHistory.objects.filter(book=book).order_by('-borrowed_at')
    if not histories.exists():
        raise BookHasNoBorrowHistory("도서에는 대출 기록이 없습니다.")
    return histories
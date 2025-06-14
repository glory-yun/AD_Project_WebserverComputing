from django.contrib.auth import get_user_model
User = get_user_model()
import pytest
from pybo.models import Book, BorrowHistory
from pybo.services.book_service import get_book_by_id, get_borrow_history_for_book
from pybo.services.exceptions import BookNotFound, BookHasNoBorrowHistory

@pytest.mark.django_db
def test_get_book_by_id_success():
    # Given
    book = Book.objects.create(title='Test Book', author='Author Name')

    # When
    found_book = get_book_by_id(book.id)

    # Then
    assert found_book == book

@pytest.mark.django_db
def test_get_book_by_id_not_found():
    # When & Then
    with pytest.raises(BookNotFound) as exc_info:
        get_book_by_id(9999)
    assert "도서(id=9999)가 존재하지 않습니다." in str(exc_info.value)

@pytest.mark.django_db
def test_get_borrow_history_success():
    # Given
    user = User.objects.create_user(username='tester', password='pass1234')
    book = Book.objects.create(title='Test Book', author='Author Name')
    BorrowHistory.objects.create(book=book, user=user, borrowed_at='2024-01-01T00:00:00Z')

    # When
    histories = get_borrow_history_for_book(book)

    # Then
    assert len(histories) == 1
    assert histories[0].user == user

@pytest.mark.django_db
def test_get_borrow_history_not_found():
    # Given
    book = Book.objects.create(title='Empty Book', author='Tester')

    # When & Then
    with pytest.raises(BookHasNoBorrowHistory) as exc_info:
        get_borrow_history_for_book(book)
    assert "도서에는 대출 기록이 없습니다." in str(exc_info.value)
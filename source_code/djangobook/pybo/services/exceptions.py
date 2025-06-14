class BookNotFound(Exception):
    """도서가 존재하지 않을 때 발생하는 예외"""
    pass

class BookHasNoBorrowHistory(Exception):
    """도서에 대출 기록이 없을 때 발생하는 예외"""
    pass
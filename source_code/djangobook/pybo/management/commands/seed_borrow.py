from django.core.management.base import BaseCommand
from pybo.models import Book, BorrowHistory
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import timedelta, timezone  # ✅ 수정됨

class Command(BaseCommand):
    help = '랜덤 대출 이력을 생성합니다.'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=50, help='생성할 대출 기록 수')

    def handle(self, *args, **options):
        fake = Faker()
        books = list(Book.objects.all())
        users = list(User.objects.all())
        total = options['total']

        if not books or not users:
            self.stdout.write(self.style.ERROR("책과 사용자 데이터가 필요합니다."))
            return

        for _ in range(total):
            book = random.choice(books)
            user = random.choice(users)
            borrowed_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.utc)

            BorrowHistory.objects.create(
                book=book,
                borrower=user.username,  # ✅ 문자열 필드에 저장
                borrowed_at=borrowed_at
            )

        self.stdout.write(self.style.SUCCESS(f"✅ 대출 기록 {total}개 생성 완료!"))
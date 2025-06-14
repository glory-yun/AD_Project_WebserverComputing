# pybo/management/commands/seed_books.py

from django.core.management.base import BaseCommand
from pybo.models import Book
from faker import Faker

class Command(BaseCommand):
    help = '랜덤 책 데이터를 생성합니다.'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(30):
            Book.objects.create(
                title=f"{fake.word().title()} Programming {i+1}",
                author=fake.name()
            )
        self.stdout.write(self.style.SUCCESS("✅ 30개의 책 생성 완료!"))
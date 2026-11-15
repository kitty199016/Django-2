from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Очищает БД и загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Загрузка категорий из фикстуры...')
        call_command('loaddata', 'fixtures/categories.json')

        self.stdout.write('Загрузка продуктов из фикстуры...')
        call_command('loaddata', 'fixtures/products.json')

        self.stdout.write(self.style.SUCCESS('База данных успешно наполнена тестовыми данными!'))

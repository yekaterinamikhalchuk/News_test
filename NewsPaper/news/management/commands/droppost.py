from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Delete all news of the certain category'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если true — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category_get', type=str)

    def handle(self, *args, **options):
        answer = input(f'Do you really want to delete all products of {options["category_get"]}? yes/no')

        if answer == 'yes':
            try:
                category = Category.objects.get(category_name=options["category_get"])
                print(category)
                Post.objects.filter(categories=category).delete()
                self.stdout.write(self.style.SUCCESS(f'Posts of {category} category are deleted successfully!'))
            except Post.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Could not find category {category}'))

        else:
            self.stdout.write(
                self.style.ERROR('Cancelled'))
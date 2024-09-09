from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Prints a greeting"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="User name")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        greeting = f"Hi, {name}. Good morning!"
        # self.stdout.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))

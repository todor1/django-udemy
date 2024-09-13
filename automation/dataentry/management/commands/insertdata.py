from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = "Inserts data into the database"

    def handle(self, *args, **options):
        # add single record
        # Student.objects.create(roll_no=1001, name="Alice", age=20)
        # add multiple records
        dataset = [
            {"roll_no": 1002, "name": "Bob", "age": 21},
            {"roll_no": 1003, "name": "Charlie", "age": 22},
            {"roll_no": 1004, "name": "David", "age": 23},
            {"roll_no": 1005, "name": "Gosho", "age": 21},
            {"roll_no": 1006, "name": "Pesho", "age": 20},
        ]
        # add validation against the roll_no
        for data in dataset:
            roll_no = data["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if existing_record:
                self.stdout.write(
                    self.style.WARNING(
                        f"Record with roll number {roll_no} already exists"
                    )
                )
                continue
            else:
                Student.objects.create(**data)
        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))

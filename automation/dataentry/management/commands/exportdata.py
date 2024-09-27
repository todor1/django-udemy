import csv
from django.core.management.base import BaseCommand, CommandError

# from dataentry.models import Student
from django.apps import apps
from datetime import datetime

# proposed command: python manage.py exportdata file_path model_name
# python manage.py exportdata "full_path_to_file\student_data.csv" Student
# python manage.py exportdata "full_path_to_file\student_data.csv" test
# python manage.py exportdata "full_path_to_file\customer_demo_records.csv" customer
# The csv column headers should match the model fields


class Command(BaseCommand):
    help = "Exports data from a database table (e.g. Student model) to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="The name of the model")

    def handle(self, *args, **kwargs):
        model_name = kwargs["model_name"].capitalize()
        # search for the model in the installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass
        # if model not found, raise an error
        if not model:
            self.stderr.write(f"Model {model_name} not found")
            return

        # fetch data from the database
        data = model.objects.all()
        if not data:
            self.stdout.write(self.style.ERROR("No data found in the table"))
            return

        # define the file path
        # file_path = kwargs["file_path"]
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        file_path = f"exported_{model_name.lower()}_data_{timestamp}.csv"

        # write data to the CSV file (blank is default newline for all OS)
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([field.name for field in model._meta.fields])
            for row in data:
                writer.writerow(
                    [getattr(row, field.name) for field in model._meta.fields]
                )
        self.stdout.write(self.style.SUCCESS(f"Data exported to {file_path}"))
        return

from django.core.management.base import BaseCommand, CommandError

# from dataentry.models import Student
from django.apps import apps
import csv


# Proposed command: python manage.py importdata file_path
# python manage.py importdata  "full_path_to_file\student_data.csv"

# Proposed command: python manage.py importdata file_path model_name
# python manage.py importdata  "full_path_to_file\student_data.csv" Student
# python manage.py importdata  "full_path_to_file\student_data.csv" test
# python manage.py importdata  "full_path_to_file\customer_demo_records.csv" customer
# The csv column headers should match the model fields


class Command(BaseCommand):
    help = "Imports data from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="CSV file path")
        parser.add_argument("model_name", type=str, help="Name of the model/data class")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"].capitalize()

        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(
                    app_label=app_config.label,
                    model_name=model_name,
                )
                break  # Stop searching  if the model is found
            except LookupError:
                continue  # Continue searching in other apps
                # model = None
        if not model:
            # self.stdout.write(self.style.ERROR("Model not found"))
            raise CommandError(f"Model {model_name} not found in any app.")

        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    model.objects.create(**row)
            self.stdout.write(self.style.SUCCESS("Data imported successfully"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("File not found"))
            return

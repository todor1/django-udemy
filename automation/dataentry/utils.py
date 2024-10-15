from django.apps import apps
from django.core.management.base import CommandError
import csv
from django.db import DataError


def get_all_custom_models():
    default_models = [
        "ContentType",
        "Session",
        "LogEntry",
        "Group",
        "Permission",
        "User",  ## Uncomment this line if you don't want to include the User in the list for upload
        "Upload",  ## Adding also custom models here to not be included in the list for upload
    ]
    # try to get all the apps in the project
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            # print(model._meta.app_label, "->", model.__name__)
            custom_models.append(model.__name__)
    return custom_models


def check_csv_errors(file_path: str, model_name: str):
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
    if not model:
        raise CommandError(f"Model {model_name} not found in any app.")

    # Get all the fields in the selected/found model
    model_fields = [field.name for field in model._meta.fields if field.name != "id"]

    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            csv_headers = reader.fieldnames
            # compare the csv headers with the model fields
            if csv_headers != model_fields:
                raise DataError(
                    f"CSV headers do not match the {model_name} table fields.\nPlease check and try again."
                )
    except Exception as e:
        raise e
    return model

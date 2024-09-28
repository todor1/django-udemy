from django.apps import apps


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
            print(model._meta.app_label, "->", model.__name__)
            custom_models.append(model.__name__)
    return custom_models

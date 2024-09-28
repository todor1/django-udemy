from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
import pathlib
from django.core.management import call_command


# Create your views here.
def import_data(request):
    if request.method == "POST":
        # Do something with the data
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")
        # store the file in the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        # constuct the full path to the file
        base_url = pathlib.Path(settings.BASE_DIR)
        relative_path = pathlib.Path(upload.file.url.lstrip("/"))
        full_path = base_url / relative_path
        print(f"{full_path=}")
        # resolved_path = full_path.resolve()
        # print(f"{resolved_path=}")

        # trigger the import_data command
        try:
            call_command("importdata", full_path, model_name)
        except Exception as e:
            # print(f"Error: {e}")
            raise e

        return redirect("import_data")
    else:
        custom_models = get_all_custom_models()
        context = {"all_models": custom_models}
        return render(request, "dataentry/importdata.html", context)

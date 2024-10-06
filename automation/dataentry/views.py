from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload
from django.conf import settings
import pathlib
from django.core.management import call_command
from django.contrib import messages
from .tasks import import_data_task


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
        full_path = str(base_url / relative_path)
        print(f"{full_path=}")
        # resolved_path = full_path.resolve()
        # print(f"{resolved_path=}")

        # # trigger the import_data command
        # try:
        #     call_command("importdata", full_path, model_name)
        #     messages.success(request, "Data imported successfully")
        # except Exception as e:
        #     # print(f"Error: {e}")
        #     # raise e
        #     messages.error(request, f"Error: {e}")
        #     # messages.error(request, str(e))

        # execute the import_data_task asynchronously
        import_data_task.delay(full_path, model_name)
        # show the message to the user
        messages.success(
            request,
            "Your data is being imported. You will be notified once it is done.",
        )

        return redirect("import_data")
    else:
        custom_models = get_all_custom_models()
        context = {"all_models": custom_models}
        return render(request, "dataentry/importdata.html", context)

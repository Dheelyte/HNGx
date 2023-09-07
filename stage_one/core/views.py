from datetime import datetime
from django.http import JsonResponse


# Create your views here.

def index(request):
    slack_name = request.GET.get('slack_name')
    now = datetime.now()
    current_day = now.strftime("%A")
    utc_time = now.isoformat().split('.')[0] + 'Z'
    track = request.GET.get('track')
    github_file_url = "https://github.com/Dheelyte/HNGx/blob/main/core/views.py"
    github_repo_url = "https://github.com/Dheelyte/HNGx"

    return JsonResponse({
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    })
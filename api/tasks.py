import requests
from django.conf import settings


# Triggers a deploy hook in front app
def task_deploy_front():
    return requests.post(settings.FRONT_APP_DEPLOY_URL)

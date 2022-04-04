# koulutettuninja-api

#### Setup:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py loaddata api/fixtures/data.json
python manage.py createsuperuser
python manage.py runserver
```

#### Always-on task

Create file `qcluster.sh` with content:

```
export $(cat /path/to/your/env/file/.env | xargs)
source /path/to/virtualenv/bin/activate
python /path/to/django/app/manage.py qcluster
```

Run script in hosting service as continous background task using command: `source /path/to/qcluster.sh`
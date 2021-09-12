# koulutettuninja-api

Setup instructions:

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

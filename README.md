1. Download project
2. Create and init virtual env
3. install and configure PostgreSQL https://www.postgresql.org/download/
4. install Redis 2.8.19
5. run redis with command "redis-server -maxheap 512mb"
6. enter your data from the email with which you want to notify users (in settings.py)
7. pip install -r requirements.txt
8. (in another command line) "celery -A quick_publisher worker —pool=solo -l info"
9. python manage.py migrate
10. python manage.py loaddata fixtures.json
11. python manage.py runserver

from django.core.mail import send_mail
from library.celery import app


@app.task
def send_verification_email(email):
	send_mail(
            'Регистрация на сайте библиотеки.',
            'Вы успешно прошли регистрацию.',
            'rusty.custom.oldtimers@gmail.com',
            [email],
            False
            )

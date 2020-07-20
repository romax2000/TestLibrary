from app.tasks import send_verification_email
from datetime import datetime
 

def post_save_user(sender, instance, *args, **kwargs):
    send_verification_email.delay(instance.email)

def pre_save_edit_book_date(sender, instance, *args, **kwargs):
    instance.edit_date = datetime.today()
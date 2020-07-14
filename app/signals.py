from app.tasks import send_verification_email
 

def post_save_user(sender, instance, *args, **kwargs):
    send_verification_email.delay(instance.email)

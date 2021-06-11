from django.core.management.base import BaseCommand, CommandError
from django.core.mail import get_connection, send_mail
from core.models import Email


# reference - https://docs.djangoproject.com/en/3.2/topics/email/
class Command(BaseCommand):
    help = "Send emails to everyone in our database"

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            emails = Email.objects.all()
            for email in emails:
                print(email.email)
                with get_connection():
                    send_mail(
                        'Hello There!',
                        'Thank you for subscribing.',
                        'toy@datarockie.com',
                        [email.email],
                        fail_silently=False,
                    )
        except CommandError:
            raise CommandError("Error!")

from django.core.mail import EmailMessage,send_mail

def register_email(email,name):
   subject = 'Tech_Blog'
   body = f'Hello {name} \n' \
         'welcome to Tech_Blog \n' \
         'Please feel free to contact us \n'\
         'Thank&Regards \n'\
         'techblog.application@gmail.com'

   email = EmailMessage(subject, body, to=[email])
   email.send()
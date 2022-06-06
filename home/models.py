from django.db import models
from twilio.rest import Client


##########  pip3 install twilio



account_sid = 'account_id_kirtladi'
auth_token = 'Token kirtladi '
client = Client(account_sid, auth_token)




class Message(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        message = client.messages.create(
            body=f"HI, {self.name} ",
            from_='Briktrlgan_nomer_kirtladi', ###### kimdan
            to=f'{self.phone}' ######### qaysi no'merga
        )
        print(message.sid)
        return super().save(*args, **kwargs)
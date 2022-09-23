from django.db import models

# Create your models here.
class Bankinfo(models.Model):
    bank_id = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=12)
    social_number = models.CharField(max_length=50)
    passport_no = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    nominee_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'Bankinfo: {self.first_name}{self.last_name}'
    



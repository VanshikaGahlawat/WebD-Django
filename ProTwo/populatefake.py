import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from faker import Faker
from AppTwo.models import User

fakegen=Faker()

def add_userDetails(n=10):
    for value in range(n):
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_email=fakegen.email()

        person=User.objects.get_or_create(first_name=fake_fname,last_name=fake_lname, email=fake_email)

if __name__ == '__main__':

    print('populating database')
    add_userDetails()
    print("database populated succesfully")

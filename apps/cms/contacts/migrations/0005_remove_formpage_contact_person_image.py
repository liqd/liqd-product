# Generated by Django 2.2.4 on 2019-08-22 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_contacts', '0004_formpage_custom_contact_person_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='contact_person_image',
        ),
    ]
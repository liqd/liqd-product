from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from adhocracy4 import transforms
from adhocracy4.images import fields as images_fields


class Partner(models.Model):
    slug = AutoSlugField(populate_from='name', unique=True)
    name = models.CharField(max_length=100)
    title = models.CharField(
        verbose_name=_('Title of your platform'),
        max_length=100,
        default='Beteiligungsplattform',
        help_text=_('The title of your platform will be shown '
                    'on the landing page. It should be clear to '
                    'the users that this is your participation '
                    'platform. max. 100 characters')
    )
    description = models.CharField(
        max_length=400,
        verbose_name=_('Short description of your organisation'),
        help_text=_('The description will be displayed on the '
                    'landing page. max. 400 characters')
    )
    logo = images_fields.ConfiguredImageField(
        'logo',
        verbose_name=_('Logo'),
        help_text=_('The Logo representing your organisation.'
                    ' The image must be square and it '
                    'should be min. 200 pixels wide and 200 '
                    'pixels tall. Allowed file formats are '
                    'png, jpeg, gif. The file size '
                    'should be max. 5 MB.'),
        upload_to='partners/logos',
        blank=True
    )
    slogan = models.CharField(
        max_length=200,
        verbose_name=_('Slogan'),
        blank=True,
        help_text=_('The slogan will be shown below '
                    'the title of your platform on '
                    'the landing page. The slogan can '
                    'provide context or additional '
                    'information to the title. '
                    'max. 200 characters')
    )
    image = images_fields.ConfiguredImageField(
        'heroimage',
        verbose_name=_('Header image'),
        help_prefix=_(
            'The image will be shown as a decorative background image.'
        ),
        upload_to='partners/backgrounds',
        blank=True
    )
    information = RichTextUploadingField(
        config_name='image-editor',
        verbose_name=_('Information about your organisation'),
        help_text=_('You can provide general information about your '
                    'participation platform to your visitors. '
                    'It’s also helpful to name a general person '
                    'of contact for inquiries. The information '
                    'will be shown on a separate page that '
                    'can be reached via the main menu.'),
        blank=True
    )
    imprint = RichTextField(
        verbose_name=_('Imprint'),
        help_text=_('Please provide all the legally '
                    'required information of your imprint. '
                    'The imprint will be shown on a separate page.')
    )
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )

    def has_admin(self, user):
        return self.admins.filter(id=user.id).exists()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.information = transforms.clean_html_field(
            self.information, 'image-editor')
        self.imprint = transforms.clean_html_field(self.imprint)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '/{}'.format(self.name).lower()

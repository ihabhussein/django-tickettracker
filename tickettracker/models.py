from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


STATES = [
    # ('', _('')),
]

SEVERITY_LEVELS = [
    ('Trivial', _('Trivial')),
    ('Minor', _('Minor')),
    ('Major', _('Major')),
    ('Critical', _('Critical')),
    ('Blocker', _('Blocker')),
]


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Milestone(models.Model):
    label = models.CharField(_('Label'), max_length=50)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('Milestone')
        verbose_name_plural = _('Milestones')


class Tag(models.Model):
    label = models.CharField(_('Label'), max_length=50)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Ticket(models.Model):
    subject = models.CharField(
        _('Subject'), max_length=100,
    )
    product = models.ForeignKey(
        Product, models.CASCADE, verbose_name=_('Product'),
    )
    severity = models.CharField(
        _('Severity'), max_length=16, choices=SEVERITY_LEVELS,
        null=True, blank=True,
    )
    milestone = models.ForeignKey(
        Milestone, models.SET_NULL, verbose_name=_('Milestone'),
        null=True, blank=True,
    )
    tags = models.ManyToManyField(
        Tag, verbose_name=_('Tags'),
        null=True, blank=True,
    )

    def __str__(self):
        return '#{0}: {1}'.format(self.id, self.subject)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')


class TicketLogEntry(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.PROTECT, verbose_name=_('Created by'),
    )
    created_at = models.DateTimeField(
        _('Created at'), auto_now_add=True,
    )
    body = models.CharField(
        _('Body'), max_length=500,
    )


class Attachement(models.Model):
    ticket = models.ForeignKey(
        TicketLogEntry, models.CASCADE,
    )
    # TODO

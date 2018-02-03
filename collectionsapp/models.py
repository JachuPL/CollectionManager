import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Collection(models.Model):
    user = models.ForeignKey(User, default=1, verbose_name='Właściciel', on_delete=models.CASCADE)
    name = models.CharField('Nazwa', max_length=200)
    created = models.DateField('Data utworzenia', default=timezone.now)
    desc = models.CharField('Opis', max_length=1000)

    def __str__(self):
        return "%s: %s" % (self.name, self.desc)

    def is_recently_created(self):
        # collection is considered recently created when its no older than 2 weeks
        return self.created >= timezone.now().date() - datetime.timedelta(weeks=2)


class CollectionValue(models.Model):
    name = models.CharField('Nazwa', max_length=200)
    aggregate = models.CharField('Agregat (np. autor, zespół)', max_length=200)
    added = models.DateField('Data dodania', default=timezone.now)
    date = models.DateField('Data produkcji przedmiotu, np. data wydania książki, rocznik wina itd.')
    desc = models.CharField('Opis przedmiotu', max_length=2000)
    collection_id = models.ForeignKey(Collection, on_delete=models.DO_NOTHING, verbose_name='Kolekcja')

    def __str__(self):
        return "%s \"%s\" (%s)" % (self.aggregate, self.name, self.date)

    def is_new_item(self):
        # item is considered new when it was added no longer than 30 days ago
        return self.date >= timezone.now().date() - datetime.timedelta(days=30)


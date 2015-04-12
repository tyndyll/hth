from django.db import models

ENTRYCHOICE = (
                    ('T', 'Tile'),
                    ('D', 'Detail'),
              )

class EntrySet(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class Entry(models.Model):
    title = models.CharField(max_length=15)
    fa_class = models.CharField(max_length=30)
    background_image = models.CharField(max_length=255)
    abstract = models.CharField(max_length=100)
    description = models.TextField()
    entry_set = models.ForeignKey('EntrySet')
    entry_type = models.CharField(max_length=1, choices=ENTRYCHOICE)

    def __unicode__(self):
        return unicode("[{}] {}".format(self.entry_set.name, self.title))


class EntrySetRelationship(models.Model):
    parent = models.OneToOneField('EntrySet', primary_key=True)
    sub_set = models.ForeignKey('EntrySet', related_name='+')


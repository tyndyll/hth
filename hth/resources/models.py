from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    abstract = models.CharField(max_length=100)
    fa_class = models.CharField(max_length=20)
    background_image = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

class CategoryAbstractLanguage(models.Model):
    category = models.ForeignKey('Category')
    language = models.CharField(max_length=2)
    abstract = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode("{} [{}]".format(self.category.name, self.language))

    class Meta:
        unique_together = ('category', 'language')


class Entry(models.Model):
    title = models.CharField(max_length=15)
    abstract = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey('Category')
    address = models.TextField()
    opening = models.TextField()

    def __unicode__(self):
        return unicode("[{}] {}".format(self.category.name, self.title))

class EntryAbstractLanguage(models.Model):
    entry = models.ForeignKey('Entry')
    language = models.CharField(max_length=2)
    abstract = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode("{} [{}]".format(self.entry.title, self.language))

    class Meta:
        unique_together = ('entry', 'language')

class EntryDescriptionLanguage(models.Model):
    entry = models.ForeignKey('Entry')
    language = models.CharField(max_length=2)
    description = models.TextField()

    def __unicode__(self):
        return unicode("{} [{}]".format(self.entry.title, self.language))

    class Meta:
        unique_together = ('entry', 'language')


class EntryPhone(models.Model):
    entry = models.ForeignKey('Entry')
    number = models.CharField(max_length=12)
    available = models.BooleanField()

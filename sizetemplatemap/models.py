from django.db import models

# Create your models here.

class CreativeSize(models.Model):
    creativeSizeId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    height = models.IntegerField()
    width = models.IntegerField()
    status = models.CharField(max_length=1)
    insertDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    bufferName = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'CreativeSize'

    def __unicode__(self):
        return self.name

class CreativeTemplate(models.Model):
    creativeTemplateId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    template = models.TextField()
    status = models.CharField(max_length=1)
    sizes = models.ManyToManyField(CreativeSize, through='CreativeSizeTemplateRel', related_name='templates')

    class Meta:
        db_table = 'CreativeTemplate'

    def __unicode__(self):
        return (self.name)

class CreativeSizeTemplateRel(models.Model):
    creativeSizeId = models.ForeignKey(CreativeSize, db_column='creativeSizeId')
    creativeTemplateId = models.ForeignKey(CreativeTemplate, db_column='creativeTemplateId')

    class Meta:
        db_table = 'CreativeSizeTemplateRel'

    def __unicode__(self):
        return u'%s + %s' % (self.creativeSizeId, self.creativeTemplateId)
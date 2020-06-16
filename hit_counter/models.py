from django.db import models

# Create your models here.
class PageHitCounter(models.Model):
    counter=models.IntegerField()
    @classmethod
    def update_count(cls):
        _t=None
        if PageHitCounter.objects.count() == 0:
            _t=PageHitCounter()
            _t.counter=0
        else:
            _t=PageHitCounter.objects.first()
        field_obj=PageHitCounter._meta.get_field("counter")
        field_value=getattr(_t,field_obj.attname)
        setattr(_t,field_obj.attname,field_value+1)
        _t.save()
        return field_value+1

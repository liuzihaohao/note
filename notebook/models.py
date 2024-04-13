from django.db import models

# Create your models here.

class NoteCon(models.Model):
    id=models.CharField(primary_key=True,verbose_name='ID',max_length=8192)
    content=models.TextField(verbose_name="Content",null=True, blank=True)
    class Meta:
        verbose_name='内容列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.id)
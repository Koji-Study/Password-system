from django.db import models

# Create your models here.


class password(models.Model):                                             #类表示数据表
    key = models.CharField('密码键', max_length=50, default='') 
    value = models.CharField('密码值', max_length=50, default='123456789')
    desc = models.CharField('描述', max_length=50, default='')
    
    def __str__(self):        #设置返回book的name字段，方便在admin中查看
        return self.key # self.value, self.desc

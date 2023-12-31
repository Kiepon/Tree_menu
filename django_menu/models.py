from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'Menus'

    
    def __str__(self):
        return f'{self.name}'
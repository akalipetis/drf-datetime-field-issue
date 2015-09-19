from django.db import models

class MainModel(models.Model):
    """
    Simple model, leading to the crash
    """
    pass


class SimpleModel(models.Model):
    """
    Simple model, leading to the crash
    """
    some_date = models.DateTimeField(blank=False)
    main_model = models.ForeignKey('MainModel', blank=False)
    

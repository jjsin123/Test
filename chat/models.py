from django.db import models

class Room(models.Model):
    class Meta:
        db_table = "room"
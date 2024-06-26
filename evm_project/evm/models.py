from django.db import models

# Create your models here.
class VoteCount(models.Model):
    party_a_votes = models.IntegerField(default=0)
    party_b_votes = models.IntegerField(default=0)
    party_c_votes = models.IntegerField(default=0)
    party_d_votes = models.IntegerField(default=0)
    count_a = models.IntegerField(default=0)
    count_b = models.IntegerField(default=0)
    count_c = models.IntegerField(default=0)
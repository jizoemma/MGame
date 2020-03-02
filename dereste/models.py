from django.db import models
from loginapp.models import *

# Create your models here.
class Songs(models.Model):
  SONG_TYPE = (
    ('Cute', 'Cute'),
    ('Cool', 'Cool'),
    ('Passion', 'Passion'),
    ('All', 'All'),
  )
  DIFFICULTY = (
    ('DEBUT', 'DEBUT'),
    ('REGULAR', 'REGULAR'),
    ('PRO', 'PRO'),
    ('MASTER', 'MASTER'),
    ('MASTER_PLUS', 'MASTER_PLUS'),
    ('Legend_MASTER_PLUS', 'Legend_MASTER_PLUS'),
    ('FORTE', 'FORTE'),
    ('PIANO', 'PIANO'),
    ('LIGHT', 'LIGHT'),
    ('TRICK', 'TRICK')
  )

  name = models.CharField(max_length=50, default='新曲名を追加してください')
  level = models.IntegerField(default=1)
  type = models.CharField(max_length=50, choices=SONG_TYPE)
  notes = models.IntegerField(default=100)
  grade = models.CharField(max_length=50, choices=DIFFICULTY)

  #class Meta:
  #    verbose_name = _("")
  #    verbose_name_pl
  #  #ural = _("s")
  def __str__(self):
      return '%s [%s(%d)]' % (self.name, self.grade, self.level)

  def get_absolute_url(self):
      return reverse(
    "dereste_detail", kwargs={"pk": self.pk})

class Challenges(models.Model):
  COMBO_EVAL =(
    ("x","x"),
    ("C","C"),
    ("B","B"),
    ("A","A"),
    ("S","S"),
  )
  cdate = models.DateField(auto_now_add=True)
  #usr_email = models.ForeignKey(User, on_delete=models.CASCADE)
  song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)
  score = models.IntegerField(default=0)
  perfect = models.IntegerField(default=0)
  great = models.IntegerField(default=0)
  nice = models.IntegerField(default=0)
  bad = models.IntegerField(default=0)
  miss = models.IntegerField(default=0)
  result = models.CharField(max_length=4, choices=COMBO_EVAL, default='x')
  combo = models.IntegerField(default=0)
  #rate = models.BigdecimalField(default=0)

  def __str__(self):
    return super().__str__()

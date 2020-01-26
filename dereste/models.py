from django.db import models

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
      return self.name

  def get_absolute_url(self):
      return reverse(
    "dereste_detail", kwargs={"pk": self.pk})

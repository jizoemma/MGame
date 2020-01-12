from django.db import models

# Create your models here.
class Songs(models.Model):
  SONG_TYPE = (
    ('Cu', 'Cute'),
    ('Co', 'Cool'),
    ('Pa', 'Passion'),
    ('Al', 'All'),
  )
  DIFFICULTY = (
    ('De', 'DEBUT'),
    ('Re', 'REGULAR'),
    ('Pr', 'PRO'),
    ('Ma', 'MASTER'),
    ('MP', 'MASTER_PLUS'),
    ('LMP', 'Legend_MASTER_PLUS'),
    ('Fo', 'FORTE'),
    ('Pi', 'PIANO'),
    ('Li', 'LIGHT'),
    ('Ti', 'TRICK')
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
    "_detail", kwargs={"pk": self.pk})

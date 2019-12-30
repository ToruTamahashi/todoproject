from django.db import models

# Create your models here.
#左の文字列はDBに保存される値,右は画面(ユーザ)に表示される値
PRIORITY = (('danger','high'),('info','nomal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        #choicesでDBに保存する値に選択肢を作ることができる
        choices = PRIORITY
    )
    #DateField,日付を保存する
    dudate = models.DateField()
    def __str__(self):
        return self.title
from django.db import models
from django.utils.translation import gettext_lazy as _


# things like question_text and pub_date represent the columns in the DB (the field's name)
class StrengthTrainingQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")


class StrenghtTrainingAnswer(models.Model):
    FULLBODY = "FB"
    PUSH = "PS"
    PULL = "PL"
    LEGS = "LG"
    SHOULDERS = "SH"
    CHEST = "CH"
    BACK = "BK"
    ARMS = "AR"
    NONE = "NO"
  
    STRENGHT_TRAINING_OPTIONS = [ 
        (PULL, "Pull"),
        (PUSH, "Push"),
        (LEGS, "Legs"),
        (SHOULDERS, "Shoulders"),
        (CHEST, "Chest"), 
        (BACK, "Back"),
        (ARMS, "Arms"),
        (NONE, "None"),
     ]
    question = models.ForeignKey(StrengthTrainingQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2, choices=STRENGHT_TRAINING_OPTIONS)
    duration = models.DurationField()

class CardioQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")
    
class CardioAnswer(models.Model):
    WALKING = "WK"
    RUNNING = "RN"
    STAIRMASTER = "SM"
    BIKE = "BK"
    NONE = "NO"
    CARDIO_OPTIONS = [
        (WALKING, "Walking"),
        (RUNNING, "Running"),
        (STAIRMASTER, "Stairmaster"),
        (BIKE, "Bike"),
        (NONE, "None"),
    ]
    question = models.ForeignKey(CardioQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=2, choices=CARDIO_OPTIONS)
    duration = models.DurationField()

class AbsQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")

class AbsAnswer(models.Model):
    question = models.ForeignKey(AbsQuestion, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    duration = models.DurationField()

class StretchQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")

class StretchAnswer(models.Model):
    question = models.ForeignKey(StretchQuestion, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    duration = models.DurationField()

class PilatesQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")

class PilatesAnswer(models.Model):
    question = models.ForeignKey(StretchQuestion, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    duration = models.DurationField()
    video = models.CharField(max_length=250, default="")

class YogaQuestion(models.Model): 
    question_text = models.CharField(max_length=250)
    pub_date = models.DateField("date published")

class YogaAnswer(models.Model):
    question = models.ForeignKey(StretchQuestion, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    duration = models.DurationField()
    video = models.CharField(max_length=250, default="")




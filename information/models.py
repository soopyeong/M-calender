from django.db import models


class AbstractJob(models.Model):

    """Abstract Job"""

    JOB_GROUP_ADVENTURER = "adventurer"
    JOB_GROUP_RESISTANCE = "resistance"
    JOB_GROUP_CYGNUIS = "cygnus"
    JOB_GROUP_HERO = "hero"
    JOB_GROUP_NOVA = "nova"
    JOB_GROUP_FLORA = "flora"
    JOB_GROUP_ANIMA = "anima"
    JOB_GROUP_ZERO = "zero"
    JOB_GROUP_KINESIS = "kinesis"

    JOB_GROUP_CHOICES = (
        (JOB_GROUP_ADVENTURER, "모험가"),
        (JOB_GROUP_RESISTANCE, "레지스탕스"),
        (JOB_GROUP_CYGNUIS, "시그너스"),
        (JOB_GROUP_HERO, "영웅"),
        (JOB_GROUP_NOVA, "노바"),
        (JOB_GROUP_FLORA, "레프"),
        (JOB_GROUP_ANIMA, "아니마"),
        (JOB_GROUP_ZERO, "제로"),
        (JOB_GROUP_KINESIS, "키네시스"),
    )

    JOB_CLASS_WARRIOR = "warrior"
    JOB_CLASS_WIZARD = "wizard"
    JOB_CLASS_ARCHER = "archer"
    JOB_CLASS_THIEF = "thief"
    JOB_CLASS_PIRATE = "pirate"

    JOB_CLASS_CHOICES = (
        (JOB_CLASS_WARRIOR, "전사"),
        (JOB_CLASS_WIZARD, "마법사"),
        (JOB_CLASS_ARCHER, "궁수"),
        (JOB_CLASS_THIEF, "도적"),
        (JOB_CLASS_PIRATE, "해적"),
    )

    job = models.CharField(max_length=8)
    job_first_class = models.CharField(max_length=8, choices=JOB_CLASS_CHOICES)
    job_second_class = models.CharField(
        max_length=8, null=True, blank=True, choices=JOB_CLASS_CHOICES
    )
    job_group = models.CharField(max_length=10, choices=JOB_GROUP_CHOICES)

    class Meta:
        abstract = True


class Union(AbstractJob):

    """Union model"""

    content = models.TextField()

    def __str__(self):
        return self.job


class Link(AbstractJob):

    """Link model"""

    content = models.TextField()

    def __str__(self):
        return self.job

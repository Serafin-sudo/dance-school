from django.db import models

class DayOfTheWeek(models.Model):

    number=models.CharField(max_length=1)
    name=models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.name

class Classroom(models.Model):

    name=models.CharField(max_length=64)
    capacity=models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):

    subject=models.CharField(max_length=64)
    day_of_the_week=models.ForeignKey(DayOfTheWeek, on_delete=models.CASCADE)
    starting_hour=models.CharField(max_length=32)
    classroom=models.ForeignKey(Classroom, on_delete=models.CASCADE)
    school=models.ForeignKey('schoolmanagement.School', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subject

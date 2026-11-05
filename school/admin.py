from django.contrib import admin
from .models import DayOfTheWeek, Classroom, Course

class DayOfTheWeekAdmin(admin.ModelAdmin):
    list_display = ["id", "number", "name"]

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "capacity"]

class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "day_of_the_week", "starting_hour", "classroom", "school"]
    search_fields = ["subject"]

admin.site.register(DayOfTheWeek, DayOfTheWeekAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Course, CourseAdmin)
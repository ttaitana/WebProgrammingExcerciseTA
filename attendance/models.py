from django.db import models

# Create your models here.
# courses = [
#     {
#         'id': 1,
#         'code' : '06016322',
#         'name' : 'WEB PROGRAMMING',
#         'description': 'The course teaches how to build a web application with database using Django framework.'
#     },
#     {
#         'id': 2,
#         'code' : '06026118',
#         'name' : 'IT PROJECT MANAGEMENT',
#         'description': 'The course teaches how to manage IT projects to meet deadline and budget.'
#     }
# ]
# classes = [
#     {
#         'id' : 1,
#         'course_id': 1,
#         'section' : 1,
#         'weekday': 'Thursday',
#         'time' : '9:00 - 13:00',
#         'room' : 'Lab304',
#         'student_amount': 50,
#     },
#     {
#         'id' : 2,
#         'course_id': 1,
#         'section' : 2,
#         'weekday': 'Thursday',
#         'time' : '13:30 - 13:00',
#         'room' : 'Lab304',
#         'student_amount': 55,
#     },
#     {
#         'id' : 3,
#         'course_id': 2,
#         'section' : 1,
#         'weekday': 'Tuesday',
#         'time' : '9:00 - 12:00',
#         'room' : '333',
#         'student_amount': 30,
#     }
# ]

# attendance = [
#     {
#         'class_id': 1,
#         'attend': 49,
#         'absent': 1
#     },
#     {
#         'class_id': 2,
#         'attend': 53,
#         'absent': 2
#     },
#     {
#         'class_id': 3,
#         'attend': 28,
#         'absent': 2
#     },
# ]



class Course(models.Model):
    name = models.CharField(max_length=50)
    describtion = models.TextField()
    semester = models.CharField(max_length=1)
    academic_year = models.CharField(max_length=4)

class Class(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    section = models.SmallIntegerField()
    WEEKDAYS = (
    ('M', 'Monday'),
    ('T', 'Tuseday'),
    ('M', 'Wednesday'),
    ('TH', 'Thursday'),
    ('F', 'Friday'),
    ('S', 'Saturday'),
    ('SU', 'Sunday')
)
    weekday = models.CharField(max_length=2, choices=WEEKDAYS)

class Student(models.Model):
    student_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    year = models.SmallIntegerField()

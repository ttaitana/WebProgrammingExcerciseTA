from django.db import models

# Create your models here.

course = {
    '06016900' : {
        'id': '06016900',
        'name' : 'Web Programming',
        'detail': "This subject will teach you about backend for Website",
        'std_amount' : 40,
        'std_come' : 30,
        'std_absent' : 10
    },
    '06016800' : {
        'id': '06016800',
        'name' : 'Web Progressive',
        'detail': "This subject will teach you about web progressive",
        'std_amount' : 40,
        'std_come' : 25,
        'std_absent' : 15
    },
    '04015200' : {
        'id': '04015200',
        'name' : 'Chinese',
        'detail': "This subject will teach you about basic Chinese",
        'std_amount' : 20,
        'std_come' : 14,
        'std_absent' : 6
    },
}

timetable = {
    "user" : [
        {
            "name" : "Jack", 
            "table" : {
                "Monday": [
                    {
                        "time": "9.00",
                        "subject": "Web Programming",
                        "id" : '06016900'
                    },
                    {
                        "time": "13.00",
                        "subject": "Web Progressive",
                        "id" : "06016800"
                    }
                ],
                "Tuesday": [
                    {
                        "time": "9.00",
                        "subject": "Chinese",
                        "id" : '04015200'
                    }
                ],
                "Wednesday": [
                ],
                "Thurseday": [
                    {
                        "time": "9.00",
                        "subject": "Web Programming",
                        "id" : '06016900'
                    }
                ],
                "Friday": [
                    {
                        "time": "9.00",
                        "subject": "Chinese",
                        "id" : '04015200'
                    }
                ]
            }
        }
    ],    
}
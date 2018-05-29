from django.contrib import admin
from .models import User, golf_course, golfround
from django.contrib.auth.admin import UserAdmin

#django admin profile view to change golf courses and golf rounds

@admin.register(golf_course)
class golf_courseAdmin(admin.ModelAdmin):
    list_display=('name', 'par', 'length')
    fields = [('name','par'),('rating','length'), ('hole_1_par', 'hole_1_yard'),
    ('hole_2_par', 'hole_2_yard'),
    ('hole_3_par', 'hole_3_yard'),
    ('hole_4_par', 'hole_4_yard'),
    ('hole_5_par', 'hole_5_yard'),
    ('hole_6_par', 'hole_6_yard'),
    ('hole_7_par', 'hole_7_yard'),
    ('hole_8_par', 'hole_8_yard'),
    ('hole_9_par', 'hole_9_yard'),
    ('hole_10_par', 'hole_10_yard'),
    ('hole_11_par', 'hole_11_yard'),
    ('hole_12_par', 'hole_12_yard'),
    ('hole_13_par', 'hole_13_yard'),
    ('hole_14_par', 'hole_14_yard'),
    ('hole_15_par', 'hole_15_yard'),
    ('hole_16_par', 'hole_16_yard'),
    ('hole_17_par', 'hole_17_yard'),
    ('hole_18_par', 'hole_18_yard')
]
    

@admin.register(golfround)
class golf_roundAdmin(admin.ModelAdmin):
    list_display=('golfer', 'date')
    fields = ['golf_course', ('golfer', 'date'), 
    'hole_1_score',
    'hole_2_score',
    'hole_3_score',
    'hole_4_score',
    'hole_5_score',
    'hole_6_score',
    'hole_7_score',
    'hole_8_score',
    'hole_9_score',
    'hole_10_score',
    'hole_11_score',
    'hole_12_score',
    'hole_13_score',
    'hole_14_score',
    'hole_15_score',
    'hole_16_score',
    'hole_17_score',
    'hole_18_score'
    ]



    



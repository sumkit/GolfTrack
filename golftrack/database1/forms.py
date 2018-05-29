from django import forms
from django.forms import ModelForm
from database1.models import User, golfround, golf_course
from django.contrib.auth.forms import UserCreationForm

#forms to add model objects to database

class courseForm(forms.ModelForm):
    class Meta:
        model = golf_course
        fields = ['name','par','length', 'rating',
        'hole_1_par', 'hole_1_yard',
        'hole_2_par', 'hole_2_yard',
        'hole_3_par', 'hole_3_yard',
        'hole_4_par', 'hole_4_yard',
        'hole_5_par', 'hole_5_yard',
        'hole_6_par', 'hole_6_yard',
        'hole_7_par', 'hole_7_yard',
        'hole_8_par', 'hole_8_yard',
        'hole_9_par', 'hole_9_yard',
        'hole_10_par', 'hole_10_yard',
        'hole_11_par', 'hole_11_yard',
        'hole_12_par', 'hole_12_yard',
        'hole_13_par', 'hole_13_yard',
        'hole_14_par', 'hole_14_yard',
        'hole_15_par', 'hole_15_yard',
        'hole_16_par', 'hole_16_yard',
        'hole_17_par', 'hole_17_yard',
        'hole_18_par', 'hole_18_yard',
    ]



class inputroundForm(forms.ModelForm):
    class Meta:
        model = golfround
        fields = ('golf_course', 'date', 'fairways', 'greens',
    'hole_1_score', 'hole_1_putts',
    'hole_2_score', 'hole_2_putts',
    'hole_3_score', 'hole_3_putts', 
    'hole_4_score', 'hole_4_putts',
    'hole_5_score', 'hole_5_putts',
    'hole_6_score', 'hole_6_putts',
    'hole_7_score', 'hole_7_putts', 
    'hole_8_score', 'hole_8_putts',
    'hole_9_score', 'hole_9_putts',
    'hole_10_score', 'hole_10_putts',
    'hole_11_score', 'hole_11_putts',
    'hole_12_score', 'hole_12_putts',
    'hole_13_score', 'hole_13_putts',
    'hole_14_score', 'hole_14_putts',
    'hole_15_score', 'hole_15_putts',
    'hole_16_score', 'hole_16_putts',
    'hole_17_score', 'hole_17_putts', 
    'hole_18_score', 'hole_18_putts'
    )
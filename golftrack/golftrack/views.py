from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.base import View
from django.urls import reverse
from django.contrib.auth.models import User
from database1.models import golf_course, golfround
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from database1.forms import inputroundForm, courseForm

'''this file includes all the views used in the app.
it also includes some of the data processing to be passed as context
to diplay on template files
'''
#home page no required login
def home(request):
	num_users = User.objects.all().count()
	num_courses = golf_course.objects.all().count()
	context={}
	context['num_users']=num_users
	context['num_courses']=num_courses
	return render(request, 'home.html', context)

#register a new user
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


#adding round to database
def inputRound(request):
	if request.method == 'POST':
		form = inputroundForm(request.POST)
		if form.is_valid():
			date=form.cleaned_data['date']
			golf_course=form.cleaned_data['golf_course']
			fairways=form.cleaned_data['fairways']
			greens=form.cleaned_data['grees']
			putts=fom.cleaned_data['putts']
			hole_1_score=form.cleaned_data['hole_1_score']
			hole_2_score=form.cleaned_data['hole_2_score']
			hole_3_score=form.cleaned_data['hole_3_score']
			hole_4_score=form.cleaned_data['hole_4_score']
			hole_5_score=form.cleaned_data['hole_5_score']
			hole_6_score=form.cleaned_data['hole_6_score']
			hole_7_score=form.cleaned_data['hole_7_score']
			hole_8_score=form.cleaned_data['hole_8_score']
			hole_9_score=form.cleaned_data['hole_9_score']
			hole_10_score=form.cleaned_data['hole_10_score']
			hole_11_score=form.cleaned_data['hole_11_score']
			hole_12_score=form.cleaned_data['hole_12_score']
			hole_13_score=form.cleaned_data['hole_13_score']
			hole_14_score=form.cleaned_data['hole_14_score']
			hole_15_score=form.cleaned_data['hole_15_score']
			hole_16_score=form.cleaned_data['hole_16_score']
			hole_17_score=form.cleaned_data['hole_17_score']
			hole_18_score=form.cleaned_data['hole_18_score']
			new_golfround = golfround(date=date,
				golfer=request.user,
				golf_course=golf_course,
				hole_1_score=hole_1_score,
				hole_2_score=hole_2_score,
				hole_3_score=hole_3_score,
				hole_4_score=hole_4_score,
				hole_5_score=hole_5_score,
				hole_6_score=hole_6_score,
				hole_7_score=hole_7_score,
				hole_8_score=hole_8_score,
				hole_9_score=hole_9_score,
				hole_10_score=hole_10_score,
				hole_11_score=hole_11_score,
				hole_12_score=hole_12_score,
				hole_13_score=hole_13_score,
				hole_14_score=hole_14_score,
				hole_15_score=hole_15_score,
				hole_16_score=hole_16_score,
				hole_17_score=hole_17_score,
				hole_18_score=hole_18_score
				)
			new_golfround.save()
			return redirect('profile')
	else:
		form = inputroundForm()
	return render(request, 'golf_round_form.html', {'form': form})

#add golf course to database
def addCourse(request):
	if request.method == 'POST':
		form = courseForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			par=form.cleaned_data['par']
			length=form.cleaned_data['length']
			rating=form.cleaned_data['rating']
			hole_1_par=form.cleaned_data['hole_1_par']
			hole_1_yard=form.cleaned_data['hole_1_yard']
			hole_2_par=form.cleaned_data['hole_2_par']
			hole_2_yard=form.cleaned_data['hole_2_yard']
			hole_3_par=form.cleaned_data['hole_3_par']
			hole_3_yard=form.cleaned_data['hole_3_yard']
			hole_4_par=form.cleaned_data['hole_4_par']
			hole_4_yard=form.cleaned_data['hole_4_yard']
			hole_5_par=form.cleaned_data['hole_5_par']
			hole_5_yard=form.cleaned_data['hole_5_yard']
			hole_6_par=form.cleaned_data['hole_6_par']
			hole_6_yard=form.cleaned_data['hole_6_yard']
			hole_7_par=form.cleaned_data['hole_7_par']
			hole_7_yard=form.cleaned_data['hole_7_yard']
			hole_8_par=form.cleaned_data['hole_8_par']
			hole_8_yard=form.cleaned_data['hole_8_yard']
			hole_9_par=form.cleaned_data['hole_9_par']
			hole_9_yard=form.cleaned_data['hole_9_yard']
			hole_10_par=form.cleaned_data['hole_10_par']
			hole_10_yard=form.cleaned_data['hole_10_yard']
			hole_11_par=form.cleaned_data['hole_11_par']
			hole_11_yard=form.cleaned_data['hole_11_yard']
			hole_12_par=form.cleaned_data['hole_12_par']
			hole_12_yard=form.cleaned_data['hole_12_yard']
			hole_13_par=form.cleaned_data['hole_13_par']
			hole_13_yard=form.cleaned_data['hole_13_yard']
			hole_14_par=form.cleaned_data['hole_14_par']
			hole_14_yard=form.cleaned_data['hole_14_yard']
			hole_15_par=form.cleaned_data['hole_15_par']
			hole_15_yard=form.cleaned_data['hole_15_yard']
			hole_16_par=form.cleaned_data['hole_16_par']
			hole_16_yard=form.cleaned_data['hole_16_yard']
			hole_17_par=form.cleaned_data['hole_17_par']
			hole_17_yard=form.cleaned_data['hole_17_yard']
			hole_18_par=form.cleaned_data['hole_18_par']
			hole_18_yard=form.cleaned_data['hole_18_yard']
			new_course = golf_course(name=name,
				par=par,
				length=length,
				rating=rating,
				hole_1_par=hole_1_par,
				hole_1_yard=hole_1_yard,
				hole_2_par=hole_2_par,
				hole_2_yard=hole_2_yard,
				hole_3_par=hole_3_par,
				hole_3_yard=hole_3_yard,
				hole_4_par=hole_4_par,
				hole_4_yard=hole_4_yard,
				hole_5_par=hole_5_par,
				hole_5_yard=hole_5_yard,
				hole_6_par=hole_6_par,
				hole_6_yard=hole_6_yard,
				hole_7_par=hole_7_par,
				hole_7_yard=hole_7_yard,
				hole_8_par=hole_8_par,
				hole_8_yard=hole_8_yard,
				hole_9_par=hole_9_par,
				hole_9_yard=hole_9_yard,
				hole_10_par=hole_10_par,
				hole_10_yard=hole_10_yard,
				hole_11_par=hole_11_par,
				hole_11_yard=hole_11_yard,
				hole_12_par=hole_12_par,
				hole_12_yard=hole_12_yard,
				hole_13_par=hole_13_par,
				hole_13_yard=hole_13_yard,
				hole_14_par=hole_14_par,
				hole_14_yard=hole_14_yard,
				hole_15_par=hole_15_par,
				hole_15_yard=hole_15_yard,
				hole_16_par=hole_16_par,
				hole_16_yard=hole_16_yard,
				hole_17_par=hole_17_par,
				hole_17_yard=hole_17_yard,
				hole_18_par=hole_18_par,
				hole_18_yard=hole_18_yard
				)

			new_course.save()
			return redirect('home')
	else:
		form = courseForm()
	return render(request, 'course_form.html', {'form': form})

#display courses in database
def CourseList(request):
	context = {}
	courses = golf_course.objects.all()
	for course in courses:
		par = course.par

	context['courses'] = courses
	print(courses)
	return render(request, 'golf_course_list.html', context)

#display course info
def course(request, course):
	context={}
	rounds = golfround.objects.filter(golf_course__name__startswith = course)
	context['rounds']=rounds
	CourseList = golf_course.objects.filter(name__startswith = course)
	course = CourseList[0]
	print(course)
	context['course']=course
	return render(request, 'course.html', context)

#main profile page, login required
@login_required
def profile(request):
	context = {}
	#order rounds reverse chronological 
	rounds = golfround.objects.filter(golfer=request.user).order_by('-date')
	context['user'] = request.user
	user = request.user
	context['username'] = user.username
	context['rounds'] = rounds
	print(rounds)
	return render(request, 'profile.html', context)


#profile statistics page
@login_required
def stats(request):
	context = {}
	rounds = golfround.objects.filter(golfer=request.user)
	#calculating averages for all data passed through context
	roundsplayed = len(rounds)
	handicapsum = 0
	parcount = 0
	birdiecount = 0
	bogeycount = 0
	eaglecount = 0
	doublecount = 0
	otherscount = 0
	par3sum = 0
	par4sum = 0
	par5sum = 0
	FIRs = 0
	GIRs = 0
	putts = 0
	OnePutts = 0
	TwoPutts = 0
	ThreePutts = 0
	for round in rounds:
		handicapsum += round.get_handicap()
		parcount += round.get_pars()
		birdiecount += round.get_birdies()
		bogeycount += round.get_bogeys()
		eaglecount += round.get_eagles()
		doublecount += round.get_doubles()
		otherscount += round.get_others()
		par3sum += round.par3average()
		par4sum += round.par4average()
		par5sum += round.par5average()
		FIRs += round.fairways
		GIRs += round.greens
		putts += round.putts()
		OnePutts += round.onePutts()
		TwoPutts += round.twoPutts()
		ThreePutts += round.threePutts()

	handicap = handicapsum/len(rounds)
	par3average = par3sum/len(rounds)
	par4average = par4sum/len(rounds)
	par5average = par5sum/len(rounds)
	FIRav= FIRs/len(rounds)
	GIRav= GIRs/len(rounds)
	PuttAv= putts/len(rounds)
	OnePutts /= len(rounds)
	TwoPutts /= len(rounds)
	ThreePutts /= len(rounds)
	averages = [ par3average, par4average, par5average]
	averages1 = [ FIRav, GIRav]
	#adding data to context dictionary
	context['roundsplayed']=roundsplayed
	context['rounds']=rounds
	context['handicap']=handicap
	context['parcount']=parcount
	context['birdiecount']=birdiecount
	context['bogeycount']=bogeycount
	context['eaglecount']=eaglecount
	context['doublecount']=doublecount
	context['otherscount']=otherscount
	context['averages']=averages
	context['averages1']=averages1
	context['FIRav'] = FIRav
	context['GIRav'] = GIRav
	context['PuttAv']=PuttAv
	puttingStats=[ OnePutts, TwoPutts, ThreePutts]
	context['puttingStats']=puttingStats

	
	return render(request, 'stats.html', context)

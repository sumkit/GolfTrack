from django.db import models
import uuid, datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

#all my models are created here

class golf_course(models.Model):
	name = models.CharField(max_length=100, help_text='Golf Course Name')
	par = models.IntegerField()
	length = models.IntegerField()
	rating = models.DecimalField(default=0, max_digits=4, decimal_places=1)
	hole_1_par = models.IntegerField()
	hole_2_par = models.IntegerField()
	hole_3_par = models.IntegerField()
	hole_4_par = models.IntegerField()
	hole_5_par = models.IntegerField()
	hole_6_par = models.IntegerField()
	hole_7_par = models.IntegerField()
	hole_8_par = models.IntegerField()
	hole_9_par = models.IntegerField()
	hole_10_par = models.IntegerField()
	hole_11_par = models.IntegerField()
	hole_12_par = models.IntegerField()
	hole_13_par = models.IntegerField()
	hole_14_par = models.IntegerField()
	hole_15_par = models.IntegerField()
	hole_16_par = models.IntegerField()
	hole_17_par = models.IntegerField()
	hole_18_par = models.IntegerField()
	hole_1_yard = models.IntegerField()
	hole_2_yard = models.IntegerField()
	hole_3_yard = models.IntegerField()
	hole_4_yard = models.IntegerField()
	hole_5_yard = models.IntegerField()
	hole_6_yard = models.IntegerField()
	hole_7_yard = models.IntegerField()
	hole_8_yard = models.IntegerField()
	hole_9_yard = models.IntegerField()
	hole_10_yard = models.IntegerField()
	hole_11_yard = models.IntegerField()
	hole_12_yard = models.IntegerField()
	hole_13_yard = models.IntegerField()
	hole_14_yard = models.IntegerField()
	hole_15_yard = models.IntegerField()
	hole_16_yard = models.IntegerField()
	hole_17_yard = models.IntegerField()
	hole_18_yard = models.IntegerField()

	def __str__(self):
		return self.name

	def get_total_par(self):
		return int(
				self.hole_1_par+
				self.hole_2_par+
				self.hole_3_par+
				self.hole_4_par+
				self.hole_5_par+
				self.hole_6_par+
				self.hole_7_par+
				self.hole_8_par+
				self.hole_9_par+
				self.hole_10_par+
				self.hole_11_par+
				self.hole_12_par+
				self.hole_13_par+
				self.hole_14_par+
				self.hole_15_par+
				self.hole_16_par+
				self.hole_17_par+
				self.hole_18_par
			)

	def get_total_yardage(self):
		return int(
				self.hole_1_yard+
				self.hole_2_yard+
				self.hole_3_yard+
				self.hole_4_yard+
				self.hole_5_yard+
				self.hole_6_yard+
				self.hole_7_yard+
				self.hole_8_yard+
				self.hole_9_yard+
				self.hole_10_yard+
				self.hole_11_yard+
				self.hole_12_yard+
				self.hole_13_yard+
				self.hole_14_yard+
				self.hole_15_yard+
				self.hole_16_yard+
				self.hole_17_yard+
				self.hole_18_yard
			)

class golfround(models.Model):
	#golf round characteristics
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date = models.DateField(help_text='MM/DD/YYYY')
	golfer = models.ForeignKey(User, null=True, blank=True)
	golf_course = models.ForeignKey('golf_course')
	fairways = models.IntegerField(default=14)
	greens = models.IntegerField(default=18)
	hole_1_score = models.IntegerField()
	hole_1_putts = models.IntegerField(default=2)
	hole_2_score = models.IntegerField()
	hole_2_putts = models.IntegerField(default=2)
	hole_3_score = models.IntegerField()
	hole_3_putts = models.IntegerField(default=2)
	hole_4_score = models.IntegerField()
	hole_4_putts = models.IntegerField(default=2)
	hole_5_score = models.IntegerField()
	hole_5_putts = models.IntegerField(default=2)
	hole_6_score = models.IntegerField()
	hole_6_putts = models.IntegerField(default=2)
	hole_7_score = models.IntegerField()
	hole_7_putts = models.IntegerField(default=2)
	hole_8_score = models.IntegerField()
	hole_8_putts = models.IntegerField(default=2)
	hole_9_score = models.IntegerField()
	hole_9_putts = models.IntegerField(default=2)
	hole_10_score = models.IntegerField()
	hole_10_putts = models.IntegerField(default=2)
	hole_11_score = models.IntegerField()
	hole_11_putts = models.IntegerField(default=2)
	hole_12_score = models.IntegerField()
	hole_12_putts = models.IntegerField(default=2)
	hole_13_score = models.IntegerField()
	hole_13_putts = models.IntegerField(default=2)
	hole_14_score = models.IntegerField()
	hole_14_putts = models.IntegerField(default=2)
	hole_15_score = models.IntegerField()
	hole_15_putts = models.IntegerField(default=2)
	hole_16_score = models.IntegerField()
	hole_16_putts = models.IntegerField(default=2)
	hole_17_score = models.IntegerField()
	hole_17_putts = models.IntegerField(default=2)
	hole_18_score = models.IntegerField()
	hole_18_putts = models.IntegerField(default=2)

	def __str__(self):
		return str(self.golfer)

	def get_absolute_url(self):
		return reverse('profile:detail', kwargs={'pk': self.pk})


	def get_total_score(self):
		return int(
				self.hole_1_score+
				self.hole_2_score+
				self.hole_3_score+
				self.hole_4_score+
				self.hole_5_score+
				self.hole_6_score+
				self.hole_7_score+
				self.hole_8_score+
				self.hole_9_score+
				self.hole_10_score+
				self.hole_11_score+
				self.hole_12_score+
				self.hole_13_score+
				self.hole_14_score+
				self.hole_15_score+
				self.hole_16_score+
				self.hole_17_score+
				self.hole_18_score
			)

	def get_overpar(self):
		par = self.golf_course.par
		total = self.get_total_score()
		return total - par

	def GIRpercentage(self):
		greens = self.greens
		return greens/18

	def FIRpercentage(self):
		fairways = self.greens
		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]
		count = 0
		for hole in ParList:
			if hole > 3:
				count +=1

		return fairways/count

	def putts(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			count += hole
		return count
	def puttAverage(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		averageSum = 0
		for hole in puttList:
			averageSum += hole

		return averageSum/len(puttList)

	def getNumPutts(self, num):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			if hole == num:
				count += 1
		return count

	def get_handicap(self):
		difficulty = self.golf_course.rating
		score = self.get_total_score()
		return score - difficulty

	#get average for a certain par hole
	def getAverage(self, par):
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		count = 0
		score = 0
		
		for i in range(len(ParList)):
			if ParList[i] == par:
				score += ScoreList[i]
				count += 1
		return score/count

'''
	def onePutts(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			if hole == 1:
				count += 1
		return count

	def twoPutts(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			if hole == 2:
				count += 1
		return count

	def threePutts(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			if hole == 3:
				count += 1
		return count

	def otherPutts(self):
		puttList = [
		self.hole_1_putts,
		self.hole_2_putts,
		self.hole_3_putts,
		self.hole_4_putts,
		self.hole_5_putts,
		self.hole_6_putts,
		self.hole_7_putts,
		self.hole_8_putts,
		self.hole_9_putts,
		self.hole_10_putts,
		self.hole_11_putts,
		self.hole_12_putts,
		self.hole_13_putts,
		self.hole_14_putts,
		self.hole_15_putts,
		self.hole_16_putts,
		self.hole_17_putts,
		self.hole_18_putts,
		]
		count = 0
		for hole in puttList:
			if hole > 3:
				count += 1
		return count
'''
def get_pars(self):
		pars = 0
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		for i in range(len(ParList)):
			if ScoreList[i] == ParList[i]:
				pars += 1
		return pars

def get_birdies(self):
		birdies = 0
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		for i in range(len(ParList)):
			if ScoreList[i] + 1 == ParList[i]:
				birdies += 1
		return birdies

def get_eagles(self):
		eagles = 0
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		for i in range(len(ParList)):
			if ScoreList[i] + 2 == ParList[i]:
				eagles += 1
		return eagles
			
def get_bogeys(self):
		bogeys = 0
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		for i in range(len(ParList)):
			if ScoreList[i] - 1 == ParList[i]:
				bogeys += 1
		return bogeys

def get_doubles(self):
		doubles = 0
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		for i in range(len(ParList)):
			if ScoreList[i] - 2 == ParList[i]:
				doubles += 1
		return doubles

def get_others(self):
		return (
			18 - 
			self.get_pars() - 
			self.get_birdies() - 
			self.get_eagles() - 
			self.get_bogeys() - 
			self.get_doubles()
			)

'''		
def par4average(self):
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		count = 0
		score = 0
		
		for i in range(len(ParList)):
			if ParList[i] == 4:
				score += ScoreList[i]
				count += 1
		return score/count

def par5average(self):
		ScoreList = [
		self.hole_1_score,
		self.hole_2_score,
		self.hole_3_score,
		self.hole_4_score,
		self.hole_5_score,
		self.hole_6_score,
		self.hole_7_score,
		self.hole_8_score,
		self.hole_9_score,
		self.hole_10_score,
		self.hole_11_score,
		self.hole_12_score,
		self.hole_13_score,
		self.hole_14_score,
		self.hole_15_score,
		self.hole_16_score,
		self.hole_17_score,
		self.hole_18_score,
		]

		ParList = [
		self.golf_course.hole_1_par,
		self.golf_course.hole_2_par,
		self.golf_course.hole_3_par,
		self.golf_course.hole_4_par,
		self.golf_course.hole_5_par,
		self.golf_course.hole_6_par,
		self.golf_course.hole_7_par,
		self.golf_course.hole_8_par,
		self.golf_course.hole_9_par,
		self.golf_course.hole_10_par,
		self.golf_course.hole_11_par,
		self.golf_course.hole_12_par,
		self.golf_course.hole_13_par,
		self.golf_course.hole_14_par,
		self.golf_course.hole_15_par,
		self.golf_course.hole_16_par,
		self.golf_course.hole_17_par,
		self.golf_course.hole_18_par,
		]

		count = 0
		score = 0
		
		for i in range(len(ParList)):
			if ParList[i] == 5:
				score += ScoreList[i]
				count += 1
		return score/count
'''

	



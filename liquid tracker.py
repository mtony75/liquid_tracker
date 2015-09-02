import datetime
import string
import os

# Quick program to track milk and juice expiration 

# Class liquid
# variables name, size
# functions whenExpire, daysLeft, isGood, pour
# private functions __setExpire, __setCapacity
# private variables __expire, __isLeft, __capacity 

# Phase 1 Create class and functions
# Phase 2 Allow user to add liquids
# Phase 3 Create text menu system to allow user to check on liquids
# Phase 4 Create gui app to access 

#Phase 1 Class and functions

class Liquid:
	name = "" # name of the liquid
	__expire = datetime.date.today() # initialize expiration date to today until set
	__capacity = 0
	__isLeft = 0 # in ounces
	
	def __init__(self, name, enddate, capacity):
		self.name = name
#		__setExpire(enddate)
		self.__expire = enddate
		self.setCapacity(capacity)
		
#	def __setExpire(self, endDate):
#		self.__expire = endDate
		
	def setCapacity(self, capacity): # initialize the capacity and current volume "isLeft" to save value 
		self.__capacity = capacity
		self.__isLeft = capacity
	
	def whenExpire(self): # shows when the expiration date is without exposing the value outside class
		return self.__expire
	
	def pour(self, amount): # amount in ounces to be removed from liquid
		__capacity = __capacity - amount
	
	def daysLeft(self): # function to see how many days till liquid expires.
		now = datetime.date.today() # set current date as now
		expire = self.__expire - now
		print "expire date {} , today {}".format(self.__expire,now)
		print "They are {} days left until the {} expires".format(expire.days,self.name)
		
	def isGood(self, expire):
		now = datetime.date.today()
		expire = __expire - now
		if expire.days > 0:
			return TRUE
			
	def isLeft(self):
		return self.__capacity

def checkValidDate(date): # check if date is in valid format
# If Date is before today the check fails and is a message is sent to the user.

	todayDate = datetime.date.today()
	if date.year < todayDate.year:
		return False
	elif date.year == todayDate.year and date.month < todayDate.month:
		return False
	elif date.year == todayDate.year and date.month == todayDate.month and date.day < todayDate.day:
		return False
	else:
		return True
	
def inputMenu():# menu to present user with options about liquids
	print "**************************************************"
	print "* 1. Add Liquid                                  *"
	print "* 2. List Liquids                                *"
	print "* 3. Pick Liquid                                 *"
	print "* 4. Purge Expired                               *"
	print "* 5. Exit                                        *"
	print "**************************************************"

def listLiquids(inventory): # Function to list all liquids in inventory
	for x in liquidInventory:
			print "{}, {} oz, expires {}".format(x.name,x.isLeft(),x.whenExpire())
	
def pickLiquid():
	print ""

def addLiquid(): # Function to add new liquid to inventory
	inputDate = raw_input("Enter a date in MM-DD-YYYY format with the dashes(-)")
	inputName = raw_input("Enter name of liquid: ")
	inputVolume = raw_input("Enter amount of liquid: ")
	fullDateString = inputDate.split('-', 3)
	expirationDate = datetime.date(int(fullDateString[2]),int(fullDateString[0]),int(fullDateString[1]))
	#print expirationDate
	if checkValidDate(expirationDate):
		liquid02 = Liquid(inputName,expirationDate,int(inputVolume))
	else:
		print ("Not a valid date")
		return False
	return liquid02
	
#endDate = datetime.date(2015,12,02)				
#liquid01 = Liquid("Milk",endDate,64)

#print liquid01.name
#liquid01.whenExpire()
#liquid01.daysLeft()
	
selection = ""
liquidInventory = []

while selection != "Exit":
	os.system('cls')
	inputMenu()
	selection = int(raw_input())
	if selection == 1 :
		liquidInventory.append(addLiquid())
	if selection == 2 :
		listLiquids(liquidInventory)
		raw_input()
		



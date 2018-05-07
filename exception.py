
#user   defined   exception#

class Error(Exception):
    ''' this is  the base exception'''
#print(Error.__file__)    
class Underage(Error):
	''' this erroe is raised when the age is less '''
class Overage(Error):
	''' this error is raised when the age  the person is more'''
class Notyetborn(Error):
	'''PERSON IS NOT BORN'''
age1=25
while True:

	try:
		age=int(input("enter the  age"))
		if (age<=0):
			raise Notyetborn
		elif (age>age1):
			raise Overage
		elif (age<age1):
			raise Underage
		break
	except Notyetborn:
		print("the person is not yet  born \n")
	except Overage:
		print("the person is of more age \n")
	except Underage:
		print("the person is of less age \n")
	finally:
		# print("you have entered some age")	
		pass
print("you have successfully entered the age")		
	
						
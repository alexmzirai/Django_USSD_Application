from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
	"""normally you receive a POST from the frontend, when form is filled by user.
		But for USSD, the POST info is sent directly to the server when user dials service code. 
		According to Africas Talking, the first response variable in either an 'if' statement or 'elif'
		statement must  begin with CON.This is the first message that appears on user's screen immediately
		after dialling a USSD code.
	"""
	if request.method == 'POST':
		session_id = request.POST.get('session_Id')
		service_code = request.POST.get('serviceCode')
		phone_number = request.POST.get('phoneNumber')
		text = request.POST.get('text')

		response = ""

		if text == "":
			response = 'CON What would you want to check?\n'
			# response = "1. My Account\n"
			response += "1. My phone number"

		elif text == "1":
			response = "END My Phone Number is {0}".format(phone_number)
		return HttpResponse(request)  # allows a function to return a response

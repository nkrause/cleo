from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
#from tickets.models import Ticket
#from tickets.serializers import TicketSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return JsonResponse({
        	'status': 200,
        	'data': {
        		'message': 'Hello World'
        	},
        	'message': 'login successful'
    	})

@api_view(['GET','POST'])
#if we change to @api_view(['POST']) we can test using the following command
#http --form POST http://127.0.0.1:8000/login/ username=username password=password
def login(request):
	statusCode = 200
	username = request.POST.get("username")
	password = request.POST.get("password")
	if not username or not password:
		return JsonResponse({
			'status': 400, 
			'data': { },
			'error': 'true',
 			'message': 'username: %s and/or password: ***** is undefined' % (username)
		})

	return JsonResponse({
			'status':200, 
			'data':{
			'user': {
				'sesion': '123asdert',
				'username': 'testUser',
				'email': 'test@user.com',
				'name': 'Test User',
				}
			},
			'message': 'login successful'
		})

@api_view(['GET','POST'])
#http --form POST http://127.0.0.1:8000/tickets/
def ticket_list(request):
	statusCode = 200
	if statusCode == 200:
		return JsonResponse({
			'status': 200, 
			'data': {
				'tickets': [
					123,
					456,
					678,
					789
				]
			},
			'message': 'Here are your tickets'
		})
	else:
		return JsonResponse({
			'status': 400, 
			'data': { },
			'error': 'true',
			'message': 'Session is undefined'
		})


@api_view(['GET','POST'])
#http --form POST http://127.0.0.1:8000/ticket/123/
def ticket_detail(request, pk):
	return JsonResponse({
			'status': 200, 
			'data': {
				'ticket': {
					'name': 'test Ticket response',
					'id': pk
				}
			},
			'message': 'Ticket: %d is yours' % (pk)
		})
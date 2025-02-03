from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

import requests

# Create your views here.

def is_prime(n : int) -> bool:
    if n > 1:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True
    return False

def is_perfect(n : int) -> bool:
    if n > 0:
        return n == sum(i for i in range(1,n) if n % i == 0 )
    return False

def is_amstrong(n : int) -> bool:
   return n == sum(int(digit) ** len(str(n)) for digit in str(n))

def get_fun_fact(n : int) -> str:
    # make a request to the numbers api and return a fun fact about that number
    try:
        response = requests.get(f'http://numbersapi.com/{n}/math?json')
        if response.status_code == 200:
            return response.json().get('text')
        return 'No fun fact available'
    except:
        return 'Could not retrieve fun fact'
        


@api_view(['GET'])
def classify_number(request):
    number = request.GET.get('number')
    # sum digits is the sum of its digits
    if number is not None:
        
        try:
            number = int(number)
            if number:
                properties = []
                if is_amstrong(number):
                    properties.append('amstrong')
                properties.append('even' if number % 2 == 0 else "odd")
                data = {
                    "number": number,
                    "is_prime" : is_prime(number),
                    "is_perfect" : is_perfect(number),
                    "properties" : properties,
                    "digit_sum" : sum(int(digit) for digit in str(number)),
                    "fun_fact" : get_fun_fact(number)
                    }
                return Response(data, status=HTTP_200_OK)
        except:
            data = {
                "number" : "alphabet",
                "error" : True
            }
            return Response(data, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_200_OK)

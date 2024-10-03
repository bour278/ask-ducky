from django.shortcuts import render
from django.http import JsonResponse
from .askblue import ask_blue
from .askchad import ask_chad

# Create your views here.

def home(request):
    return render(request, 'home.html')

def get_response(request):
    query = request.GET.get('query')
    api_type = request.GET.get('api_type')
    
    try:
        if api_type == 'gemini':
            response = ask_blue(query)
        else:
            response = ask_chad(query)
        return JsonResponse({'response': response})
    except Exception as e:
        print(f"Error: {e}")  # Print the error to the console
        return JsonResponse({'error': str(e)}, status=500)
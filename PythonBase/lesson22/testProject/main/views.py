from django.shortcuts import render


# Create your views here.
def index(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Name: {name}\nEmail: {email}\nMessage: {message}')

    return render(request, 'main/index.html')



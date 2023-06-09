from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'usernames': ['kar', 'unclear legacy', 'lender', 'cyreh', 'cyreh', 'cyreh', 'cyreh', 'cyreh']
    }
    return render(request, 'cubeapp/index.html', context)

from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    context = {
        # 'user' : [User]
        'usernames': ['kar', 'unclear legacy', 'lender', 'cyreh', 'cyreh', 'cyreh', 'cyreh', 'cyreh']
    }
    return render(request, 'cubeapp/index.html', context)

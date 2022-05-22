from django.shortcuts import render
from faker import Faker
import random
# Create your views here.

def index(request):
    fake = Faker()
    initials = fake.name()
    n = random.randint(3, 6)
    m = random.randint(4, 6)
    initials = initials.split()[0][0:n]  + initials.split()[1][0:m]
    num = random.randint(10,9999)
    name = initials.lower() + str(num)
    return render(request, 'index.html', {'name': name})
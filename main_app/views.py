from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Bug:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

bugs = [
  Bug('Lolo', 'tabby', 'foul little demon', 3),
  Bug('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Bug('Raven', 'black tripod', '3 legged bug', 4)
]

# Define the home view
def home(request):
  return render(request, 'bugs/index.html')

def about(request):
  return render(request, 'about.html')

def bugs_index(request):
  return render(request, 'bugs/index.html', { 'bugs': bugs })
from django.shortcuts import render

# Create your views here.

def HomePageView(request):
  context = {}
  return render(request, 'portfolio/home.html', context)
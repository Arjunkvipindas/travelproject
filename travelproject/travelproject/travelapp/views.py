from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':team})

#def add(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #Add=x+y
    #Sub=x-y
  #  Mul=x*y
   # Div=x/y
    #return render(request,"result.html",{'add':Add,'sub':Sub,'mul':Mul,'div':Div})

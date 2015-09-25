from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.
def home(request):
    form = SignUpForm(request.POST or None)
    title = "Welcome"
    context = {
        "tempalte_title":title,
        "form":form
    }

    if (form.is_valid()):
        instanse = form.save(commit=True)
        if not instanse.full_name:
             instanse.full_name = "Ashish"
             context = {
                 "tempalte_title":"Thank You"
             }



    return render(request,'home.html',context)
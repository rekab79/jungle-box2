from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from django.template import loader
from .models import GrowProfile



def register(request):
    template = loader.get_template('jungle/register.html')
    
    return HttpResponse(template.render(context,request))

def index(request):
    all_profiles = GrowProfile.objects.all()
    template = loader.get_template('jungle/index.html')
    context = {
        'all_profiles': all_profiles,
    }
    return HttpResponse(template.render(context,request))
  

class UserFormView(View):
    form_class=UserForm
    template_name= 'jungle/register.html'
    
    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    
    #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            #(normalized)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #returns User Objects ud credetiansla are valid
            user = authenticate(username=username,password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('jungle:index')
        return render(request,self.template_name,{'form':form})
                
            
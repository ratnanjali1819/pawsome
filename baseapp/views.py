from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import Dog
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login 


# Create your views here.

def website(request):
    return render(request,'website.html')

class Contact(View):

    def get(self,request):
        return render(request,'contact.html')
    
    def post(self,request):
        class ContactForm(forms.ModelForm):
            class Meta:
                model=models.Contact
                fields='__all__'
        contact=ContactForm(request.POST)
        contact.save()
        return website(request)



def about(request):
    return render(request,'about.html')

def help(request):
    return render(request,'help.html')

@login_required
def service(request):
    queryset=Dog.objects.all()
    dogs={'dog':queryset}
    print(dogs)
    return render(request,'service.html',dogs)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name=forms.CharField(label="firstname")
    last_name=forms.CharField(label="lastname")

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2', )


class RegisterView(FormView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('website')
    template_name = 'registration/register.html'
    form_class = RegisterForm
    

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('website')
        return super(RegisterView,self).get(request,*args,**kwargs)

        
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(RegisterView, self).form_valid(form)
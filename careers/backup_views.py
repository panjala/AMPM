from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import logout
from forms import NameForm,CareersForm,ExpForm
from models import Careers,Profile,Exp
import pdb
#from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.sessions.models import Session
#from django.http import HttpResponseRedirect,HttpResponse
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
EMAIL_SUBJECT = 'profile information'
EMAIL_BODY = 'Dear'


# Create your views here.
def careers(request):
    return render(request,"careers.html") 

def fresher(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print username, password
        from django.contrib import auth 
        user = auth.authenticate(username=username,password=password)
        print user
        if user is not None and user.is_active:
           from django.contrib import auth
           auth.login(request, user) 
           return HttpResponseRedirect("/profile/")
        else:
                e = "yes"
    return render(request,"fresher.html", locals())
def Experience(request):
     if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print username, password
        from django.contrib import auth
        user = auth.authenticate(username=username,password=password)
        print user
        if user is not None and user.is_active:
           from django.contrib import auth
           auth.login(request, user)
           return HttpResponseRedirect("/expprofile/")
        else:
                e = "yes"
     return render(request,"experience.html")
@login_required(login_url='/exp/')
def Exp_Profile(request):
    if request.method=="POST":
        form=ExpForm(request.POST,request.FILES)
        if form.is_valid():
            primary=form.cleaned_data['primary']
            secondary=form.cleaned_data['secondary']
            role=form.cleaned_data['role']
            designation=form.cleaned_data['secondary']
            exp=form.cleaned_data['exp']
            email=form.cleaned_data['email']
            ctc=form.cleaned_data['ctc']
            exp_ctc=form.cleaned_data['exp_ctc']
            reason_for_change=form.cleaned_data['reason_for_change']
            current_company=form.cleaned_data['current_company']
            docfile=form.cleaned_data['docfile']
            e=Exp()
            e.primary=primary
            e.secondary=secondary
            e.role=role
            e.designation= designation
            e.exp=exp
            e.ctc=ctc
            e.exp_ctc=exp_ctc
            e.reason_for_change=reason_for_change
            e.current_company=current_company
            e.email=email
            e.docfile=docfile
            e.save()
            success = "yes"
            from email.mime.text import MIMEText
            #attachment.add_header('Content-Disposition', 'attachment', filename=f) 
            success = "yes"
            subject="profile informayion"
            #url='http://127.0.0.1:8000/resetpwd/'
            url='http://127.0.0.1:8000/resetpwd/{0}'
            html_content='<a href="%s" > download</a>'% url
            body = preprocess_email_body(request,  html_content)
            email = EmailMessage(subject, body, to=[email])
            try:
              #email =EmailMultiAlternatives(subject,body,to=[email])
              email.attach(docfile.name, docfile.read(), docfile.content_type)
              content_subtype = "html"
              #email.attach_alternative(html_content, "text/html")
              #email.attach(attachment)
              email.send()
              #return render(request,"profile.html",locals())       
              success = "yes"
            except Exception as e:
              print e


            success="yes"
            return render (request,"expprofile.html",locals())
        else:
            error = "yes"
            print "34233333434", form.errors
    else:
        form=ExpForm()
    return render(request,"expprofile.html",{"form":form})
def Walkin(request):

    return render(request,"walkin.html")
def validation(data):
    username = data.get("username", None)
    try:
        user = User.objects.get(username__iexact=username)
        return False
    except User.DoesNotExist:
        return True
def register(request):
    if request.method == 'POST':
        print validation(request.POST)
        if validation(request.POST):
            username=request.POST.get("username", None)
            password=request.POST.get("password", None)
            email=request.POST.get("email", None)
            print username, password, email
            user = User.objects.create_user(
            username=username,
            password=password,
            email=email
            )
            user.save()
            success = "yes"
            #return HttpResponseRedirect('/fresher/')
        else:
             error = "yes"

    return render(request,"register.html",locals())
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
def forgotpwd(request):
    if request.method=="POST":
        email=request.POST.get('email')
        session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]
        print session_key
        session = Session.objects.get(session_key=session_key)
        print session
        session_data = session.get_decoded()
        print session_data
        uid = session_data.get('_auth_user_id')
        print email,uid
        subject="Reset Password"
        #url='http://127.0.0.1:8000/resetpwd/'

        url='http://127.0.0.1:8000/resetpwd/{0}'.format(uid)
        html_content='<a href="%s" > click here</a>'% url
        body = preprocess_email_body(request,  html_content)
        #email = EmailMessage(subject, body, to=[email])
        email =EmailMultiAlternatives(subject,body,to=[email])
        content_subtype = "html"
        email.attach_alternative(html_content, "text/html")
        email.send()
        #return render(request,"profile.html",locals())       
        success = "yes"

       # return HttpResponse('success')
    return render (request,"forgotpwd.html",locals())

def resetpwd(request,uid):
    if request.method=="POST":
        pwd=request.POST.get('password')

        print pwd
        from django.contrib.auth.models import User
        print uid
        user = User.objects.get(id=uid)
        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        user.set_password(pwd)
        user.save()
        return HttpResponse('Password reset')
    else:
        return render(request,"resetpwd.html",locals())
@login_required(login_url='/fresher/')

def profile(request):
    if request.method=="POST":
        form=NameForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            surname=form.cleaned_data['surname']
            email=form.cleaned_data['email']
            ssc=form.cleaned_data['ssc']
            inter=form.cleaned_data['inter']
            phone_number=form.cleaned_data['phone_number']
            highest_qualification=form.cleaned_data['highest_qualification']
            docfile=form.cleaned_data['docfile']
            p=Profile()
            p.name=name
            p.surname=surname
            p.email=email
            p.ssc=ssc
            p.inter=inter
            p.phone_number=phone_number
            p.highest_qualification=highest_qualification
            p.docfile=docfile
            p.save()
            print docfile
            from email.mime.text import MIMEText
            #attachment.add_header('Content-Disposition', 'attachment', filename=f) 
            success = "yes"
            subject="profile informayion"
            #url='http://127.0.0.1:8000/resetpwd/'
            url='http://127.0.0.1:8000/resetpwd/{0}'
            html_content='<a href="%s" > download</a>'% url
            body = preprocess_email_body(request,  html_content)
            email = EmailMessage(subject, body, to=[email])
            try:
              #email =EmailMultiAlternatives(subject,body,to=[email])
              email.attach(docfile.name, docfile.read(), docfile.content_type)
              content_subtype = "html"
              #email.attach_alternative(html_content, "text/html")
              #email.attach(attachment)
              email.send()
              #return render(request,"profile.html",locals())       
              success = "yes"
            except Exception as e:
              print e
             
            return render (request,"profile.html",locals())
        else:
            error = "yes"
            print "34233333434", form.errors
    else:
        form=NameForm()
    return render(request,"profile.html",{"form":form})
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/fresher/")
def success(request):
    return render(request,"success.html")
def upcomming_open(request):
     if request.method=="POST":
        form= CareersForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']
            c=Careers()
            c.firstname=firstname
            c.lastname=lastname
            c.email=email
            c.save()
            subject="profile informayion"
            print firstname
            firstname=firstname
            html_content='Hi'
            body = preprocess_email_to_careers_body(request,  firstname,html_content)
            print body
            body = body.replace('\n', '<br/>')
            #email = EmailMessage(subject, body, to=[email])
            email =EmailMultiAlternatives(subject,body,to=[email])
            content_subtype = "html"
            email.attach_alternative(html_content, "text/html")
            email.send()
            success = "yes"
            return render (request,"upcomming.html",locals())
        else:
            error = "yes"
            print "34233333434", form.errors
     else:
        form=CareersForm()
     return render(request,"upcomming.html",{"form":form})
def preprocess_email_body(request, url='url'):
    return ''
def facebook(request):
    url="https://www.facebook.com/peopletechInc"
    return HttpResponseRedirect(url)
def google(request):
    url="https://plus.google.com/+PeopleTechGroupInc/posts"
    return HttpResponseRedirect(url)
def linkedin(request):
    url="https://www.linkedin.com/company/people-tech-group-in"
    return HttpResponseRedirect(url)
def youtube(request):
    url="https://www.youtube.com/user/PeopleTechInc"
    return HttpResponseRedirect(url)
def twitter(request):
    url="https://twitter.com/peopletechinc"
    return HttpResponseRedirect(url)
def preprocess_email_to_careers_body(request, firstname='firstname',html_content=''):
    return EMAIL_BODY\
    .replace('{firstname}',firstname)

def editprofilepic(request):
    if request.method=="POST":
        if "image" in request.FILES:
            image = request.FILES['image']
            Profile.ppic=image
            image.save()
            print image
            return HttpResponseRedirect("/profile/")
    return render(request,"ppic.html",locals())


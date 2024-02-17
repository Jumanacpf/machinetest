from django.shortcuts import render,redirect
from .models import Register,Blog
from django.http import HttpResponse

# Create your views here.

def userregister(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        data=Register.objects.create(first_name=first_name,
                                     last_name=last_name,
                                     username=username,
                                     email=email,
                                     address=address,
                                     phone=phone,
                                     password=password)
        data.save()
        return redirect(userlogin)
        # return HttpResponse("registered")
    else:
        return render(request,'register.html')


def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=int(request.POST['password'])
        data = Register.objects.get(username=username)
        if data.password == password:
            request.session['id'] = data.id
            return redirect(userhome)
        else:
            return render(request, 'login.html',{'error':'Invalid Credential'})
    else:
        return render(request,'login.html')

def createblog(request):
    id = request.session['id']
    userdata = Register.objects.get(id=id)
    if request.method=='POST':
        title=request.POST['title']
        image=request.FILES['image']
        description=request.POST['description']
        data=Blog.objects.create(register_id=userdata,
                                 title=title,
                                 image=image,
                                 description=description)
        data.save()
        return redirect(userhome)
    else:
        return render(request,'createblog.html')
def editblog(request,blogid):
    id = request.session['id']
    userdata = Register.objects.get(id=id)
    blog=Blog.objects.get(id=blogid)

    if request.method=='POST':
        blog.title=request.POST['title']
        blog.image = request.POST['image']
        blog.description = request.POST['description ']
        blog.save()
        return HttpResponse("edited")
    else:
        return render(request, 'editblog.html',{'blog':blog})

def deleteblog(request,blogid):
    id = request.session['id']
    userdata = Register.objects.get(id=id)
    data= Blog.objects.filter(id=blogid)
    data.delete()
    return redirect(viewblog)

def viewblog(request):
    id = request.session['id']
    userdata = Register.objects.get(id=id)
    datas = Blog.objects.filter(register_id=userdata)
    return render(request,'viewblog.html',{'datas':datas})

def allblog(request):
    data=Blog.objects.all()
    return render (request,'allblog.html',{'data':data})

def logout(request):
    request.session.flush()
    return redirect(index)



def userhome(request):
    return render(request,'userhome.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def post(request):
    return render(request,'post.html')

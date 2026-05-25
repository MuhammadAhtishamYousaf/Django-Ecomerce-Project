from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from app.forms.form import SignupForm, loginForm
from app.models import AppModel, BlogModel, SignupModel

import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 

def home(request):
    # context = {
    #     # 'name':'Ahtisham',
    #     'course_list':['Pytorch','Python','Django'],
    #     'numbers' : [10,20,30,40,50],
    #     'student_details': [
    #         {"name": 'Ahtisham','phone': 545345454},
    #         {'name' : 'Parveen','phone': 345345435}
    #     ]
    # }
    # return render(request,'index.html',context)
    return render (request,'home.html')

def allah(request):
    return HttpResponse("Allah pak help me please!")

def about(request):
    if request.method == 'GET':
        output = request.GET.get('output')
    return render(request, 'about.html',context = {'output':output})

def contact(request):

    return render(request, 'contact.html')

def blog(request):
    blog_data = BlogModel.objects.all() #to get all the data
    # blog_data = BlogModel.objects.filter(blog_title__icontains = 'django') #to get data with specific condition
    # blog_data = BlogModel.objects.order_by('-id') # to order data in descending order
    print(len(blog_data))
    return render(request, 'blog.html',{'blog_data': blog_data})


def shop(request):
    object_list = AppModel.objects.all() # Get the queryset of object to paginate

    paginator = Paginator(object_list, 1) # Show 1 object per page

    page_number = request.GET.get('page')
    print(f"Page num : {page_number}")
    total_pages = paginator.num_pages
    print(f'total _pages : {total_pages}')
    try:
        page_obj = paginator.page(page_number)
        print(f"Page obj : {page_obj}")
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)


    if request.GET.get('prod_name'):
        prod_name = request.GET.get('prod_name')
        page_obj = AppModel.objects.filter(p_name__icontains = prod_name)

    context = {'page_obj': page_obj}
    return render(request, 'shop.html', context)

def submit(request):
    try:
        if request.method == 'POST':

            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            # return HttpResponse(final_output)
            return render(request, 'submit.html',context = {'name':name,'username':username, 'email': email})

    except:
        return HttpResponse("ERROR")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # process form data here (e.g., save user)
            return redirect(login_form)
    
    # save every important detail comming with requsest in a dict with key and value pair and pass that dict in render function as context
    request_data = {
        'name': request.POST.get('name'),
        'username': request.POST.get('username'),
        'email': request.POST.get('email')
    }
    return HttpResponse(request_data)
    # return render(request, 'signup.html', {'form': form})


def login_form(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
      
        user_password = request.POST.get('password')
        user = SignupModel.objects.get(username=username, password=user_password)
        print(f'User : {user}')
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect(home)  # Redirect to a post-login page
        else:
            messages.error(request, 'Username or password is incorrect!')
            return render(request, 'login.html',)


def forgot_password(request):
    if request.method == 'POST':
        
        from django.contrib.auth.models import User
        user = User.objects.get(username='your_admin_username')
        user.set_password('your_new_password')
        user.save()

    
    return render(request, 'forgot_password.html')


def course_details(request, courseid):
    return HttpResponse(courseid)


def calculator(request):
    c = ''
    print(f"request ===== {request.method}")
    try:
        if request.method == 'POST':
            val1 = eval(request.POST.get('val1'))
            opr = request.POST.get('opr')
            val2 = eval(request.POST.get('val2'))
            print(f'opr ===== {opr}')
            print(f'val1 ===== {val1}')
            print(f'val2 ===== {val2}')

            if opr == '+': 
                c  = val1 + val2
            elif opr == '-':
                c = val1 - val2 

            elif opr == '*':
                c = val1 * val2 

            elif opr == '/':
                c = val1 / val2
            return render(request, 'calculator.html', context = {'c':c})
        

        elif request.method == 'GET':
            print("GET request = ",request)
            return render(request, 'calculator.html')


    except Exception as e: 
    #     print(f"Error : {str(e)}")
        c = str(e)
        return HttpResponse(c)


def even_odd(request):
    output = ''
    print(f'Request ========== {request.method}')
    try:
        if request.method == 'POST':
            val = eval(request.POST.get('val'))
            if val % 2 == 0:
                output = 'EVEN'
            elif val % 2 != 0 :
                output = 'ODD'
        # elif request.method == 'GET':
        #     return render(request, 'even_odd.html')
        
    except Exception as e:
        return HttpResponse(str(e))
    return render(request, 'even_odd.html',{'c': output})


def marksheet(request):
    if request.method == 'POST':
        s1 = request.POST.get('sub1', '')
        s2 = request.POST.get('sub2', '')
        s3 = request.POST.get('sub3', '')
        s4 = request.POST.get('sub4', '')
        s5 = request.POST.get('sub5', '')

        if s1 == '':
            return render(request, 'marksheet.html', {'error': True, 'sub1': s1, 'sub2': s2, 'sub3': s3, 'sub4': s4, 'sub5': s5})

        try:
            sub1 = eval(s1)
            sub2 = eval(s2)
            sub3 = eval(s3)
            sub4 = eval(s4)
            sub5 = eval(s5)
        except Exception:
            return render(request, 'marksheet.html', {'error': True, 'sub1': s1, 'sub2': s2, 'sub3': s3, 'sub4': s4, 'sub5': s5})

        total = sub1 + sub2 + sub3 + sub4 + sub5
        perc = math.floor(total / 500 * 100)

        if perc > 90:
            division = 'A'
        elif perc > 80:
            division = 'B'
        elif perc > 70:
            division = 'C'
        else:
            division = 'D'

        data = {'total': total, 'perc': perc, 'division': division, 'sub1': s1, 'sub2': s2, 'sub3': s3, 'sub4': s4, 'sub5': s5}
        return render(request, 'marksheet.html', data)

    return render(request, 'marksheet.html')


def blog_detail(request, blog_slug):
    print(f'Blog ID ========== {blog_slug}')
    blog_detail = BlogModel.objects.get(blog_slug = blog_slug)
    data = {'blog_detail':blog_detail}
    return render(request, 'blog_detail.html', data)


def form_testing(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age  = form.cleaned_data['age']
            is_super = form.cleaned_data['is_super']
            
            context = {
                'form': form, 
                'password': password, 
                'email': email, 'age': age, 
                'is_super': is_super
                }
            
            return render(request, 'form_testing.html', context = context)
    else:
        form = loginForm()
    return render(request, 'form_testing.html', context = {'form': form})